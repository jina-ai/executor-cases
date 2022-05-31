ARG JINA_VERSION

FROM jinaai/jina:$JINA_VERSION

ADD *.yml ./

RUN pip install -r requirements.txt

ENTRYPOINT ["jina", "pod", "--uses", "config.yml"]
