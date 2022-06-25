FROM jupyter/datascience-notebook:2022-06-20

USER root
RUN apt-get update &&\
    apt-get install -y cmake xvfb &&\
    apt-get clean &&\
    rm -rf /usr/local/src/* &&\
    rm -rf /var/lib/apt/lists/* &&\
    usermod -aG sudo jovyan &&\
    echo 'jovyan ALL=(ALL) NOPASSWD: ALL' | EDITOR='tee -a' visudo

USER ${NB_USER}
WORKDIR /tmp
ENV CONDA_DIR=/opt/conda
ENV JAVA_HOME=/opt/conda/jre

COPY --chown=${NB_UID}:${NB_GID} packages.* ./
COPY --chown=${NB_UID}:${NB_GID} requirements.txt ./
RUN pip install --upgrade pip  &&\
    pip install --quiet --no-cache-dir -r ./requirements.txt &&\
    julia ./packages.jl &&\
    Rscript ./packages.R

RUN conda install beakerx openjdk=8 pyimagej rise \
    jupyter_contrib_nbextensions -c conda-forge -y &&\
    conda clean -i -t -y

RUN pip install --quiet --no-cache-dir git+https://github.com/imagej/pyimagej.git@master &&\
    wget https://raw.githubusercontent.com/imagej/pyimagej/master/doc/Puncta-Segmentation.ipynb &&\
    wget https://raw.githubusercontent.com/imagej/pyimagej/master/doc/sample-data/test_still.tif &&\
    mkdir sample-data &&\
    mv test_still.tif sample-data &&\
    jupyter nbconvert --to python Puncta-Segmentation.ipynb &&\
    python Puncta-Segmentation.py

RUN echo "c.NotebookApp.token=''" >> ~/.jupyter/jupyter_notebook_config.py &&\
    fix-permissions "${CONDA_DIR}" &&\
    fix-permissions "/home/${NB_USER}"

WORKDIR /notebooks
EXPOSE 8888
