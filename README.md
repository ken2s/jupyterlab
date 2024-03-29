# Docker-JupyterLab for PyImageJ

<!-- ![Publish Docker image workflow](https://github.com/ken2s/jupyterlab/actions/workflows/build-and-push-image.yml/badge.svg) -->
<a href="https://github.com/ken2s/jupyterlab/actions" rel="nofollow noopener" target="_blank"><img src="https://github.com/ken2s/jupyterlab/actions/workflows/build-and-push-image.yml/badge.svg" alt="Publish Docker image workflow"></a></p>

## Notebooks

- [Python3](https://www.python.org)
    - [PyImageJ](https://github.com/imagej/pyimagej)
        - [Clojure](https://clojure.org/)
        - [Groovy](http://groovy-lang.org/)
        - [Java](https://www.java.com/)
        - [Kotlin](https://kotlinlang.org/)
        - [Scala](https://www.scala-lang.org/)
        - SQL
    - [scikit-image](https://scikit-image.org)
    - [OpenCV](https://opencv.org)
<!-- - [Julia](https://julialang.org)
- [R](https://www.r-project.org)
- [ImageJ](https://imagej.nih.gov/ij/)
- [BeakerX](http://beakerx.com)
- [OpenJDK](https://openjdk.java.net) -->

![notebooks](https://raw.githubusercontent.com/ken2s/jupyterlab/main/notebooks.png)

## Usage

On the terminal, create the `notebooks` directory in the current directory. Next, enter the following docker command.

### Example 1:

```
 docker run -it \
  -p 8888:8888 \
  --name jupyterlab \
  -v $PWD/notebooks:/notebooks  \
  ken2s/jupyterlab
```

Visiting `http://<hostname>:8888/lab?token=<token>` in a browser loads JupyterLab, where:

- `hostname` is the name of the computer running Docker
- `token` is the secret token printed in the console.

The container remains intact for restart after the Jupyter Server exits.

### Example 2:

```
 docker run -it \
  --rm \
  --env NB_UID=1000 \
  --env NB_GID=100 \
  --net="host" \
  -v $PWD/notebooks:/notebooks  \
  ken2s/jupyterlab
```

- By `--rm` option, automatically remove the container when it exits.
- By `--env` option, the notebook user `jovyan` in the container can be given the same `UID` or `GID` as the host user.
- By `--net="host"` option, use host network mode for the container.

## URLs
- https://github.com/ken2s/jupyterlab
- https://hub.docker.com/r/ken2s/jupyterlab
- [Customizing the Jupyter container to run PyImageJ (in Japanease)](https://qiita.com/ken2s/items/8784576d4f22432c4270)

## References
- https://jupyter-docker-stacks.readthedocs.io/
- https://pyimagej.readthedocs.io/
- https://github.com/imagej/pyimagej/
