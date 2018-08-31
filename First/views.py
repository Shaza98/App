from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1> Go to http://127.0.0.1:8000/admin/First/person/add/ to insert a new person in the database ")