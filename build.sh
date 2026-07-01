#!/usr/bin/env bash

docker build -t latex .
docker run --rm -i -v "$PWD":/data latex lualatex Duong-Viet-Hung-RN.tex
