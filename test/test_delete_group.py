__author__ = 'vlovets'
from model.group import GroupNew


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.creation(GroupNew(name="new"))
    app.group.delete_first_group()

