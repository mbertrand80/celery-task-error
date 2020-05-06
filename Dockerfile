FROM centos:latest

RUN yum install -y gcc python2 python2-devel
ENV PYTHONPATH /usr/src

COPY requirements.txt /usr/src/requirements.txt
ENV NEW_RELIC_EXTENSIONS=true
RUN pip2 install --user -U -r /usr/src/requirements.txt

COPY . /usr/src/
WORKDIR /usr/src

ENV PYTHONUNBUFFERED=1
CMD ["python2", "/usr/src/manage.py", "runserver", "0.0.0.0:8080"]