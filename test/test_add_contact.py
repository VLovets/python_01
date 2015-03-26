# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="First", middlename="Midle", lastname="Last", nickname="Nick", title="Title", company="Company", address="Address", home="Home", mobile="Mobile", work="Work", fax="Fax", email2="Mail2", email="Mail", email3="Mail3", homepage="Homepage", address2="Address2", phone2="Phone2", notes="Notes")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

#def test_add_empty_contact(app):
#    old_contacts = app.contact.get_contact_list()
#    app.contact.create(Contact(firstname='', middlename='', lastname='', nickname='', title='', company='', address='', home='', mobile='', work='', fax='', email2='', email='', email3='', homepage='', address2='', phone2='', notes=''))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) + 1 == len(new_contacts)
