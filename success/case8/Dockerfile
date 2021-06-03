ARG JINA_VERSION

FROM jinaai/jina:$JINA_VERSION

ADD *.py *.yml ./

RUN pip install -r requirements.txt

ENTRYPOINT ["jina", "pod", "--uses", "config.yml"]