# fund-my-watcard

This is a convenient tool to fund the watcard. I am too lazy to fund it by hand, so I write this tool.

## requirements

```bash
teachertian@linux ~ » google-chrome --version
Google Chrome 75.0.3770.90 

teachertian@linux ~ » python3 --version
Python 3.6.8

teachertian@linux ~ » pip3 list | grep splinter
splinter                      0.10.0
```

For other versions of chrome, download the corresponding version of chromedriver at [here](http://chromedriver.chromium.org/downloads)

## usage

Edit `config.json` to fill your information.

Run the script in the project directory:

```bash
python3 main.py
```

## TODO

- Run in docker
- Check the balance automatically
- More robust
