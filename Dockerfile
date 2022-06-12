FROM jupyter/datascience-notebook:2022-06-06

USER root
RUN apt-get update &&\
    apt-get install -y cmake &&\
    apt-get clean &&\
    rm -rf /usr/local/src/*

USER ${NB_USER}
WORKDIR /home/${NB_USER}/work
COPY --chown=${NB_UID}:${NB_GID} packages.* .
COPY --chown=${NB_UID}:${NB_GID} requirements.txt .

RUN pip install --upgrade pip  &&\
    pip install --quiet --no-cache-dir -r ./requirements.txt &&\
    julia ./packages.jl &&\
    Rscript ./packages.R

RUN conda install beakerx openjdk=8 pyimagej rise \
    jupyter_contrib_nbextensions -c conda-forge &&\
    conda clean -i -t -y

RUN echo "c.NotebookApp.token=''" >> ~/.jupyter/jupyter_notebook_config.py &&\
    fix-permissions "${CONDA_DIR}" &&\
    fix-permissions "/home/${NB_USER}"

USER root
RUN rm -rf /var/lib/apt/lists/* &&\
    usermod -aG sudo jovyan &&\
    echo 'jovyan ALL=(ALL) NOPASSWD: ALL' | EDITOR='tee -a' visudo

EXPOSE 8888
