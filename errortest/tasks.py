from celeryerror.celery import app

@app.task()
def debug_task():
    raise Exception('FOO')
