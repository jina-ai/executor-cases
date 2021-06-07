FROM jinaai/jina:master

RUN pip install -r requirements.txt

ENTRYPOINT ["jina", "pod", "--uses", "config.yml"]