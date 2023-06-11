FROM jupyter/scipy-notebook

USER ${NB_USER}

WORKDIR /tmp

ENV CONDA_DIR=/opt/conda
ENV JAVA_HOME=/opt/conda/jre

COPY --chown=${NB_UID}:${NB_GID} requirements.txt ./
RUN pip install --upgrade pip  &&\
    pip install --quiet --no-cache-dir -r ./requirements.txt

RUN mamba install beakerx openjdk=8 pyimagej rise \
    jupyter_contrib_nbextensions -c conda-forge -y &&\
    mamba clean --all -f -y && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

RUN pip install --quiet --no-cache-dir git+https://github.com/imagej/pyimagej.git@1.4.1 &&\
    wget https://raw.githubusercontent.com/imagej/pyimagej/1.4.1/doc/Classic-Segmentation.ipynb &&\
    jupyter nbconvert --to python Classic-Segmentation.ipynb &&\
    python Classic-Segmentation.py
RUN wget https://raw.githubusercontent.com/imagej/pyimagej/1.4.1/doc/Puncta-Segmentation.ipynb &&\
    wget https://raw.githubusercontent.com/imagej/pyimagej/1.4.1/doc/sample-data/test_still.tif &&\
    mkdir sample-data &&\
    mv test_still.tif sample-data &&\
    jupyter nbconvert --to python Puncta-Segmentation.ipynb &&\
    python Puncta-Segmentation.py

RUN fix-permissions "${CONDA_DIR}" &&\
    fix-permissions "/home/${NB_USER}"

WORKDIR /notebooks

EXPOSE 8888
