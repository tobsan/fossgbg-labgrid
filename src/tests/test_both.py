import pytest

def test_both_shells(sh_zero, sh_two):
    # Check shell of first target
    stdout, stderr, returncode = sh.zero.run('cat /proc/version')
    assert returncode == 0
    assert stdout
    assert not stderr
    assert 'Linux' in stdout[0]

    # Check shell of second target
    stdout, stderr, returncode = sh_two.run('cat /proc/version')
    assert returncode == 0
    assert stdout
    assert not stderr
    assert 'Linux' in stdout[0]

# TODO: Parameterize to go both ways
def test_gpio_connection(sh_zero, sh_two, gpios):
    (pin_zero, pin_two) = gpios
    gpio_path = '/sys/class/gpio/gpio'

    # Export the gpios
    sh_zero.run('echo export {} /sys/class/gpio/'.format(pin_zero))
    sh_two.run('echo export {}'.format(pin_two))

    # Set directions

    # Write to one, read from the other

