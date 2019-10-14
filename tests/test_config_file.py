import pytest

from src.fund_my_watcard.config_file import check_config_file


@pytest.mark.skip(reason="util function, no need to test")
def assert_report_error(config):
    with pytest.raises(SystemExit) as e:
        check_config_file(config)
    assert e.type == SystemExit
    assert e.value.code == 1


def test_user_name():
    _config = {"userName": "userName"}
    assert_report_error(_config)


def test_ord_name():
    _config = {"userName": "username", "ordName": "ord Name!"}
    assert_report_error(_config)


def test_postal_code():
    _config = {"userName": "username", "ordName": "ord Name", "ordPostalCode": "D1L D2L"}
    assert_report_error(_config)
