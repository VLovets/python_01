# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + ' '*5
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname='', middlename='', lastname='', nickname='', title='',
                    company='', address='', home='', mobile='', work='', fax='', email2='', email='',
                    email3='', homepage='', address2='', phone2='', notes='')] + [
        Contact(firstname=random_string("fn", 10), middlename=random_string("mn", 10), lastname=random_string("ln", 10),
                nickname=random_string("nn", 10), title=random_string("tt", 10),
                company=random_string("co", 10), address=random_string("ad", 10), home=random_string("hp", 10),
                mobile=random_string("mp", 10), work=random_string("wp", 10), fax=random_string("fp", 10),
                email2=random_string("m2", 10), email=random_string("m1", 10), email3=random_string("m3", 10),
                homepage=random_string("hp", 10), address2=random_string("ad2", 10),
                phone2=random_string("p2", 10), notes=random_string("note", 10))
        for i in range(3)
        ]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
