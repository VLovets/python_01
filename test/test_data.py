__author__ = 'vlovets'
from random import randrange
import re
from model.contact import Contact


def test_phones_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='new contact for edit'))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    data_from_home_page = app.contact.get_contact_list()[index]
    date_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert data_from_home_page.lastname == date_from_edit_page.lastname
    assert data_from_home_page.firstname == date_from_edit_page.firstname
    assert data_from_home_page.address == date_from_edit_page.address
    assert data_from_home_page.all_mails == merge_mails_like_on_home_page(date_from_edit_page)
    assert data_from_home_page.all_phones_from_homepge == merge_phones_like_on_home_page(date_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_mails_like_on_home_page(contact):
    return '\n'.join(filter(lambda x: x != '',
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))


def merge_phones_like_on_home_page(contact):
    return '\n'.join(filter(lambda x: x != '',
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.mobile, contact.work, contact.phone2]))))
