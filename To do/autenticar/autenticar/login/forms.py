from django.forms import ModelForm
from .models import Grupos, Tarefa, Tags, Sub_Grupos

class GruposForm(ModelForm):
    class Meta:
        model = Grupos
        fields = '__all__'

class Sub_GruposForm(ModelForm):
    class Meta:
        model = Sub_Grupos
        fields = '__all__'

class TarefasForm(ModelForm):
    class Meta:
        model = Tarefa
        fields = '__all__'

class TagsForm(ModelForm):
    class Meta:
        model = Tags
        fields = '__all__'