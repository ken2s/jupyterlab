# Docker-JupyterLab

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

```
 docker run -it \
  -p 8888:8888 \
  -w /home/jovyan/notebooks \
  -v $PWD/notebooks:/home/jovyan/notebooks  \
  --rm ken2s/jupyterlab
```

## URLs
- https://github.com/ken2s/jupyterlab
- https://hub.docker.com/r/ken2s/jupyterlab
