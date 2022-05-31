import os.path
import pathlib
import subprocess

from django.db import models
import numpy as np
from io import StringIO
import matplotlib.pyplot as plt


class Algos(models.Model):
    name = models.CharField('Algorithm', max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Algorithm'
        verbose_name_plural = 'Algorithms'


class Problems(models.Model):
    name = models.CharField('Problem', max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Problem'
        verbose_name_plural = 'Problems'


class Output:

    def __init__(self):
        self.problem = None
        self.algos = None
        self.algos_params = None

    # def output(self, problem, algos, algos_params=None):
    #     self.problem = problem
    #     self.algos = algos
    #     self.algos_params = algos_params

    def get_output(self):
        res = {'problem': None, 'algos': []}
        if self.algos:
            for alg in self.algos:
                res['algos'].append(alg.name)

        if self.problem:
            res['problem'] = self.problem.name

        # algs_project_path = '/home/sd/prj/thesis/PyProgs/MethodsCompare'
        algs_project_path = 'C:/PycharmProjects/methodscompare'
        # algs_project_env_path = '/home/sd/anaconda3/envs/scientific/bin'
        algs_project_env_path = 'C:/PycharmProjects/methodscompare/venv/Scripts'

        algos_params_string = ''
        for key, value in self.algos_params.items():
            algos_params_string += f'{key},{value};'
        print(algos_params_string)
        out = subprocess.check_output([os.path.join(algs_project_env_path, 'python.exe'),
                                       os.path.join(algs_project_path, "run_algs_command.py"),
                                       "-a", ','.join(res['algos']), "-p", self.problem.name, "-k", algos_params_string],
                                      stderr=subprocess.STDOUT)

        lines = out.decode('utf-8')
        print(lines)
        results_path = lines
        contents = os.listdir(results_path)
        for it in contents:
            item_full_path = os.path.join(results_path, it)
            if os.path.isfile(item_full_path):
                if os.path.splitext(item_full_path)[1] == '.png':
                    self.graph_path = item_full_path
                    res['graph_path'] = item_full_path
                elif os.path.splitext(item_full_path)[1] == '.txt':
                    self.txt_path = item_full_path
                    file = open(item_full_path, 'r')
                    res['output'] = file.read()


        return res

    @staticmethod
    def return_graph():
        x = np.arange(0, np.pi * 3, .1)
        y = np.sin(x)

        fig = plt.figure(figsize=(2, 2))
        plt.plot(x, y)

        imgdata = StringIO()
        fig.savefig(imgdata, format='svg')
        imgdata.seek(0)

        data = imgdata.getvalue()
        return data

    def __str__(self):
        return self


class HistoryRecord(models.Model):
    username = models.CharField('User', max_length=250)
    title = models.CharField('Title', max_length=250)

    graph_path = models.CharField('Graph', max_length=250)
    txt_path = models.CharField('TXT', max_length=250)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'History'
        verbose_name_plural = 'Histories'
