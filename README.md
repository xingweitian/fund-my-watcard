# fund-my-watcard

![PyPI](https://img.shields.io/pypi/v/fund-my-watcard.svg) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/fund-my-watcard.svg)

This is a convenient tool to fund your WatCard easily. I am too lazy to do it by my hand everytime, so I write this tool.

For now, it is only tested in __Ubuntu18.04__ with __Python3.6__.

## install package

```bash
pip install fund-my-watcard
```

## usage

First, set the path to your chromedriver as environment variable:

```bash
export CHROMEDRIVER="/path/to/chromedriver"
```

Check if the path of chromedriver is correct:

```bash
env | grep CHROMEDRIVER
```

Find and download the corresponding versions of your chrome at [here](http://chromedriver.chromium.org/downloads)

Then, try the following commands:

```bash
# see the help of watcard
watcard --help

# gengerate the config file
watcard --config

# fund your WatCard with $10
watcard --fund 10
```

## plan

- Tests
- Check the balance and fund automatically
- More robust
