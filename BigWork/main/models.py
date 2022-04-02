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

    def output(self, problem, algos):
        self.problem = problem
        self.algos = algos

    def get_output(self):
        res = {'problem': None, 'algos': []}
        if self.algos:
            for alg in self.algos:
                res['algos'].append(alg.name)

        if self.problem:
            res['problem'] = self.problem.name

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
