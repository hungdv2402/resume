FROM alpine:3.21

RUN apk add --no-cache \
    texlive texlive-luatex texmf-dist-latexextra texmf-dist-fontsrecommended texmf-dist-fontsextra

WORKDIR /data
VOLUME ["/data"]
