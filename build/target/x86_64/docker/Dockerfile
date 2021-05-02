ARG hbmBaseImage=agorasdk.azurecr.io/x86_64/hbm-base:1.0.0
FROM $hbmBaseImage

ARG hbmBaseImage
RUN echo Building from Base image : $hbmBaseImage

RUN apt-get update && \
    apt-get install -y --no-install-recommends python3-pip

RUN pip3 install --upgrade pip
RUN pip3 install numpy

MAINTAINER vscode

ENV PYTHONPATH "${PYTHONPATH}:/usr/lib"
ENV PYTHONOPTIMIZE "1"

COPY lib/* /usr/lib/

COPY module.json /

CMD ["/usr/bin/hbm"]

