"""Defines how connections with databases via peewee will be handled"""
import hug
from peewee import MySQLDatabase, PostgresqlDatabase, SqliteDatabase, Model
from playhouse.berkeleydb import BerkeleyDatabase
from playhouse.shortcuts import model_to_dict

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
            engine_instance.close()

    class DatabaseModel(Model):
        class Meta:
            database = engine_instance

        def __native_types__(self):
            return model_to_dict(self)

        @classmethod
        def row(cls, primary_key='id'):
            def get_item(id):
                if isinstance(id, cls):
                    return id

                return cls.get(getattr(cls, primary_key)==id)
            get_item.__doc__ = 'A {} retrieved based on unique {}'.format(cls.__name__, primary_key)
            return get_item

    engine_instance.Model = DatabaseModel
    return engine_instance
