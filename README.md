# Docker-JupyterLab

<!-- ![Publish Docker image workflow](https://github.com/ken2s/jupyterlab/actions/workflows/build-and-push-image.yml/badge.svg) -->
<a href="https://github.com/ken2s/jupyterlab/actions" rel="nofollow noopener" target="_blank"><img src="https://github.com/ken2s/jupyterlab/actions/workflows/build-and-push-image.yml/badge.svg" alt="Publish Docker image workflow"></a></p>

## Notebooks

- [Python3](https://www.python.org)
    - [OpenCV](https://opencv.org)
    - [PyImageJ](https://github.com/imagej/pyimagej)
        - [Clojure](https://clojure.org/)
        - [Groovy](http://groovy-lang.org/)
        - [Java](https://www.java.com/)
        - [Kotlin](https://kotlinlang.org/)
        - [Scala](https://www.scala-lang.org/)
        - SQL
- [Julia 1.7.3](https://julialang.org)
- [R](https://www.r-project.org)
<!-- - [ImageJ](https://imagej.nih.gov/ij/)
- [BeakerX](http://beakerx.com)
- [OpenJDK](https://openjdk.java.net) -->

![notebooks](https://raw.githubusercontent.com/ken2s/jupyterlab/main/notebooks.png)

## Usage

On the terminal, create the `notebooks` directory in the current directory. Next, enter the following docker command.

### Example 1:

```
 docker run -it \
  -v $PWD/notebooks:/notebooks  \
  -p 8888:8888 \
  --name jupyterlab \
  ken2s/jupyterlab:latest
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
  ken2s/jupyterlab:latest
```

- By `--rm` option, automatically remove the container when it exits.
- By `--env` option, the notebook user `jovyan` in the container can be given the same `UID` or `GID` as the host user.
- By `--net="host"` option, use host network mode for the container.

## URLs
- https://github.com/ken2s/jupyterlab
- https://hub.docker.com/r/ken2s/jupyterlab
