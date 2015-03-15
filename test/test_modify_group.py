__author__ = 'vlovets'

from model.group import GroupNew


def test_modify_group_name(app):
    app.group.modify_first_group(GroupNew(name="new group"))



def test_modify_group_header(app):
    app.group.modify_first_group(GroupNew(header="new header"))



def test_modify_group_footer(app):
    app.group.modify_first_group(GroupNew(footer="new footer"))
