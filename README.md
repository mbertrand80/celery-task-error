Demo
====

This demonstrates an issue that manifests with a Celery Task that has
been wrapped by both the Sentry SDK and New Relic.

```
Exception Type: AttributeError at /debug-task
Exception Value: 'method-wrapper' object has no attribute '__module__'
```

This error only appears when the New Relic library uses the wrappers C extension instead of the pure python version.

Setup
-----

Using Docker is the fastest way to see the issue.

1. Clone the repo
2. Run
    ```
    docker-compose up web
    ```
3. Visit http://0.0.0.0:8080/debug-task

You should then see the following

```
Environment:

Request Method: GET
Request URL: http://0.0.0.0:8080/debug-task

... DJANGO INFO ...

Traceback:

File "/root/.local/lib/python2.7/site-packages/django/core/handlers/exception.py" in inner
  41.             response = get_response(request)

File "/root/.local/lib/python2.7/site-packages/django/core/handlers/base.py" in _get_response
  187.                 response = self.process_exception_by_middleware(e, request)

File "/root/.local/lib/python2.7/site-packages/django/core/handlers/base.py" in _get_response
  185.                 response = wrapped_callback(request, *callback_args, **callback_kwargs)

File "/usr/src/errortest/views.py" in task_trigger
  9.     result = debug_task.apply(args=[])

File "/root/.local/lib/python2.7/site-packages/celery/app/task.py" in apply
  738.             propagate=throw, app=self._get_app(),

File "/root/.local/lib/python2.7/site-packages/newrelic/hooks/application_celery.py" in build_tracer
  168.             return _build_tracer(name, task, *args, **kwargs)

File "/root/.local/lib/python2.7/site-packages/sentry_sdk/integrations/celery.py" in sentry_build_tracer
  62.                 task.__call__ = _wrap_task_call(task, task.__call__)

File "/root/.local/lib/python2.7/site-packages/sentry_sdk/integrations/celery.py" in _wrap_task_call
  160.     @functools.wraps(f)

File "/usr/lib64/python2.7/functools.py" in update_wrapper
  33.         setattr(wrapper, attr, getattr(wrapped, attr))

Exception Type: AttributeError at /debug-task
Exception Value: 'method-wrapper' object has no attribute '__module__'

```


Notes
-----

* The Docker build sets the environment variable `NEW_RELIC_EXTENSIONS=true` to ensure the C extension is compiled and used.
* It isn't important to run a Celery broker as the problem only manifests when calling `task.apply()`.
* Database migrations aren't needed either. Django is here mostly because this more closely simulates how we're using Celery.