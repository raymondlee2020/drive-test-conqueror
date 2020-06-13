from django.contrib import admin

# Register your models here.
from restapi.models import RuleTrueFalse
from restapi.models import RuleMultipleChoice

admin.site.register(RuleTrueFalse)
admin.site.register(RuleMultipleChoice)