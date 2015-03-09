# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application_contact import Application_contact

@pytest.fixture
def appc(request):
    fixture = Application_contact()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(appc):
    appc.sessionc.log_in(username="admin", password="secret")
    appc.contact.create(Contact("First", "Middle", "Last", "Nickname", "Title", "Company", "Address", "1234567890",
                            "1234567891", "1234567892", "1234567893", "email2@company.com",
                            "first.lastmiddle@company.com", "email3@company.com", "http://homepage.com", "addressS",
                            "homeS", "notes"))
    appc.sessionc.log_out()


def test_add_empty_contact(appc):
    appc.sessionc.log_in(username="admin", password="secret")
    appc.contact.create(Contact("", "", "", "", "", "", "", "", "", "", "", "",
                            "", "", "", "", "", ""))
    appc.sessionc.log_out()
