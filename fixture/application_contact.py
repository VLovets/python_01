__author__ = 'vlovets'
from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.sessionc import SessionHelperC
from fixture.contact import ContactHelper


class Application_contact:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.sessionc = SessionHelperC(self)
        self.contact = ContactHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()