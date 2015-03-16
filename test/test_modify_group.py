__author__ = 'vlovets'

from model.group import GroupNew


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.creation(GroupNew(name="new group for update1"))
    app.group.modify_first_group(GroupNew(name="new group"))


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.creation(GroupNew(name="new group for update2"))
    app.group.modify_first_group(GroupNew(header="new header"))


def test_modify_group_footer(app):
    if app.group.count() == 0:
        app.group.creation(GroupNew(name="new group for update3"))
    app.group.modify_first_group(GroupNew(footer="new footer"))
