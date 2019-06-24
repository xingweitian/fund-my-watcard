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

```json
{
  "userName": "s123zhang",
  "password": "1234567",
  "ordName": "San Zhang",
  "phoneNumber": "123 456 7890",
  "address1": "123 Queen Street West",
  "address2": "",
  "ordPostalCode": "A1B2C3",
  "ordCity": "Waterloo",
  "ordEmailAddress": "zhangsan@gmail.com",
  "paymentMethod": "CC",
  "trnCardOwner": "San Zhang",
  "trnCardType": "MC",
  "trnCardNumber": "1234567890123456",
  "trnExpMonth": "01",
  "trnExpYear": "25",
  "trnCardCvd": "123"
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
