__author__ = 'vlovets'
from model.group import GroupNew


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.creation(GroupNew(name="new group for delete"))
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[0:1] = []
    assert old_groups == new_groups

