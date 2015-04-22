__author__ = 'vlovets'
from model.contact import Contact
from model.group import GroupNew
import random
from fixture.orm import ORMFixture


def test_add_contact_to_group(app):
    db = ORMFixture(host='127.0.0.1', name='addressbook', user='root', password='')
    group_name = 'new group for contact'
    if len(db.check_group_in_list(GroupNew(name=group_name))) == 0:
        app.group.creation(GroupNew(name=group_name))
    cig_old = db.get_contacts_in_group(GroupNew(name=group_name))
    if len(db.get_contacts_not_in_group(GroupNew(name=group_name))) == 0:
        app.contact.create(Contact(firstname='new contact for add to group', lastname='lastname'))
    old_contacts = db.get_contacts_not_in_group(GroupNew(name=group_name))
    contact = random.choice(old_contacts)
    app.contact.open_home_page()
    app.contact.select_contact_by_id_for_group(contact.id)
    if len(db.get_group_list()) == 1:
        app.contact.click_add_to_group()
    else:
        app.group.get_groups_from_main_page(group_name)
        app.contact.click_add_to_group()
    cig_new = db.get_contacts_in_group(GroupNew(name=group_name))
    assert len(cig_old) + 1 == len(cig_new)
