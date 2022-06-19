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

### Example 1:

```
 docker run -it \
  -w /notebooks \
  -v $PWD/notebooks:/notebooks  \
  --net=host \
  --rm ken2s/jupyterlab \
  jupyter-lab --allow-root --NotebookApp.token=''
```

Visiting [http://localhost:8888/](http://localhost:8888/) in a browser loads JupyterLab.

### Example 2:

```
 docker run -it \
  -w /notebooks \
  -v $PWD/notebooks:/notebooks  \
  --name jupyterlab \
  --net=host \
  ken2s/jupyterlab
```

Visiting `http://<hostname>:8888/?token=<token>` in a browser loads JupyterLab, where:

- `hostname` is the name of the computer running Docker
- `token` is the secret token printed in the console.

The container remains intact for restart after the Jupyter Server exits.

## URLs
- https://github.com/ken2s/jupyterlab
- https://hub.docker.com/r/ken2s/jupyterlab
