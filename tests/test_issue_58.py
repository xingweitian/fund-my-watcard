from src.fund_my_watcard.util import check_ord_name, check_trn_card_owner


def test_ord_name():
    _config = {"ordName": "San Zhang"}
    assert check_ord_name(_config["ordName"]) is None


def test_trn_card_owner():
    _config = {"trnCardOwner": "San Zhang"}
    assert check_trn_card_owner(_config["trnCardOwner"]) is None
