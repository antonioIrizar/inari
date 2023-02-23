FROM python:3.11.2-slim

ENV HOMEDIR=/app/ \
  TERM=vt100 \
  C_FORCE_ROOT=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONPATH=/app

ARG ENV

WORKDIR $HOMEDIR

# hadolint ignore=DL3008,DL3013
RUN apt-get update -y --fix-missing \
  && apt-get clean \
  && apt-get install -y --no-install-recommends supervisor git make wait-for-it openssl libssl1.1 liblz4-1 libgnutls30 \
  && apt-get install --assume-yes --no-install-recommends postgresql-client-13 \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* \
  && pip install --no-cache-dir --upgrade pip poetry \
  && poetry config virtualenvs.create false

COPY src/pyproject.toml $HOMEDIR/pyproject.toml
RUN if [ "$ENV" = "local" ] ; then poetry install ; else poetry install --no-dev ; fi

COPY src $HOMEDIR

COPY bin/* /usr/local/bin/
