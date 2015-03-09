# -*- coding: utf-8 -*-
from model.group import GroupNew


def test_(app):
    app.session.log_in(username="admin", password="secret")
    app.group.creation(GroupNew(name="new3", header="new3", footer="new3"))
    app.session.log_out()


def test_add_emp_group(app):
    app.session.log_in(username="admin", password="secret")
    app.group.creation(GroupNew(name="", header="", footer=""))
    app.session.log_out()
