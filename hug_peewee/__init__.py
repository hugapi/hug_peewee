"""Defines how the hug_peewee package exposes modules as well as exposes it's version number"""
from hug_peewee._version import current
from hug_peewee.connection import ENGINES
from hug_peewee import connection

__version__ = current
