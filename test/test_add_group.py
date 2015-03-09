# -*- coding: utf-8 -*-
import pytest
from model.group import GroupNew
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_(app):
    app.session.log_in(username="admin", password="secret")
    app.creation_group(GroupNew(name="new3", header="new3", footer="new3"))
    app.session.log_out()


def test_add_emp_group(app):
    app.session.log_in(username="admin", password="secret")
    app.creation_group(GroupNew(name="", header="", footer=""))
    app.session.log_out()
