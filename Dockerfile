FROM ubuntu:latest
LABEL authors="Sasha"

ENTRYPOINT ["top", "-b"]