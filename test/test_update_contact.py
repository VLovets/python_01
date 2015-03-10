__author__ = 'vlovets'

from model.contact import Contact


def test_edit_contact(app):
    app.session.log_in(username="admin", password="secret")
    app.contact.edit(Contact("second", "second", "second", "second", "second", "second", "second", "00000",
                            "0000000", "000000", "0000000", "email2@company.com",
                            "first.lastmiddle@company.com", "email3@company.com", "http://homepage.com", "addressS",
                            "homeS", "notes"))
    app.session.log_out()