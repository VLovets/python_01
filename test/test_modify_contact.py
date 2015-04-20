__author__ = 'vlovets'
from model.contact import Contact
from random import randrange


def test_modify_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname='new contact for edit'))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Second", lastname="Second1")
    contact.id = old_contacts[index].id
    app.contact.modify_some_contact(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    len(old_contacts) == len(new_contacts)
