# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname="First", middlename="Midle", lastname="Last", nickname="Nick", title="Title", company="Company", address="Address", home="Home", mobile="Mobile", work="Work", fax="Fax", email2="Mail2", email="Mail", email3="Mail3", homepage="Homepage", address2="Address2", phone2="Phone2", notes="Notes"))


def test_add_empty_contact(app):
   app.contact.create(Contact(firstname='', middlename='', lastname='', nickname='', title='', company='', address='', home='', mobile='', work='', fax='', email2='', email='', email3='', homepage='', address2='', phone2='', notes=''))

