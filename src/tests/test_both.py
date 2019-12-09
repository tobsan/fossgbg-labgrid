import pytest

def test_both_shells(sh_zero, sh_two):
    # Check shell of first target
    stdout, stderr, returncode = sh_zero.run('cat /proc/cpuinfo')
    assert returncode == 0
    assert stdout
    assert not stderr
    assert 'Raspberry Pi Zero' in stdout[-1]

    # Check shell of second target
    stdout, stderr, returncode = sh_two.run('cat /proc/cpuinfo')
    assert returncode == 0
    assert stdout
    assert not stderr
    assert 'Raspberry Pi 2 Model B' in stdout[-1]

# TODO: Parameterize to go both ways
def test_gpio_connection(sh_zero, sh_two, gpios):
    (pin_zero, pin_two) = gpios
    gpio_path = '/sys/class/gpio/gpio'

    # Export the gpios
    sh_zero.run('echo {} > /sys/class/gpio/export'.format(pin_zero))
    sh_two.run('echo {} > /sys/class/gpio/export'.format(pin_two))

    # Set directions
    sh_zero.run('echo in > /sys/class/gpio/gpio{}/direction'.format(pin_zero))
    sh_two.run('echo out > /sys/class/gpio/gpio{}/direction'.format(pin_two))

    # Write to one, read from the other
    for n in [1,0,1,1,1,0,0,0,1]:
        sh_two.run('echo {} > /sys/class/gpio/gpio{}/value'.format(n, pin_two))
        stdout, stderr, returncode = sh_zero.run('cat /sys/class/gpio/gpio{}/value'.format(pin_zero))
        assert not stderr
        assert returncode == 0
        assert int(stdout[0].strip()) == n


