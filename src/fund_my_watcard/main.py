import argparse
import json
import os

from cryptography.fernet import Fernet

from .version import VERSION
from .util import report_error, report_message, PRINT_PREFIX, query_yes_no, encrypt_password, input_and_encrypt_password
from .mywatcard import MyWatCard
from .config_file import (
    CONFIG_FILE_PATH,
    generate_config_file,
    reset_config_file,
    decrypt_config_file,
    encrypt_config_file,
)


def main():
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
    args = parser.parse_args()

    if args.config:
        generate_config_file()

    if args.fund:
        amount = round(args.fund, 2)
        if os.path.isfile(CONFIG_FILE_PATH):
            with open(CONFIG_FILE_PATH) as f:
                _config = json.load(f)
            if _config["encrypted"] != "False":
                report_message("Config file has been encrypted, needs to be decrypted at first.")
                f = Fernet(input_and_encrypt_password())
                decrypt_config_file(_config, f)
            _my_wat_card = MyWatCard(**_config)
            res = _my_wat_card.add_fund(amount)
            if res:
                report_message("Adding ${} to account {} successfully.".format(amount, _config["userName"]))
            else:
                report_message("Adding ${} to account {} failed.".format(amount, _config["userName"]))
        else:
            report_error("Cannot find config file under user directory, try 'watcard --config'.")

    if args.version:
        print("fund-my-watcard v{}".format(VERSION))

    if args.encrypt:
        if query_yes_no(PRINT_PREFIX + "This will encrypt your config file! Do you want to proceed?", "no"):
            if os.path.isfile(CONFIG_FILE_PATH):
                with open(CONFIG_FILE_PATH) as f:
                    _config = json.load(f)
            else:
                report_error("Cannot find config file under user directory, try 'watcard --config'.")

            if _config["encrypted"] != "False":
                report_message("Your config file is already encrypted. To decrypt it, please try 'watcard -d'.")
            else:
                if os.path.isfile(CONFIG_FILE_PATH):
                    with open(CONFIG_FILE_PATH) as f:
                        _config = json.load(f)
                else:
                    report_error("Cannot find config file under user directory, try 'watcard --config'.")

                f = Fernet(encrypt_password(input(PRINT_PREFIX + "Please input your password: ").encode()))
                _encrypted_config_info = encrypt_config_file(_config, f)

                with open(CONFIG_FILE_PATH, "w+") as json_file:
                    json.dump(_encrypted_config_info, json_file, indent=2)

                report_message("Config file successfully encrypted.")

    if args.decrypt:
        if query_yes_no(PRINT_PREFIX + "This will decrypt your config file! Do you want to proceed?", "no"):
            if os.path.isfile(CONFIG_FILE_PATH):
                with open(CONFIG_FILE_PATH) as f:
                    _config = json.load(f)
            else:
                report_error("Cannot find config file under user directory, try 'watcard --config'.")

            if _config["encrypted"] == "False":
                report_message("Your config file is already decrypted. To encrypt it, please use 'watcard -e'.")
            else:
                if os.path.isfile(CONFIG_FILE_PATH):
                    with open(CONFIG_FILE_PATH) as f:
                        _config = json.load(f)
                else:
                    report_error("Cannot find config file under user directory, try 'watcard --config'.")

                f = Fernet(input_and_encrypt_password())
                _decrypted_config_info = decrypt_config_file(_config, f)

                with open(CONFIG_FILE_PATH, "w+") as json_file:
                    json.dump(_decrypted_config_info, json_file, indent=2)

                report_message("Config file successfully decrypted.")

    if args.reset:
        if query_yes_no(PRINT_PREFIX + "This will reset your config file! Do you want to proceed?", "no"):
            reset_config_file()

    if not (args.config or args.fund or args.version or args.encrypt or args.decrypt or args.reset):
        parser.parse_args(["-h"])
