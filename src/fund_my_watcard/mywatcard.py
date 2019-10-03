import time

from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

from .util import report_fail

card_type = {"VI": "VISA", "PV": "VISA Debit", "MC": "MasterCard", "MD": "Debit MasterCard", "AM": "AMEX"}


class MyWatCard:
    def __init__(self, **kwargs):
        self.userName = kwargs["userName"]
        self.password = kwargs["password"]
        self.ordName = kwargs["ordName"]
        self.phoneNumber = kwargs["phoneNumber"]
        self.ordAddress1 = kwargs["address1"]
        self.ordAddress2 = None if len(kwargs["address2"]) == 0 else kwargs["address2"]
        self.ordCity = kwargs["ordCity"]
        self.ordProvince = "Ontario" if "ordProvince" not in kwargs else kwargs["ordProvince"]
        self.ordCountry = "Canada" if "ordCountry" not in kwargs else kwargs["ordCountry"]
        self.ordPostalCode = kwargs["ordPostalCode"]
        self.ordEmailAddress = kwargs["ordEmailAddress"]
        self.paymentMethod = kwargs["paymentMethod"]
        self.trnCardOwner = kwargs["trnCardOwner"]
        self.trnCardType = kwargs["trnCardType"]
        self.trnCardNumber = kwargs["trnCardNumber"]
        self.trnExpMonth = kwargs["trnExpMonth"]
        self.trnExpYear = kwargs["trnExpYear"]
        self.trnCardCvd = kwargs["trnCardCvd"]
        self.trnAmount = 0

    def add_fund(self, amount):
        try:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--incognito")
            with Browser(
                "chrome", **{"executable_path": ChromeDriverManager().install()}, options=chrome_options
            ) as browser:
                browser.visit("https://watcard.uwaterloo.ca/OneWebUW/addfunds_watiam.asp")
                browser.fill("UserName", self.userName)
                browser.fill("Password", self.password)
                button = browser.find_by_name("submit")
                button.click()
                time.sleep(2)

                browser.fill("ordName", self.ordName)
                browser.fill("ordPhoneNumber", self.phoneNumber)
                browser.fill("ordAddress1", self.ordAddress1)
                if self.ordAddress2 is not None:
                    browser.fill("ordAddress2", self.ordAddress2)
                browser.fill("ordCity", self.ordCity)
                browser.fill("ordPostalCode", self.ordPostalCode)
                browser.fill("ordEmailAddress", self.ordEmailAddress)
                browser.fill("trnAmount", str(amount))
                browser.find_by_name("paymentMethod").first.select(self.paymentMethod)
                browser.fill("trnCardOwner", self.trnCardOwner)
                browser.find_option_by_text(card_type[self.trnCardType]).first.click()
                browser.fill("trnCardNumber", self.trnCardNumber)
                browser.find_by_name("trnExpMonth").first.select(self.trnExpMonth)
                browser.find_by_name("trnExpYear").first.select(self.trnExpYear)
                browser.fill("trnCardCvd", self.trnCardCvd)
                browser.find_option_by_text(self.ordCountry).first.click()
                browser.find_option_by_text(self.ordProvince).first.click()
                button = browser.find_by_name("submitButton")
                button.click()
                if browser.find_by_text("Funds were added to your card.").first is not None:
                    return True
        except Exception as e:
            report_fail(str(e))
            return False

    def check_balance(self):
        pass
