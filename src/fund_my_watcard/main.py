import argparse
import json
import os
import re

from cryptography.fernet import Fernet

from .version import VERSION
from .util import report_error, report_success, report_warning, report_fail, query_yes_no, input_and_encrypt_password
from .mywatcard import MyWatCard
from .config_file import (
    CONFIG_FILE_PATH,
    generate_config_file,
    reset_config_file,
    decrypt_config_file,
    encrypt_config_file,
)
from .messages import (
    CAN_NOT_FIND_CONFIG_FILE,
    CONFIG_FILE_HAS_BEEN_ENCRYPTED,
    ADDING_FUND_FAILED,
    ADDING_FUND_SUCCESSFULLY,
    WILL_DECRYPT_YOUR_CONFIG_FILE_WARNING,
    WILL_ENCRYPT_YOUR_CONFIG_FILE_WARNING,
    WILL_RESET_YOUR_CONFIG_FILE_WARNING,
    IS_ALREADY_DECRYPTED,
    IS_ALREADY_ENCRYPTED,
    CONFIG_FILE_SUCCESSFULLY_DECRYPTED,
    CONFIG_FILE_SUCCESSFULLY_ENCRYPTED,
    INVALID_CONFIG_FILE,
)
from .log import init_logger
from .transaction import print_transactions


def main():
    logfile = init_logger()
    parser = argparse.ArgumentParser(description="Fund my WatCard: A tool that add funds to your WatCard easily.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-c", "--config", help="generate the config file", action="store_true")
    group.add_argument("-f", "--fund", type=float, help="the amount to add into the WatCard", action="store")
    group.add_argument("-v", "--version", help="show the version of fund-my-watcard", action="store_true")
    group.add_argument(
        "-e", "--encrypt", help="encrypt the config file with user defined password", action="store_true"
    )
    group.add_argument("-d", "--decrypt", help="decrypt the config file so you can edit it", action="store_true")
    group.add_argument("-r", "--reset", help="reset the config file", action="store_true")
    group.add_argument("-va", "--valid", help="check if the config file is valid", action="store_true")
    group.add_argument("-t", "--transaction", help="review previous transactions", action="store_true")
    args = parser.parse_args()

    if args.transaction:
        print_transactions(logfile)

    elif args.config:
        generate_config_file()

    elif args.fund:
        amount = round(args.fund, 2)
        if os.path.isfile(CONFIG_FILE_PATH):
            try:
                with open(CONFIG_FILE_PATH) as f:
                    _config = json.load(f)
                if _config["encrypted"] != "False":
                    report_warning(CONFIG_FILE_HAS_BEEN_ENCRYPTED)
                    f = Fernet(input_and_encrypt_password())
                    decrypt_config_file(_config, f)
                _my_wat_card = MyWatCard(**_config)
                res = _my_wat_card.add_fund(amount)
                if res:
                    report_success(ADDING_FUND_SUCCESSFULLY.format(amount, _config["userName"]))
                else:
                    report_fail(ADDING_FUND_FAILED.format(amount, _config["userName"]))
            except json.decoder.JSONDecodeError:
                report_fail(INVALID_CONFIG_FILE)
        else:
            report_error(CAN_NOT_FIND_CONFIG_FILE)
    elif args.version:
        from .util import PRINT_PREFIX

        print(PRINT_PREFIX + " v{}".format(VERSION))

    elif args.encrypt:
        if query_yes_no(WILL_ENCRYPT_YOUR_CONFIG_FILE_WARNING, "no"):
            if os.path.isfile(CONFIG_FILE_PATH):
                with open(CONFIG_FILE_PATH) as f:
                    _config = json.load(f)
            else:
                report_error(CAN_NOT_FIND_CONFIG_FILE)

            if _config["encrypted"] != "False":
                report_warning(IS_ALREADY_ENCRYPTED)
            else:
                if os.path.isfile(CONFIG_FILE_PATH):
                    with open(CONFIG_FILE_PATH) as f:
                        _config = json.load(f)
                else:
                    report_error(CAN_NOT_FIND_CONFIG_FILE)

                f = Fernet(input_and_encrypt_password())
                _encrypted_config_info = encrypt_config_file(_config, f)

                with open(CONFIG_FILE_PATH, "w+") as json_file:
                    json.dump(_encrypted_config_info, json_file, indent=2)

                report_success(CONFIG_FILE_SUCCESSFULLY_ENCRYPTED)

    elif args.decrypt:
        if query_yes_no(WILL_DECRYPT_YOUR_CONFIG_FILE_WARNING, "no"):
            if os.path.isfile(CONFIG_FILE_PATH):
                with open(CONFIG_FILE_PATH) as f:
                    _config = json.load(f)
            else:
                report_error(CAN_NOT_FIND_CONFIG_FILE)

            if _config["encrypted"] == "False":
                report_warning(IS_ALREADY_DECRYPTED)
            else:
                if os.path.isfile(CONFIG_FILE_PATH):
                    with open(CONFIG_FILE_PATH) as f:
                        _config = json.load(f)
                else:
                    report_error(CAN_NOT_FIND_CONFIG_FILE)

                f = Fernet(input_and_encrypt_password())
                _decrypted_config_info = decrypt_config_file(_config, f)

                with open(CONFIG_FILE_PATH, "w+") as json_file:
                    json.dump(_decrypted_config_info, json_file, indent=2)

                report_success(CONFIG_FILE_SUCCESSFULLY_DECRYPTED)

    elif args.reset:
        if query_yes_no(WILL_RESET_YOUR_CONFIG_FILE_WARNING, "no"):
            reset_config_file()

    elif args.valid:
        if os.path.isfile(CONFIG_FILE_PATH):
            with open(CONFIG_FILE_PATH) as f:
                _config = json.load(f)
        else:
            report_error(CAN_NOT_FIND_CONFIG_FILE)

        if _config["encrypted"] == "True":
            report_warning(CONFIG_FILE_HAS_BEEN_ENCRYPTED)
        else:
            if os.path.isfile(CONFIG_FILE_PATH):
                with open(CONFIG_FILE_PATH) as f:
                    _config = json.load(f)
            else:
                report_error(CAN_NOT_FIND_CONFIG_FILE)

            errors_found = False

            if re.fullmatch('[!@#$%^&*(),.?":{}|<>]', _config["userName"]):
                report_warning("userName has special characters, please remove them.")
                errors_found = True

            if re.fullmatch("([a-zA-Z]+ +)", _config["ordName"]):
                report_warning("ordName has characters other than letters, please remove them.")
                errors_found = True

            if len(_config["phoneNumber"]) != 10:
                report_warning("phoneNumber has too few or too many characters, please check it.")
                errors_found = True

            if not re.fullmatch(
                "[ABCEGHJKLMNPRSTVXY][0-9][ABCEGHJKLMNPRSTVWXYZ] ?[0-9][ABCEGHJKLMNPRSTVWXYZ][0-9]",
                _config["ordPostalCode"],
            ):
                report_warning("ordPostalCode is not a valid postal code, please check it.")
                errors_found = True

            if not re.fullmatch("([a-zA-Z]+)", _config["ordCity"]):
                report_warning("ordCity has characters other than letters, please remove them.")
                errors_found = True

            if not re.fullmatch("([^@]+@[^@]+\\.[^@]+)", _config["ordEmailAddress"]):
                report_warning("ordEmailAddress is not a valid email address, please check it.")
                errors_found = True

            if _config["paymentMethod"] != "CC":
                report_warning("paymentMethod is not CC, please check it.")
                errors_found = True

            if re.fullmatch("([a-zA-Z]+ +)", _config["trnCardOwner"]):
                report_warning("trnCardOwner has characters other than letters, please remove them.")
                errors_found = True

            if not re.fullmatch("(MC|VI|PV|MD|AM)", _config["trnCardType"]) and len(_config["trnCardType"]) != 2:
                report_warning("trnCardType is an unsupported card type, please check it.")
                errors_found = True

            if len(_config["trnExpMonth"]) != 2:
                report_warning("trnExpMonth is not valid, please check it.")
                errors_found = True

            if len(_config["trnExpYear"]) != 2:
                report_warning("trnExpYear is not valid, please check it.")
                errors_found = True

            if len(_config["trnCardCvd"]) != 3:
                report_warning("trnCardCvd is not valid, please check it.")
                errors_found = True

            # TODO add a function to validate credit card number (this needs an algorithm)

            if not errors_found:
                report_success("The config file is valid.")

    else:
        parser.parse_args(["-h"])
