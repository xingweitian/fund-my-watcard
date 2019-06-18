from splinter import Browser
import time
import json

config = dict()

with open("./config.json") as json_file:
    _data = json.load(json_file)
    for k, v in _data.items():
        config[k] = v

executable_path = {'executable_path': './chromedriver'}

with Browser("chrome", **executable_path, incognito=True) as browser:
    browser.visit("https://watcard.uwaterloo.ca/OneWebUW/addfunds_watiam.asp")
    browser.fill("UserName", config["UserName"])
    browser.fill("Password", config["Password"])
    button = browser.find_by_name("submit")
    button.click()
    time.sleep(3)

    browser.fill("ordName", config["Name"])
    browser.fill("ordPhoneNumber", config["PhoneNumber"])
    browser.fill("ordAddress1", config["Address1"])
    browser.fill("ordCity", config["City"])
    browser.fill("ordPostalCode", config["PostalCode"])
    browser.fill("ordEmailAddress", config["EmailAddress"])
    browser.fill("trnAmount", config["Amount"])
    browser.find_by_name("paymentMethod").first.select(config["PaymentMethod"])
    browser.fill("trnCardOwner", config["CardOwner"])
    browser.find_by_name("trnCardType").first.select(config["CardType"])
    browser.fill("trnCardNumber", config["CardNumber"])
    browser.find_by_name("trnExpMonth").first.select(config["ExpMonth"])
    browser.find_by_name("trnExpYear").first.select(config["ExpYear"])
    browser.fill("trnCardCvd", config["CardCvd"])
    button = browser.find_by_name("submitButton")
    button.click()

    if browser.find_by_text("Funds were added to your card.").first is not None:
        print("Add successful.")
