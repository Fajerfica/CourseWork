from django.http import FileResponse
from django.shortcuts import render
from .models import Algos, Problems, Output

from .forms import SelectAlgosForm, SelectProblemsForm

def index(request):
    return render(request, 'main/index.html')

output = Output()


def testing(request):
        algos = SelectAlgosForm()
        problems = SelectProblemsForm()

        return render(request, 'main/testing.html', {'algos': algos, 'problems':problems})


def result(request):
    if request.method == 'POST':
        algos = SelectAlgosForm(request.POST)
        problems = SelectProblemsForm(request.POST)
        if algos.is_valid() and problems.is_valid():
            algos_select = algos.cleaned_data.get('algos', [])
            problems_select = problems.cleaned_data.get('problems', [])
            output.output(problems_select, algos_select)

    site_output = output.get_output()
#    picture = output.return_graph()
    return render(request, 'main/result.html',
                  {'graph_path': site_output['graph_path'], 'output': site_output})


def graph(request):
    file_id = request.GET['file']
    img = open(file_id, 'rb')
    response = FileResponse(img)

    return response