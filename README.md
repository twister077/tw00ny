## About tw00ny
A new port of Web2py 2.14.6 to Pyramid, wsgiref and other frameworks (based on mdipierro/gluino)

Port of web2py libraries to Pyramid with an example.

This semi fork from mdipierro/gluino is a succesfull attempt to upgraded the Gluino libraries to Web2py 2.14.6 (Gluino later became known as Web2y).

The reason why I decided to semi upgrade gluino is Web2py was not updated for almost a year now since writing this. So I decided to upgrade to an active Python Web Frameworks such as Pyramid, which I really like. But there was one downsize. I didn't like templating libraries like jinja2 or chameleon. Web2py has a realy thoughtout templating system. Easy to use and similar to jinja2 and chameleon. By working on gluino/tw00ny I could easing step over to Pyramid, without recoding al my templates and databaseconnections.

Author: Massimo Di Pierro
Edited and upgraded by: Jefta Harlingen
Based on mdipierro/gluino

License: Web2py license (LGPL) applies to files in gluon/ folder

On PyPI: http://pypi.python.org/pypi/Gluon

The port includes;
* Database Abstraction Layer (dal.py) documentation
* Template language (template.py) documentation
* FORMs (form,py) documentation
* SQLFORMs (sqlhtml.py) documentation
* validators (validators.py) documentation
* widgets documentation
* cache (cache.py) documentation

### Examples

* pyramid_example.py

All the examples include the same common code:
```
db=DAL('sqlite://storage.sqlite')
db.define_table('person',Field('name',requires=IS_NOT_EMPTY()))

...
form = SQLFORM(db.person)
if form.accepts(vars):
    message = 'hello %s' % form.vars.name
else:
    message = 'hello anonymous'
people = db(db.person).select()
return locals()
```

and execute the same template:

```
{{extend 'templates/layout.html'}}
<h1>{{=message}}</h1>
{{=form}}
<h2>People</h2>
{{=people}}
<h2>A static image</h2>
<img src="/static/cat.jpg" />
```

Databases supported:
* SQLite	sqlite3 or pysqlite2 or zxJDBC [zxjdbc] (on Jython)
* PostgreSQL	psycopg2 [psycopg2] or pg8000 [pg8000] or zxJDBC [zxjdbc] (on Jython)* 
* MySQL	pymysql [pymysql] or MySQLdb [mysqldb]
* Oracle	cx_Oracle [cxoracle]
* MSSQL	pyodbc [pyodbc] or pypyodbc[pypyodbc]
* FireBird	kinterbasdb [kinterbasdb] or fdb or pyodbc
* DB2	pyodbc [pyodbc]
* Informix	informixdb [informixdb]
* Ingres	ingresdbi [ingresdbi]
* Cubrid	cubriddb [cubridb] [cubridb]
* Sybase	Sybase [Sybase]
* Teradata	pyodbc [Teradata]
* SAPDB	sapdb [SAPDB]
* MongoDB	pymongo [pymongo]
* IMAP	imaplib [IMAP]
