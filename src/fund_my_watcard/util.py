import base64

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

PRINT_PREFIX = "[fund-my-watcard] "


def report_error(msg: str):
    print(PRINT_PREFIX + msg)
    exit(1)


def report_message(msg: str):
    print(PRINT_PREFIX + msg)


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
        print(question + prompt)
        choice = input().lower()
        if default is not None and choice == "":
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            print("Please respond with 'yes' or 'no' (or 'y' or 'n').\n")


def input_and_encrypt_password():
    return encrypt_password(input(PRINT_PREFIX + "Please input your password: ").encode())


def encrypt_password(password):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=b"x\xe6}\xb5\r+\xbf\xa2\x10+\xed\x94Q\xc2\x14+",
        iterations=100000,
        backend=default_backend(),
    )
    return base64.urlsafe_b64encode(kdf.derive(password))
