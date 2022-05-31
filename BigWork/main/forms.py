from django.forms import ModelForm, ModelChoiceField, CharField, ModelMultipleChoiceField, Form, FloatField, IntegerField
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
    min_iters = IntegerField(min_value=1)
    max_iters = IntegerField(min_value=1)
    lam = FloatField()
    # x_axis_type = IntegerField(min_value=1, max_value=2)
    # y_axis_type = IntegerField(min_value=1, max_value=4)

    required_css_class = 'field'

# class SetProblemForm(Form):
#     min_iters = IntegerField(min_value=1)
#     max_iters = IntegerField(min_value=1)
#     lam = FloatField()
