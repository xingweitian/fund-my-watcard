import pytest

from src.fund_my_watcard.util import (
    check_user_name,
    check_ord_name,
    check_phone_number,
    check_ord_postal_code,
    check_ord_city,
    check_email_address,
    check_payment_method,
    check_trn_card_owner,
    check_trn_card_type,
    check_trn_card_number,
    check_trn_exp_month,
    check_trn_exp_year,
    check_trn_card_cvd,
)


@pytest.mark.skip(reason="util function, no need to test")
def assert_report_error(checker_func, config):
    with pytest.raises(SystemExit) as e:
        checker_func(config)
    assert e.type == SystemExit
    assert e.value.code == 1


def test_user_name():
    _config = {"userName": "s123Zhang"}
    assert_report_error(check_user_name, _config["userName"])


def test_ord_name():
    _config = {"ordName": "San Zhang!"}
    assert_report_error(check_ord_name, _config["ordName"])


def test_postal_code():
    _config = {"ordPostalCode": "D1L 0B1"}
    assert_report_error(check_ord_postal_code, _config["ordPostalCode"])


def test_phone_number():
    _config = {"phoneNumber": "90512312345"}
    assert_report_error(check_phone_number, _config["phoneNumber"])


def test_ord_city():
    _config = {"ordCity": "Wat3rl00"}
    assert_report_error(check_ord_city, _config["ordCity"])


def test_email_address():
    _config = {"ordEmailAddress": "abc123gmail.com"}
    assert_report_error(check_email_address, _config["ordEmailAddress"])


def test_payment_method():
    _config = {"paymentMethod": "CCC"}
    assert_report_error(check_payment_method, _config["paymentMethod"])


def test_trn_card_onwer():
    _config = {"trnCardOwner": "3an Zhang"}
    assert_report_error(check_trn_card_owner, _config["trnCardOwner"])


def test_trn_card_number():
    _config = {"trnCardNumber": "929 111 929 922"}
    assert_report_error(check_trn_card_number, _config["trnCardNumber"])


def test_trn_exp_month():
    _config = {"trnExpMonth": "00"}
    assert_report_error(check_trn_exp_month, _config["trnExpMonth"])


def test_trn_exp_year():
    _config = {"trnExpYear": "ab"}
    assert_report_error(check_trn_exp_year, _config["trnExpYear"])


def test_trn_card_type():
    _config = {"trnCardType": "AB"}
    assert_report_error(check_trn_card_type, _config["trnCardType"])


def test_trn_card_cvd():
    _config = {"trnCardCVD": "123456"}
    assert_report_error(check_trn_card_cvd, _config["trnCardCVD"])
