from django.contrib import admin

# Register your models here.
#from import_export import resources
from .models import Person


admin.site.register(Person)


# class PersonResource(resources.ModelResource):
#     class Meta:
#         model = Person
        
