__author__ = 'vlovets'


def test_delete_first_contact(app):
    app.session.log_in(username="admin", password="secret")
    app.contact.delete_first_contact()
    app.session.log_out()
