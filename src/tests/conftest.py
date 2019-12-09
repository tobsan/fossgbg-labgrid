import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--keepalive", action="store_true", default=False, help="Don't power down after tests"
    )

@pytest.fixture(scope='session')
def keepalive(request):
    return request.config.getoption("--keepalive")

@pytest.fixture(scope='session')
def powertwo(env, keepalive):
    target = env.get_target("pitwo")
    strat = target.get_driver("ShellStrategy")
    strat.transition("shell")
    yield target
    if not keepalive:
        strat.transition("off")

@pytest.fixture(scope='session')
def power(target):
    strat = target.get_driver("ShellStrategy")
    strat.transition("shell")
    yield
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
