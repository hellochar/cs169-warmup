# Create your views here.
from loginapp.models import UsersModel
from django.utils import simplejson
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

@csrf_exempt
@require_POST
def login(request):
    json = simplejson.loads(request.raw_post_data)
    user = json['user']
    password = json['password']
    login_result = UsersModel.login(user, password)
    if login_result >= 1:
        json = { 'errCode' : 1, 'count' : login_result }
    else:
        json = { 'errCode' : login_result }
    return HttpResponse(simplejson.dumps(json), content_type="application/json")

@csrf_exempt
@require_POST
def add(request):
    json = simplejson.loads(request.raw_post_data)
    # import code
    # code.interact(local=locals())
    user = json['user']
    password = json['password']
    add_result = UsersModel.add(user, password)
    if add_result >= 1:
        json = { 'errCode' : 1, 'count' : add_result }
    else:
        json = { 'errCode' : add_result }
    return HttpResponse(simplejson.dumps(json), content_type="application/json")

@csrf_exempt
@require_POST
def resetFixture(request):
    UsersModel.TESTAPI_resetFixture()
    return HttpResponse(simplejson.dumps({'errCode' : 1}), content_type="application/json")

@csrf_exempt
@require_POST
def unitTests(request):
    import unittest
    from loginapp.tests import SimpleTest

    test_suite = unittest.TestLoader().loadTestsFromTestCase(SimpleTest)
    results = test_suite.run(unittest.TestResult())

    json = {'totalTests' : results.testsRun,
            'nrFailed' : len(results.errors) + len(results.failures),
            'output' : '\n\n'.join([x[1] for x in results.errors + results.failures]),
            }
    
    return HttpResponse(simplejson.dumps(json), content_type="application/json")
