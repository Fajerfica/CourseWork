from django.http import FileResponse
from django.shortcuts import render
from .models import HistoryRecord, Output

from .forms import SelectAlgosForm, SelectProblemsForm, SetAlgosParamsForm

from datetime import datetime

def index(request):
    return render(request, 'main/index.html')

output = Output()

def testing(request):
        algos = SelectAlgosForm()
        problems = SelectProblemsForm()

        return render(request, 'main/testing.html', {'algos': algos, 'problems':problems})

txt_path = None
graph_path = None

def result(request):

    if request.method == 'POST':
        params = SetAlgosParamsForm(request.POST)
        params_dict = dict()
        if params.is_valid():
            output.algos_params = params.cleaned_data
    # params_dict = {str(el):None for el in output.algos}
    # if request.method == 'POST':
    #     for i in range(len(output.algos)):

    params_dict = output.algos_params
    site_output = output.get_output()
    # global  txt_path, graph_path
    # txt_path = output.txt_path
    # graph_path = output.graph_path


#    picture = output.return_graph()
    return render(request, 'main/result.html',
                  {'graph_path': site_output['graph_path'], 'output': site_output['output']}) #{'params_dict': params_dict})


def params(request):

    if request.method == 'POST':
        algos = SelectAlgosForm(request.POST)
        problems = SelectProblemsForm(request.POST)
        if algos.is_valid() and problems.is_valid():
            algos_select = algos.cleaned_data.get('algos', [])
            problems_select = problems.cleaned_data.get('problems', [])
            output.problem = problems_select
            output.algos = algos_select

    params = SetAlgosParamsForm()

    return render(request, 'main/params.html', {'params': params})


def graph(request):
    file_id = request.GET['file']
    img = open(file_id, 'rb')
    response = FileResponse(img)

    return response

def history(request):
    try:
        if request.user.is_authenticated:
            history1 = HistoryRecord(username=request.user.username, graph_path=output.graph_path, txt_path=output.txt_path, title=str(datetime.now()))
            history1.save()
    except:
        pass

    history = HistoryRecord.objects.all()

    return render(request, 'main/history.html', {'history': history})
c = 2

def outsavings(request):
    #output_txt = open('')
    record_id = None
    if request.method == 'GET':
        record_id = request.GET['id']

    history_rec = HistoryRecord.objects.get(id=record_id)
    graph_path = history_rec.graph_path
    txt_path = history_rec.txt_path

    txt_file = open(txt_path, 'r')
    txt_read = txt_file.read()

    return render(request, 'main/outsavings.html', {'txt': txt_read, 'graph_path': graph_path, 'history_rec': history_rec})