from django.db import models
import numpy as np
from io import StringIO
import matplotlib.pyplot as plt

class Algos(models.Model):
    algos = models.CharField('Algorithms', max_length=250)

    def __str__(self):
        return self.algos

    class Meta:
        verbose_name = 'Algorithm'
        verbose_name_plural = 'Algorithms'

class Problems(models.Model):
    problems = models.CharField('Problems', max_length=250)

    def __str__(self):
        return self.problems

    class Meta:
        verbose_name = 'Problem'
        verbose_name_plural = 'Problems'

class Output:

    def __init__(self):
        self.problems = dict()
        self.algos = dict()

    def output(self, problems, algos):
        self.problems = problems
        self.algos = algos


    def get_output(self):
        return list(self.problems.keys()) + list(self.algos.keys())

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

