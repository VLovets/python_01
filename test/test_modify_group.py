__author__ = 'vlovets'

from model.group import GroupNew


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.creation(GroupNew(name="new group for update1"))
    old_groups = app.group.get_group_list()
    group = GroupNew(name="new group")
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=GroupNew.id_or_max) == sorted(new_groups, key=GroupNew.id_or_max)


#def test_modify_group_header(app):
#    if app.group.count() == 0:
#        app.group.creation(GroupNew(name="new group for update2"))
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(GroupNew(header="new header"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)


#def test_modify_group_footer(app):
#    if app.group.count() == 0:
#        app.group.creation(GroupNew(name="new group for update3"))
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(GroupNew(footer="new footer"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
