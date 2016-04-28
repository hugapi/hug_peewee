hug_peewee
===================

[![PyPI version](https://badge.fury.io/py/hug_peewee.svg)](http://badge.fury.io/py/hug_peewee)
[![Build Status](https://travis-ci.org/timothycrosley/hug_peewee.svg?branch=master)](https://travis-ci.org/timothycrosley/hug_peewee)
[![Coverage Status](https://coveralls.io/repos/timothycrosley/hug_peewee/badge.svg?branch=master&service=github)](https://coveralls.io/github/timothycrosley/hug_peewee?branch=master)
[![License](https://img.shields.io/github/license/mashape/apistatus.svg)](https://pypi.python.org/pypi/hug_peewee/)
[![Join the chat at https://gitter.im/timothycrosley/hug_peewee](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/timothycrosley/hug_peewee?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

An extension to hug that adds clean integration with the peewee ORM:

```py
import hug_peewee

db = hug_peewee.connection.manage(__name__, 'sqlite', 'my.db')
```

Works with hug 2.1.0 or greater.

Installing hug_peewee
===================

Installing hug_peewee is as simple as:

```bash
pip3 install hug_peewee --upgrade
```

Ideally, within a virtual environment.


What is hug_peewee?
===================

An extension to hug that adds clean integration with the peewee ORM

--------------------------------------------

Thanks and I hope you find hug_peewee helpful!

~Timothy Crosley
