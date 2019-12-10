import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--keepalive", action="store_true", default=False, help="Don't power down after tests"
    )
    parser.addoption(
        "--assume-on", action="store_true", default=False, help="Assume target is powered on already"
    )

@pytest.fixture(scope='session')
def keepalive(request):
    return request.config.getoption("--keepalive")

@pytest.fixture(scope='session')
def assume_on(request):
    return request.config.getoption("--assume-on")

@pytest.fixture(scope='session')
def powertwo(env, keepalive, assume_on):
    target = env.get_target("pitwo")
    strat = target.get_driver("ShellStrategy")
    if not assume_on:
        strat.transition("shell")
    yield target
    if not keepalive:
        strat.transition("off")

@pytest.fixture(scope='session')
def power(target, keepalive, assume_on):
    strat = target.get_driver("ShellStrategy")
    if not assume_on:
        strat.transition("shell")
    yield target
    if not keepalive:
        strat.transition("off")

@pytest.fixture(scope='session')
def powerboth(power, powertwo):
    yield

@pytest.fixture(scope='session')
def sh_zero(power, target):
    shell = target.get_driver('CommandProtocol')
    return shell

@pytest.fixture(scope='session')
def sh_two(powertwo):
    shell = powertwo.get_driver('CommandProtocol')
    return shell
    
@pytest.fixture(scope='session')
def gpios(env):
    pinzero = int(env.config.get_option("gpio_pin_zero"))
    pintwo = int(env.config.get_option("gpio_pin_two"))
    return (pinzero, pintwo)
