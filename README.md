# fund-my-watcard

[![Build Status](https://travis-ci.org/xingweitian/fund-my-watcard.svg?branch=master)](https://travis-ci.org/xingweitian/fund-my-watcard)
[![PyPI](https://img.shields.io/pypi/v/fund-my-watcard.svg)](https://pypi.org/project/fund-my-watcard)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/fund-my-watcard.svg)](https://pypi.org/project/fund-my-watcard)

This is a convenient tool to fund your WatCard easily. I am too lazy to do it by my hand everytime, so I write this tool.

## installation

```bash
pip install fund-my-watcard
```

## usage

```bash
teachertian@v1040-wn-rt-c-83-249 ~/PycharmProjects/fundmywatcard ±dev⚡ » watcard
usage: watcard [-h] [-c | -f FUND | -v]

Fund my WatCard: A tool to fund WatCard easily.

optional arguments:
  -h, --help            show this help message and exit
  -c, --config          generate the config file
  -f FUND, --fund FUND  the fund amount to the WatCard
  -v, --version         show the version of fund-my-watcard

```

## contributing

Please install `dev-requirements.txt` instead of `requirements.txt`, after that, run `dev-init.sh` to install the pre-commit hook to force PEP8 style checking.

## plan

- Tests
- Check the balance and fund automatically
- More robust
