# fund-my-watcard

[![Build Status](https://travis-ci.org/xingweitian/fund-my-watcard.svg?branch=master)](https://travis-ci.org/xingweitian/fund-my-watcard)
[![PyPI](https://img.shields.io/pypi/v/fund-my-watcard.svg)](https://pypi.org/project/fund-my-watcard)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/fund-my-watcard.svg)](https://pypi.org/project/fund-my-watcard)

This is a convenient tool to fund your WatCard easily. I am too lazy to do it by my hand everytime, so I write this tool.

## Installation

```bash
pip3 install fund-my-watcard
```

## Usage

```bash
teachertian@v1040-wn-rt-c-83-249 ~/PycharmProjects/fundmywatcard: watcard
usage: watcard [-h] [-c | -f FUND | -v]

Fund my WatCard: A tool to fund WatCard easily.

optional arguments:
  -h, --help            show this help message and exit
  -c, --config          generate the config file
  -f FUND, --fund FUND  the fund amount to the WatCard
  -v, --version         show the version of fund-my-watcard

```

An example of **.watcard_config**:

```python
{
  "userName": "s123zhang", // User name of WatIM
  "password": "1234567", // Password of WatIM
  "ordName": "San Zhang", // Full name
  "phoneNumber": "123 456 7890", // Phone number
  "address1": "123 Queen Street West", // Home address 1
  "address2": "", // Home address 2
  "ordPostalCode": "A1B2C3", // Postal code
  "ordCity": "Waterloo", // City
  "ordEmailAddress": "zhangsan@gmail.com", // Email address
  "paymentMethod": "CC", // Payment method
  "trnCardOwner": "San Zhang", // Name on the card
  "trnCardType": "MC", // Card type
  "trnCardNumber": "1234567890123456", // Card number
  "trnExpMonth": "01", // Expire month on the card
  "trnExpYear": "25", // Expire year on the card
  "trnCardCvd": "123" // Three digital numbers on the back of card
}
```

Payment Method should be "CC" (Credit Card). Do not support **Interac Online**.

Card Type can be "MC" (Mastercard), "VI" (Visa), "PV" (VISA Debit), "MD" (Debit Mastercard) or "AM" (AMEX).

## Contributing

Please install `dev-requirements.txt` instead of `requirements.txt`. After that, run `dev-init.sh` to install the pre-commit hook to force PEP8 style checking.

## Plan

- Tests
- Docker
- Check the balance and fund automatically
- More robust
