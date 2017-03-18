## About tw00ny
A new port of the [Web2py](http://www.web2py.com) 2.14.6 libraries to [Pyramid](http://docs.pylonsproject.org/en/latest) (based on [mdipierro/gluino](https://github.com/mdipierro/gluino))

This semi fork from mdipierro/gluino is a succesfull attempt to upgraded the Gluino libraries to Web2py 2.14.6 (Gluino later became known as Web2y) for use with the Pyramid Web Framework.

The reason why I decided to semi upgrade gluino is Web2py was not updated for almost a year now since writing this. So I decided to upgrade to an active Python Web Frameworks such as Pyramid, which I really like. But there was one downsize. Database connections were harder to configure in Pyramid than in Web2py. I also didn't like templating libraries like jinja2 or chameleon. But because Pyramid is versatile I could reuse the templating system of Web2py, which is really nice. Easy to use and similar to jinja2 and chameleon. With minor adjustments you now can reuse your Web2py based python code and enjoy Pyramid.

Author: Massimo Di Pierro

Edited and upgraded by: Jefta Harlingen

Based on mdipierro/gluino

License: Web2py license (LGPL) applies to files in gluon/ folder

On Web2py: http://web2py.com

On Pyramid: http://docs.pylonsproject.org/en/latest

The port includes:
* Database Abstraction Layer (dal.py)
* Template language (template.py)
* FORMs (form.py)
* SQLFORMs (sqlhtml.py)
* validators (validators.py)
* widgets
* cache (cache.py)

All Web2py documentation can be found [here](http://web2py.com/book).

### Examples

* pyramid_example.py (basic example)
* Example/Model-View-Controller (each in their own separate file)


The basic pyramid_example.py example included:
```
db=DAL('sqlite://storage.sqlite')
db.define_table('person',Field('name',requires=IS_NOT_EMPTY()))

...
form = SQLFORM(db.person)
if form.accepts(vars):
    message = 'hello %s' % form.vars.name
    db.commit()
else:
    message = 'hello anonymous'
people = db(db.person).select()
return locals()
```

and execute the same template:

```
{{extend 'templates/layout.html'}}
{{from gluon.html import *}}

<h1>{{=message}}</h1>
{{=form}}
<h2>People</h2>
{{=people}}
<h2>A static image</h2>
{{=IMG(_src=URL('static','cat.jpg'), _alt="Cat")}}
```

which generates the following output on the Pyramid web framework:

![GitHub Logo](/static/screenshot.png)

Databases supported:
* SQLite	sqlite3 or pysqlite2 or zxJDBC (on Jython)
* PostgreSQL	psycopg2 or pg8000 or zxJDBC (on Jython)
* MySQL	pymysql or MySQLdb
* Oracle	cx_Oracle
* MSSQL	pyodbc or pypyodbc
* FireBird	kinterbasdb or fdb or pyodbc
* DB2	pyodbc
* Informix	informixdb
* Ingres	ingresdbi
* Cubrid	cubriddb
* Sybase	Sybase
* Teradata	pyodbc
* SAPDB	sapdb
* MongoDB	pymongo
* IMAP	imaplib

You can also create an executable for production purposes by using [PyInstaller](http://www.pyinstaller.org/). See the [WIKI](https://github.com/twister077/tw00ny/wiki) page for more details and for an example.
