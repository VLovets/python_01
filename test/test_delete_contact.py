__author__ = 'vlovets'
from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='new contact for del'))
    app.contact.delete_first_contact()
