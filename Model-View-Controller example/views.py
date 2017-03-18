from pyramid.response import Response
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from gluon import SQLFORM
from wrapper import wrapper
from models import Models

wrapper.debug = True
wrapper.response = Response
wrapper.redirect = lambda status,url: HTTPFound(location=url)

db = Models().db()


@view_config(route_name='index')
@wrapper(view='templates/index.html',dbs=[db])
def index(context, request):
    vars = wrapper.extract_vars(request.POST)
    form = SQLFORM(db.person)
    if form.accepts(vars):
        message = 'Hello %s' % form.vars.name
        db.commit()
    else:
        message = 'Hello anonymous'
    people = db(db.person).select()
    return locals()

