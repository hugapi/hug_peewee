"""Tests hug_peewee's connection related features"""
import hug
import pytest
from peewee import SqliteDatabase

import hug_peewee

api = hug.API(__name__)


def test_manage():
    """Test to ensure telling hug_peewee to manage connections works as expected"""
    assert isinstance(hug_peewee.connection.manage(api), SqliteDatabase)
    assert isinstance(hug_peewee.connection.manage(api, location='here'), SqliteDatabase)
