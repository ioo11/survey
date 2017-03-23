from django.contrib import admin

# Register your models here.

from .models import Test, Question, RadioAnswer, SetAnswer

admin.site.register(Test)
admin.site.register(Question)
admin.site.register(SetAnswer)
admin.site.register(RadioAnswer)