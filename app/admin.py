from django.contrib import admin
from .models import *

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(CompanyValue)
admin.site.register(CompanyValueIdea)

# Register your models here.
