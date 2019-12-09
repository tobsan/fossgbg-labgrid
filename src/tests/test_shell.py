def test_shell(sh_zero):
    stdout, stderr, returncode = sh_zero.run('cat /proc/version')
    assert returncode == 0
    assert stdout
    assert not stderr
    assert 'Linux' in stdout[0]

    stdout, stderr, returncode = sh_zero.run('false')
    assert returncode != 0
    assert not stdout
    assert not stderr
