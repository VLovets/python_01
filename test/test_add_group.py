# -*- coding: utf-8 -*-
from model.group import GroupNew


def test_(app):
    app.group.creation(GroupNew(name="new", header="new3", footer="new3"))


def test_add_emp_group(app):
    app.group.creation(GroupNew(name="", header="", footer=""))

