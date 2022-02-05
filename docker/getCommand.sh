#!/bin/bash
apt-get update && apt-get install -y \
    make \
    cmake \
    sudo \
    gcc \
    curl \
    file \
    git \
    python3-dev \
    python3-wheel \
    python3-setuptools \
    libmecab-dev \
    mecab \
    mecab-ipadic-utf8


HOME="/home/ubuntu"
mkdir $HOME && chomod 777 $HOME

pip3 install pip -U
pip3 install \
    black \
    isort==4.3.21 \
    jupyter \
    jupyterlab \
    environment_kernels \
    jupytext \
    jupyter-contrib-nbextensions \
    && rm -rf /root/.cache && rm -rf ${HOME}/.cache

jupyter contrib nbextension install --system 
jupyter nbextension install https://github.com/drillan/jupyter-black/archive/master.zip
jupyter nbextension install https://github.com/benjaminabel/jupyter-isort/archive/master.zip
jupyter nbextension enable jupyter-black-master/jupyter-black
jupyter nbextension enable jupyter-isort-master/jupyter-isort
jupyter nbextension enable contrib_nbextensions_help_item/main
jupyter nbextension enable execute_time/ExecuteTime
jupyter nbextension enable highlight_selected_word/main
jupyter nbextension enable keyboard_shortcut_editor/main
jupyter nbextension enable notify/notify
jupyter nbextension enable scratchpad/main
jupyter nbextension enable scroll_down/main
jupyter nbextension enable collapsible_headings/main
jupyter nbextension enable toc2/main
jupyter nbextension enable varInspector/main
jupyter nbextension enable freeze/main

git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git
mecab-ipadic-neologd/bin/install-mecab-ipadic-neologd -y

echo "end $0"