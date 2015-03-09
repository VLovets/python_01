__author__ = 'vlovets'


def test_delete_first_group(app):
    app.session.log_in(username="admin", password="secret")
    app.group.delete_first_group()
    app.session.log_out()
