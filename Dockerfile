FROM jupyter/datascience-notebook

USER root

RUN apt-get update && apt-get install -y \
    make \
    curl \
    file \
    git
COPY requirements.txt $PWD
RUN pip install -r requirements.txt