"""Tests hug_peewee's connection related features"""
import hug
import pytest
from peewee import SqliteDatabase

import hug_peewee

api = hug.API(__name__)


@hug.get()
def fake_endpoint():
    return True


def test_manage():
    """Test to ensure telling hug_peewee to manage connections works as expected"""
    assert isinstance(hug_peewee.connection.manage(api), SqliteDatabase)
    assert isinstance(hug_peewee.connection.manage(api, location='connection_testing.db'), SqliteDatabase)
    assert hug.test.get(api, 'fake_endpoint').data == True

