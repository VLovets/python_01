__author__ = 'vlovets'
from model.group import GroupNew


def test_update_first_group(app):
    app.session.log_in(username="admin", password="secret")
    app.group.test_update_first_group(GroupNew(name="new13", header="new13", footer="new31"))
    app.session.log_out()

