"""Defines how connections with databases via peewee will be handled"""
import hug
from peewee import MySQLDatabase, PostgresqlDatabase, SqliteDatabase
from playhouse.berkeleydb import BerkeleyDatabase

ENGINES = {'sqlite': SqliteDatabase, 'psql': PostgresqlDatabase, 'mysql': MySQLDatabase, 'berkeley': BerkeleyDatabase}


def manage(api, engine='sqlite', location=':memory:', **settings):
    '''Creates a new database object for handling connections based on the specified parameters'''
    if not engine in ENGINES:
        raise ValueError(('{0} is not one of the registered database engines: {1}.'
                         "To add an engine: hug_peewee.ENGINES['{0}'] = Class").format(engine,
                                                                                        ', '.join(ENGINES.keys())))
    engine_instance = ENGINES[engine](location, **settings)
    if location != ':memory:':
        hug_api = hug.API(api)
        @hug.request_middleware(api=hug_api)
        def process_data(request, response):
            engine_instance.connect()

        @hug.response_middleware(api=hug_api)
        def process_data(request, response, resource):
            engine_instance.disconnect()

    return engine_instance
