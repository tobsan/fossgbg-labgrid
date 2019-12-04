import pytest

@pytest.fixture(scope='session')
def powertwo(env):
    target = env.get_target("pitwo")
    strat = target.get_driver("ShellStrategy")
    strat.transition("shell")
    yield target
    strat.transition("off")

@pytest.fixture(scope='session')
def power(target):
    strat = target.get_driver("ShellStrategy")
    strat.transition("shell")
    yield
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
    pinzero = int(env.get_option("gpio_pin_zero"))
    pintwo = int(env.get_option("gpio_pin_two"))
    return (pinzero, pintwo)
