import time
import platform
import subprocess
import os
import json

from cryptography.fernet import InvalidToken, Fernet

from .util import report_message, report_error

CONFIG_FILE_PATH = os.path.expanduser("~") + "/.watcard_config"


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
        report_message("Config file '.watcard_config' already exists.")
        report_message("Opening " + CONFIG_FILE_PATH + ".")
        time.sleep(1)
        open_config_file()
        return

    write_template_to_config_file()
    report_message("Generate config file at user directory successfully. Please fill your information.")
    report_message("Opening " + CONFIG_FILE_PATH + ".")
    time.sleep(1)
    open_config_file()


def reset_config_file():
    write_template_to_config_file()
    report_message("Reset config file successfully. Try 'watcard --config' to fill your information.")


def write_template_to_config_file():
    _config_info = {
        "userName": "WatIAM username",
        "password": "WatIAM username",
        "ordName": "Name on the credit card",
        "phoneNumber": "Phone number",
        "address1": "Home address 1",
        "address2": "Home address 2 (Blank if no address2)",
        "ordPostalCode": "Postal code",
        "ordCity": "City",
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
        report_error("Invalid password. Decrypting config file failed.")
    for k, v in config.items():
        config[k] = f.decrypt(v.encode()).decode("utf8")
    return config
