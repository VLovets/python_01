__author__ = 'vlovets'
from model.contact import *


def test_compare_bd_ui(app, db):
    l_ui = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    l_bd = sorted(db.get_contact_list(), key=Contact.id_or_max)
    for i in range(len(l_bd)):
        assert l_ui[i].firstname == l_bd[i].firstname.strip()
        assert l_ui[i].lastname == l_bd[i].lastname.strip()
        assert l_ui[i].address == l_bd[i].address.strip()