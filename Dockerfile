FROM python:latest

ARG pyrotate=/home/pyrotate
ARG logdir=/mnt/log

LABEL authors="github.com/ermantraun"
LABEL version="1.0.1"

RUN mkdir -p ${logdir} ${pyrotate}
COPY pyrotate.py ${pyrotate}/pyrotate.py

WORKDIR ${pyrotate}

ENTRYPOINT ["python3", "pyrotate.py"]
