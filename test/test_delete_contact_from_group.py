__author__ = 'vlovets'
from model.contact import Contact
from model.group import GroupNew
import random
from fixture.orm import ORMFixture


def test_delete_contact_from_group(app, db):
    dbc = ORMFixture(host='127.0.0.1', name='addressbook', user='root', password='')
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname='new contact for add to company'))
    if len(db.get_group_list()) == 0:
        app.group.creation(GroupNew(name="new group for contact"))
    if len(db.get_contacts_in_group()) == 0:
        old_contacts = db.get_contact_list()
        contact = random.choice(old_contacts)
        app.contact.select_contact_by_id_for_group(contact.id)
        if len(db.get_group_list()) == 1:
            app.contact.click_add_to_group()
        else:
            app.contact.select_second_group()
            app.contact.click_add_to_group()
    cig_old = dbc.get_contacts_in_group(GroupNew(id='94'))
    app.contact.display_contact_in_group()
    app.contact.select_first_contact(0)
    app.contact.remove_from_group()
    cig_new = dbc.get_contacts_in_group(GroupNew(id='94'))
    assert len(cig_old) - 1 == len(cig_new)
