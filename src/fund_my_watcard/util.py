import base64
import getpass
import logging
import re

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

from .messages import (
    CARDNUMBER_ERROR,
    CARDOWNER_ERROR,
    CARDTYPE_ERROR,
    CVD_ERROR,
    EMAIL_ERROR,
    EXPMONTH_ERROR,
    EXPYEAR_ERROR,
    ORDCITY_ERROR,
    ORDNAME_ERROR,
    PAYMETHOD_ERROR,
    PHONENUMBER_ERROR,
    POSTALCODE_ERROR,
    USERNAME_ERROR,
)

logger = logging.getLogger("logger")

PRINT_PREFIX = "[fund-my-watcard]"


def report_error(msg):
    logger.error(msg)
    exit(1)


def report_message(msg):
    logger.info(msg)


def report_warning(msg):
    logger.warning(msg)


def report_success(msg):
    logger.success(msg)


def report_fail(msg):
    logger.error(msg)


def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    Args:
        question: a string that is presented to the user.
        default: the presumed answer if the user just hits <Enter>. It must be "yes" (the default),
        "no" or None (meaning an answer is required of the user).

    Returns:
        True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True, "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        report_warning(question + prompt)
        choice = input().lower()
        if default is not None and choice == "":
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            report_warning("Please respond with 'yes' or 'no' (or 'y' or 'n').")


def input_and_encrypt_password():
    return encrypt_password(getpass.getpass(PRINT_PREFIX + " Please input your password: ").encode())


def encrypt_password(password):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=b"x\xe6}\xb5\r+\xbf\xa2\x10+\xed\x94Q\xc2\x14+",
        iterations=100000,
        backend=default_backend(),
    )
    return base64.urlsafe_b64encode(kdf.derive(password))


def sum_digits(digit):
    if digit < 10:
        return digit
    else:
        ans = (digit % 10) + (digit // 10)
        return ans


def valid_card_number(number):
    num = [int(i) for i in number[::-1]]
    doubled_digit_list = list()
    digits = list(enumerate(num, start=1))

    for index, digit in digits:
        if index % 2 == 0:
            doubled_digit_list.append(digit * 2)
        else:
            doubled_digit_list.append(digit)

    doubled_digit_list = [sum_digits(x) for x in doubled_digit_list]
    sum_of_digits = sum(doubled_digit_list)

    return sum_of_digits % 10 == 0


def check_user_name(user_name):
    if not re.fullmatch(r"[0-9a-z]+", user_name):
        report_error(USERNAME_ERROR)


def check_ord_name(ord_name):
    if not re.fullmatch(r"[a-zA-Z\s]+", ord_name):
        report_error(ORDNAME_ERROR)


def check_phone_number(phone_number):
    if not re.fullmatch(r"(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}", phone_number):
        report_error(PHONENUMBER_ERROR)


def check_ord_postal_code(ord_postal_code):
    if not re.fullmatch(r"^(?!.*[DFIOQU])[A-VXY][0-9][A-Z] ?[0-9][A-Z][0-9]$", ord_postal_code):
        report_error(POSTALCODE_ERROR)


def check_ord_city(ord_city):
    if not re.fullmatch(r"[a-zA-Z]+", ord_city):
        report_error(ORDCITY_ERROR)


def check_email_address(email_address):
    if not re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email_address):
        report_error(EMAIL_ERROR)


def check_payment_method(payment_method):
    if payment_method != "CC":
        report_error(PAYMETHOD_ERROR)


def check_trn_card_owner(trn_card_owner):
    if not re.fullmatch(r"[a-zA-Z\s]+", trn_card_owner):
        report_error(CARDOWNER_ERROR)


def check_trn_card_type(trn_card_type):
    from .mywatcard import card_type

    if trn_card_type not in card_type:
        report_error(CARDTYPE_ERROR)


def check_trn_card_number(trn_card_number):
    if not valid_card_number(trn_card_number.replace(" ", "")):
        report_error(CARDNUMBER_ERROR)


def check_trn_exp_month(trn_exp_month):
    if not re.fullmatch(r"0[1-9]|1[0-2]", trn_exp_month):
        report_error(EXPMONTH_ERROR)


def check_trn_exp_year(trn_exp_year):
    if not re.fullmatch(r"[0-9][0-9]", trn_exp_year):
        report_error(EXPYEAR_ERROR)


def check_trn_card_cvd(trn_card_cvd):
    if not re.fullmatch(r"[0-9]{3,4}", trn_card_cvd):
        report_error(CVD_ERROR)
