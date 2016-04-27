import peewee
from peewee import *

def connect(database='SqliteDatabse', location=':memory:', **settings):
    try:
        database_class = load_class(database_config)
        assert issubclass(database_class, database)
    except ImportError:
        raise RuntimeError('Unable to import: "{}"'.format(database))
    except AttributeError:
        raise RuntimeError('Database engine not found: "{}"'.format(database))
    except AssertionError:
        raise ValueError('Database engine not a subclass of peewee.Database: "{}"'.format(database))

    return database_class(location, **settings)
