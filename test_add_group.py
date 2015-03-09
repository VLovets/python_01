# -*- coding: utf-8 -*-
import pytest
from group import GroupNew
from application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_(app):
    app.log_in(username="admin", password="secret")
    app.creation_group(GroupNew(name="new3", header="new3", footer="new3"))
    app.log_out()


def test_add_emp_group(app):
    app.log_in(username="admin", password="secret")
    app.creation_group(GroupNew(name="", header="", footer=""))
    app.log_out()
