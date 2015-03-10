# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.log_in(username="admin", password="secret")
    app.contact.create(Contact("First", "Middle", "Last", "Nickname", "Title", "Company", "Address", "1234567890",
                            "1234567891", "1234567892", "1234567893", "email2@company.com",
                            "first.lastmiddle@company.com", "email3@company.com", "http://homepage.com", "addressS",
                            "homeS", "notes"))
    app.session.log_out()


def test_add_empty_contact(app):
    app.session.log_in(username="admin", password="secret")
    app.contact.create(Contact("", "", "", "", "", "", "", "", "", "", "", "",
                            "", "", "", "", "", ""))
    app.session.log_out()
