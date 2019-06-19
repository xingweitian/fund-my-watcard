# fund-my-watcard

This is a convenient tool to fund the watcard. I am too lazy to fund it by hand, so I write this tool.

## install package

```bash
pip install fund-my-watcard
```

## usage

First, set the path to your chromedriver as environment variable:

```bash
export CHROMEDRIVER="xxx/yyy/zzz/chromedriver"
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

## TODO

- Docker support
- Check the balance automatically
- More robust
