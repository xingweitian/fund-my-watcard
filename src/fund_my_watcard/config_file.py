import time
import platform
import subprocess
import os
import json
import re

from cryptography.fernet import InvalidToken, Fernet

from .util import report_error, report_warning, report_success, valid_card_number
from .messages import (
    CONFIG_FILE_ALREADY_EXISTS,
    OPENING_CONFIG_FILE,
    GENERATE_CONFIG_FILE_SUCCESSFULLY,
    RESET_CONFIG_FILE_SUCCESSFULLY,
    INVALID_PASSWORD,
    DECRYPTING_CONFIG_FILE_FAILED,
)
from .mywatcard import card_type

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
    if re.fullmatch(r'[!@#$%^&*(),.?":{}|<>]', config["userName"]):
        report_error("userName has special characters, please remove them.")

    if re.fullmatch(r"([a-zA-Z]+ )", config["ordName"]):
        report_error("ordName has characters other than letters, please remove them.")

    if not re.fullmatch(r"^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$", config["phoneNumber"]):
        report_error("phoneNumber isn't formatted correctly, please check it.")

    if not re.fullmatch(
        r"[ABCEGHJKLMNPRSTVXY][0-9][ABCEGHJKLMNPRSTVWXYZ] ?[0-9][ABCEGHJKLMNPRSTVWXYZ][0-9]", config["ordPostalCode"]
    ):
        report_error("ordPostalCode is not a valid postal code, please check it.")

    if not re.fullmatch(r"([a-zA-Z]+)", config["ordCity"]):
        report_error("ordCity has characters other than letters, please remove them.")

    if not re.fullmatch(r"([^@]+@[^@]+\.[^@]+)", config["ordEmailAddress"]):
        report_error("ordEmailAddress is not a valid email address, please check it.")

    if config["paymentMethod"] != "CC":
        report_error("paymentMethod is not CC, please check it.")

    if re.fullmatch(r"([a-zA-Z]+ )", config["trnCardOwner"]):
        report_error("trnCardOwner has characters other than letters, please remove them.")

    if config["trnCardType"] not in card_type:
        report_error("trnCardType is an unsupported card type, please check it.")

    if not valid_card_number(config["trnCardNumber"].replace(" ", "")):
        report_error("trnCardNumber is not a valid card number, please check it.")

    if len(config["trnExpMonth"]) != 2:
        report_error("trnExpMonth is not valid, please check it.")

    if len(config["trnExpYear"]) != 2:
        report_error("trnExpYear is not valid, please check it.")

    if not re.fullmatch(r"^[0-9]{3,4}$", config["trnCardCvd"]):
        report_error("trnCardCvd is not valid, please check it.")

    report_success("The config file is valid.")


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
