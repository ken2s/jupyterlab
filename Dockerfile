FROM jupyter/datascience-notebook:2022-06-13

USER root
RUN apt-get update &&\
    apt-get install -y cmake xvfb &&\
    apt-get clean &&\
    rm -rf /usr/local/src/*

USER ${NB_USER}
WORKDIR /home/${NB_USER}/work

COPY --chown=${NB_UID}:${NB_GID} packages.* ./
COPY --chown=${NB_UID}:${NB_GID} requirements.txt ./

RUN pip install --upgrade pip  &&\
    pip install --quiet --no-cache-dir -r ./requirements.txt &&\
    julia ./packages.jl &&\
    Rscript ./packages.R

RUN conda install beakerx openjdk=8 pyimagej rise \
    jupyter_contrib_nbextensions -c conda-forge -y &&\
    conda clean -i -t -y

RUN echo "c.NotebookApp.token=''" >> ~/.jupyter/jupyter_notebook_config.py &&\
    fix-permissions "${CONDA_DIR}" &&\
    fix-permissions "/home/${NB_USER}"

RUN wget https://downloads.imagej.net/fiji/latest/fiji-linux64.zip &&\
    unzip ./fiji-linux64.zip

RUN wget https://maven.scijava.org/content/repositories/public/net/imglib2/imglib2-unsafe/0.4.1/imglib2-unsafe-0.4.1.jar &&\ 
    wget https://maven.scijava.org/content/repositories/public/net/imglib2/imglib2-imglyb/1.0.1/imglib2-imglyb-1.0.1.jar &&\
    mv ./*.jar ./Fiji.app/jars/

USER root
WORKDIR /home/${NB_USER}/work

RUN rm fiji-linux64.zip &&\
    mv Fiji.app /opt/

RUN rm -rf /var/lib/apt/lists/* &&\
    usermod -aG sudo jovyan &&\
    echo 'jovyan ALL=(ALL) NOPASSWD: ALL' | EDITOR='tee -a' visudo

WORKDIR /notebooks
RUN fix-permissions "/notebooks"

EXPOSE 8888
