from django.shortcuts import render
from .models import Algos, Problems, Output

from .forms import SelectAlgosForm, SelectProblemsForm

def index(request):
    return render(request, 'main/index.html')

output = Output()


def testing(request):
        if request.method == 'POST':
            algos = SelectAlgosForm(request.POST)
            problems = SelectProblemsForm(request.POST)
            if algos.is_valid() and problems.is_valid():
                algos_select = algos.cleaned_data.get('algos', None)
                problems_select = problems.cleaned_data
                output.output(problems_select, algos_select)
                return render(request, 'main/result.html')
        else:
            algos = SelectAlgosForm()
            problems = SelectProblemsForm()

        return render(request, 'main/testing.html', {'algos': algos, 'problems':problems})


def result(request):
    site_output = output.get_output()
    picture = output.return_graph()
    return render(request, 'main/result.html',
                  {'picture': picture, 'output': site_output, 'output_1': dicts})
