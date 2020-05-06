from django.conf.urls import url
from errortest.views import task_trigger

urlpatterns = [
    url(r'^debug-task$', task_trigger, name='celery-task-trigger')
]