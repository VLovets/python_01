# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import pytest
from contact import Contact
from application_contact import Application_contact

@pytest.fixture
def appc(request):
    fixture = Application_contact()
    request.addfinalazer(fixture.destroy)
    return fixture


def test_add_contact(appc):
    appc.log_in(username="admin", password="secret")
    appc.create_contact(Contact("First", "Middle", "Last", "Nickname", "Title", "Company", "Address", "1234567890",
                            "1234567891", "1234567892", "1234567893", "email2@company.com",
                            "first.lastmiddle@company.com", "email3@company.com", "http://homepage.com", "addressS",
                            "homeS", "notes"))
    appc.log_out()


def test_add_empty_contact(appc):
    appc.log_in(username="admin", password="secret")
    appc.create_contact(Contact("", "", "", "", "", "", "", "", "", "", "", "",
                            "", "", "", "", "", ""))
    appc.log_out()
