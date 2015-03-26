# -*- coding: utf-8 -*-
from model.group import GroupNew


def test_(app):
    old_groups = app.group.get_group_list()
    group = GroupNew(name="new", header="new3", footer="new3")
    app.group.creation(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=GroupNew.id_or_max) == sorted(new_groups, key=GroupNew.id_or_max)


#def test_add_emp_group(app):
#    old_groups = app.group.get_group_list()
#    group = GroupNew(name="", header="", footer="")
#    app.group.creation(group)
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) + 1 == len(new_groups)
#    old_groups.append(group)
#    assert sorted(old_groups, key=GroupNew.id_or_max) == sorted(new_groups, key=GroupNew.id_or_max)

