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
RUN wget https://downloads.imagej.net/fiji/latest/fiji-linux64.zip &&\
    wget https://maven.scijava.org/service/local/artifact/maven/redirect?r=releases&g=net.imglib2&a=imglib2-unsafe&v=0.4.1&e=jar &&\
    wget https://maven.scijava.org/service/local/artifact/maven/redirect?r=releases&g=net.imglib2&a=imglib2-imglyb&v=1.0.1&e=jar
RUN unzip fiji-linux64.zip

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

USER root
WORKDIR /home/${NB_USER}/work
RUN rm fiji-linux64.zip &&\
    mv Fiji.app /opt/ &&\
    mv *.jar /opt/Fiji.app/jars/
RUN rm -rf /var/lib/apt/lists/* &&\
    usermod -aG sudo jovyan &&\
    echo 'jovyan ALL=(ALL) NOPASSWD: ALL' | EDITOR='tee -a' visudo

EXPOSE 8888
