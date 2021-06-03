FROM jinaai/jina:master

ADD *.py *.yml ./

ENTRYPOINT ["jina", "pod", "--uses", "config.yml"]