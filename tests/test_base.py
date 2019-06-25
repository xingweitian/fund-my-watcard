import json
from .util import out


def test_print_version():
    with open("fund-my-watcard/config.json") as f:
        config = json.load(f)
    _version = out("watcard --version")
    assert _version.strip() == "fund-my-watcard v{}".format(config["VERSION"])
