from importlib.machinery import SourceFileLoader

from .util import out

VERSION = SourceFileLoader("version", "src/fund_my_watcard/version.py").load_module().VERSION


def test_print_version():
    _version = out("watcard --version")
    assert _version.strip() == "fund-my-watcard v{}".format(VERSION)
