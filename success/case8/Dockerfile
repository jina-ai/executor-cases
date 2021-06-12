FROM jinaai/jina:master

ADD *.py *.yml ./

RUN pip install -r requirements.txt

ENTRYPOINT ["jina", "pod", "--uses", "config.yml"]