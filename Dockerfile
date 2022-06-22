FROM jupyter/datascience-notebook

USER ${NB_USER}
WORKDIR /home/${NB_USER}/work

COPY --chown=${NB_UID}:${NB_GID} requirements.txt ./
RUN pip install --upgrade pip  &&\
    pip install --quiet --no-cache-dir -r ./requirements.txt

RUN conda install beakerx openjdk=8 pyimagej rise \
    jupyter_contrib_nbextensions -c conda-forge -y &&\
    conda clean -i -t -y

RUN wget https://downloads.imagej.net/fiji/latest/fiji-linux64.zip &&\
    unzip ./fiji-linux64.zip

RUN wget https://maven.scijava.org/content/repositories/public/net/imglib2/imglib2-unsafe/0.4.1/imglib2-unsafe-0.4.1.jar &&\ 
    wget https://maven.scijava.org/content/repositories/public/net/imglib2/imglib2-imglyb/1.0.1/imglib2-imglyb-1.0.1.jar &&\
    mv ./*.jar ./Fiji.app/jars/

RUN fix-permissions "${CONDA_DIR}" &&\
    fix-permissions "/home/${NB_USER}"

RUN pip install --quiet --no-cache-dir git+https://github.com/imagej/pyimagej.git@master

USER root

RUN rm /home/${NB_USER}/work/fiji-linux64.zip &&\
    mv /home/${NB_USER}/work/Fiji.app /opt/

WORKDIR /notebooks

ENV CONDA_DIR=/opt/conda
ENV JAVA_HOME=/opt/conda/jre

EXPOSE 8888
