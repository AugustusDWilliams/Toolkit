# Docker Cheatsheet

| Command | Action |
| ------- | ------ |
| FROM | specifies the base (parent) image |
| LABEL | provides metadata. Good place to include maintainer info |
| ENV | sets a persistent environment variable |
| RUN | runs a command and creates an image layer. Used to install packages into containers |
| COPY | copies files and directories to the container |
| ADD | copies files and directories to the container, can upack local .tar files |
| CMD |provides a command and arguments for an executing container. Parameters can be overridden. There can be only one CMD |
| WORKDIR | sets the working directory for the instructions that follow |
| ARG | defines a variable to pass to Docker at build-time |
| ENTRYPOINT | provides command and arguments for an executing container, arguments persist |
| EXPOSE | exposes a port |
| VOLUME | creates a directory mount point to access and store persistent data |
