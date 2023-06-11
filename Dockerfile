FROM jupyter/datascience-notebook:2023-06-04

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

RUN mamba install beakerx openjdk=8 pyimagej rise \
    jupyter_contrib_nbextensions -c conda-forge -y &&\
    mamba clean --all -f -y && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

RUN pip install --quiet --no-cache-dir git+https://github.com/imagej/pyimagej.git@main &&\
    wget https://raw.githubusercontent.com/imagej/pyimagej/main/doc/Puncta-Segmentation.ipynb &&\
    wget https://raw.githubusercontent.com/imagej/pyimagej/main/doc/Classic-Segmentation.ipynb &&\
    wget https://raw.githubusercontent.com/imagej/pyimagej/main/doc/sample-data/test_still.tif &&\
    wget https://scikit-image.org/docs/dev/_downloads/07fcc19ba03226cd3d83d4e40ec44385/auto_examples_python.zip &&\
    unzip auto_examples_python.zip &&\
    sed -e 's/^plotly/#plotly/g' data/plot_3d.py | python &&\
    python data/plot_general.py &&\
    python data/plot_scientific.py &&\
    python data/plot_specific.py &&\
    mkdir sample-data &&\
    mv test_still.tif sample-data &&\
    jupyter nbconvert --to python Puncta-Segmentation.ipynb &&\
    python Puncta-Segmentation.py &&\
    jupyter nbconvert --to python Classic-Segmentation.ipynb &&\
    python Classic-Segmentation.py

RUN fix-permissions "${CONDA_DIR}" &&\
    fix-permissions "/home/${NB_USER}"

ENTRYPOINT ["tini", "-g", "--"]
CMD ["start-notebook.sh", "--LabApp.token=''"]

WORKDIR /notebooks
EXPOSE 8888
