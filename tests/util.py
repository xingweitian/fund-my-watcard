import pytest

from subprocess import PIPE, run


def out(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return result.stdout


def assert_report_error(checker_func, config):
    with pytest.raises(SystemExit) as e:
        checker_func(config)
    assert e.type == SystemExit
    assert e.value.code == 1
