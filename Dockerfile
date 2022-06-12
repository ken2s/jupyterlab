FROM jupyter/datascience-notebook

USER ${NB_USER}
WORKDIR /home/${NB_USER}/work
COPY --chown=${NB_UID}:${NB_GID} requirements.txt ./

RUN pip install --upgrade pip  &&\
    pip install --quiet --no-cache-dir -r ./requirements.txt
RUN conda install beakerx openjdk=8 pyimagej rise \
    jupyter_contrib_nbextensions -c conda-forge -y &&\
    conda clean -i -t -y

USER root
RUN fix-permissions "${CONDA_DIR}" &&\
    fix-permissions "/home/${NB_USER}"

EXPOSE 8888
