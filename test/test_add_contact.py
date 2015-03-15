# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact("First", "Middle", "Last", "Nickname", "Title", "Company", "Address", "1234567890",
                            "1234567891", "1234567892", "1234567893", "email2@company.com",
                            "first.lastmiddle@company.com", "email3@company.com", "http://homepage.com", "addressS",
                            "homeS", "notes"))


def test_add_empty_contact(app):
    app.contact.create(Contact("", "", "", "", "", "", "", "", "", "", "", "",
                            "", "", "", "", "", ""))

