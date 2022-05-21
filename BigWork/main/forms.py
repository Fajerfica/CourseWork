from django.forms import ModelForm, ModelChoiceField, CharField, ModelMultipleChoiceField, Form, FloatField
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

class SetAlgosParamsForm(Form):
    # x0x = FloatField()
    # x0y = FloatField()
    eps = FloatField()
    min_iters = FloatField()
    max_iters = FloatField()
    lam = FloatField()
