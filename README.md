# fund-my-watcard

This is a convenient tool to fund the watcard. I am too lazy to fund it by hand, so I write this tool.

## requirements

```bash
teachertian@linux ~ » google-chrome --version
Google Chrome 75.0.3770.90 

teachertian@linux ~ » python3 --version
Python 3.6.8

teachertian@linux ~ » pip list                     
Package          Version
---------------- -------
EasyProcess      0.2.7  
pip              10.0.1 
PyVirtualDisplay 0.2.3  
selenium         3.141.0
setuptools       39.1.0 
splinter         0.10.0 
urllib3          1.25.3 
```

For other version of chrome, download the corresponding version chromedriver at [here](http://chromedriver.chromium.org/downloads)

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