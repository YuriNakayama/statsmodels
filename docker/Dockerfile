FROM jupyter/datascience-notebook

USER root

RUN apt-get update -y && apt-get install -y \
    bash

ADD getCommand.sh /root/getCommand.sh
RUN chmod +x /root/getCommand.sh
RUN bash /root/getCommand.sh

COPY requirements.txt $PWD
RUN pip install -r requirements.txt