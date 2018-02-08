# Dockerfile for project.
#
# Build:
#
# docker build -t bwv988/psapp .
#

FROM python:3.6-stretch
ENV PYTHONUNBUFFERED "true"

COPY requirements.txt /opt/psapp/
COPY src/trivial/ /opt/psapp/

RUN pip install -r /opt/psapp/requirements.txt

WORKDIR /opt/psapp