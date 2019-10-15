import time
import platform
import subprocess
import os
import json

from cryptography.fernet import InvalidToken, Fernet

from .util import (
    report_error,
    report_warning,
    report_success,
    check_trn_card_cvd,
    check_trn_exp_year,
    check_trn_exp_month,
    check_trn_card_number,
    check_trn_card_type,
    check_trn_card_owner,
    check_payment_method,
    check_email_address,
    check_ord_city,
    check_ord_postal_code,
    check_phone_number,
    check_ord_name,
    check_user_name,
)
from .messages import (
    CONFIG_FILE_ALREADY_EXISTS,
    OPENING_CONFIG_FILE,
    GENERATE_CONFIG_FILE_SUCCESSFULLY,
    RESET_CONFIG_FILE_SUCCESSFULLY,
    INVALID_PASSWORD,
    DECRYPTING_CONFIG_FILE_FAILED,
    VALID_CONFIG_FILE,
)

USER_DIR = os.path.expanduser("~")
CONFIG_FILE_PATH = USER_DIR + "/.watcard_config"


def open_config_file():
    operating_system = platform.system()
    if operating_system == "Linux":
        subprocess.call(["vi", CONFIG_FILE_PATH])
    elif operating_system == "Windows":
        subprocess.call(["notepad.exe", CONFIG_FILE_PATH])
    elif operating_system == "Darwin":
        subprocess.call(["open", CONFIG_FILE_PATH])


def generate_config_file():
    if os.path.isfile(CONFIG_FILE_PATH):
        report_warning(CONFIG_FILE_ALREADY_EXISTS)
        report_warning(OPENING_CONFIG_FILE.format(CONFIG_FILE_PATH))
        time.sleep(1)
        open_config_file()
        return

    write_template_to_config_file()
    report_success(GENERATE_CONFIG_FILE_SUCCESSFULLY)
    report_success(OPENING_CONFIG_FILE.format(CONFIG_FILE_PATH))
    time.sleep(1)
    open_config_file()


def reset_config_file():
    write_template_to_config_file()
    report_success(RESET_CONFIG_FILE_SUCCESSFULLY)


def check_config_file(config):
    check_user_name(config["userName"])
    check_ord_name(config["ordName"])
    check_phone_number(config["phoneNumber"])
    check_ord_postal_code(config["ordPostalCode"])
    check_ord_city(config["ordCity"])
    check_email_address(config["ordEmailAddress"])
    check_payment_method(config["paymentMethod"])
    check_trn_card_owner(config["trnCardOwner"])
    check_trn_card_type(config["trnCardType"])
    check_trn_card_number(config["trnCardNumber"])
    check_trn_exp_month(config["trnExpMonth"])
    check_trn_exp_year(config["trnExpYear"])
    check_trn_card_cvd(config["trnCardCvd"])
    report_success(VALID_CONFIG_FILE)


def write_template_to_config_file():
    # TODO Read the template from a json file.
    _config_info = {
        "userName": "WatIAM username",
        "password": "WatIAM password",
        "ordName": "Name on the credit card",
        "phoneNumber": "Phone number",
        "address1": "Home address 1",
        "address2": "Home address 2 (Blank if no address2)",
        "ordPostalCode": "Postal code",
        "ordCity": "City",
        "ordCountry": "Country (Canada by default)",
        "ordProvince": "Province (Ontario by default)",
        "ordEmailAddress": "Email address",
        "paymentMethod": "Payment method ('CC' for 'Credit Card')",
        "trnCardOwner": "Card owner",
        "trnCardType": "Card type ('VI' for 'Visa', 'MC' for 'Master Card', see more card types in README)",
        "trnCardNumber": "Card number",
        "trnExpMonth": "Expiry month",
        "trnExpYear": "Expiry year",
        "trnCardCvd": "Card CVD (3 digit number on the back of the card)",
        "encrypted": "False",
    }
    with open(CONFIG_FILE_PATH, "w+") as f:
        json.dump(_config_info, f, indent=2)
    assert os.path.isfile(CONFIG_FILE_PATH) is True


def encrypt_config_file(config: dict, f: Fernet) -> dict:
    for k, v in config.items():
        config[k] = f.encrypt(v.encode()).decode("utf8")
    return config


def decrypt_config_file(config: dict, f: Fernet) -> dict:
    try:
        f.decrypt(config["encrypted"].encode())
    except InvalidToken:
        report_error(" ".join([INVALID_PASSWORD, DECRYPTING_CONFIG_FILE_FAILED]))
    for k, v in config.items():
        config[k] = f.decrypt(v.encode()).decode("utf8")
    return config
