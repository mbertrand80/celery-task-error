# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from errortest.tasks import debug_task
# Create your views here.

def task_trigger(request):
    result = debug_task.apply(args=[])

    return HttpResponse(content=result.get())