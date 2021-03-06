__author__ = 'vlovets'
from model.group import GroupNew
import random


def test_delete_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.creation(GroupNew(name="new group for delete"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = db.get_group_list()
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=GroupNew.id_or_max) == sorted(app.group.get_group_list(), key=GroupNew.id_or_max)