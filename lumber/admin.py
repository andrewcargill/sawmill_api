from django.contrib import admin
from .models import Test, Tree, Log, Plank, MoistureCheck

admin.site.register(Test)
admin.site.register(Tree)
admin.site.register(Log)
admin.site.register(Plank)
admin.site.register(MoistureCheck)

