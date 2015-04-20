__author__ = 'vlovets'
from model.group import GroupNew
from random import randrange
import random

def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.creation(GroupNew(name="new group for delete"))
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    group = GroupNew(name="new group")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    old_groups[index] = group
    if check_ui:
        assert sorted(new_groups, key=GroupNew.id_or_max) == sorted(app.group.get_group_list(), key=GroupNew.id_or_max)
    len(old_groups) == len(new_groups)
