from fund_my_watcard.config import VERSION
from .util import out


def test_print_version():
    _version = out("watcard --version")
    assert _version.strip() == "fund-my-watcard v{}".format(VERSION)
