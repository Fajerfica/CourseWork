from django.forms import ModelForm, ModelChoiceField, CharField, ModelMultipleChoiceField
from .models import Algos, Problems

class SelectAlgosForm(ModelForm):
    algos = ModelMultipleChoiceField(Algos.objects.all(), required=True, label=False)

    algos.widget.attrs.update({'size': '3'})

    class Meta:
        model = Algos
        fields = ['algos']

class SelectProblemsForm(ModelForm):
    problems = ModelChoiceField(queryset=Problems.objects.all(), required=True, label=False, empty_label='')
    problems.widget.attrs.update({'size': '3'})
    class Meta:
        model = Problems
        fields = ['problems']
