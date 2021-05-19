from django.contrib import admin
from .models import Tarefa, Grupos, Tags, Sub_Grupos

admin.site.register(Grupos)
admin.site.register(Sub_Grupos)
admin.site.register(Tarefa)
admin.site.register(Tags)



# Register your models here.
