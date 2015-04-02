# -*- coding: utf-8 -*-
from model.group import GroupNew
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + ' '*5
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [GroupNew(name='', header='', footer='')] + [
        GroupNew(name=random_string("n", 10), header=random_string("h", 15), footer=random_string("f", 20))
        for i in range(5)
        #for name in [' ', random_string("n", 10)]
        #for header in [' ', random_string("h", 15)]
        #for footer in [' ', random_string("f", 20)]
        ]

@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.creation(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=GroupNew.id_or_max) == sorted(new_groups, key=GroupNew.id_or_max)

