__author__ = 'vlovets'

from model.contact import Contact


def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='new contact for edit'))
    app.contact.edit(Contact(firstname="Second", middlename="Second1"))
