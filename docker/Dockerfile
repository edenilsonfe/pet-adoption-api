FROM python:3.6-stretch

ENV PYTHONUNBUFFERED 1

COPY . /server
RUN pip install -r /server/requirements-dev.txt

RUN cp /server/docker/entrypoint /entrypoint \
    && chmod +x /entrypoint

EXPOSE 8000

WORKDIR /server

ENTRYPOINT [ "/entrypoint" ]
