ARG PYTHON_VERSION=andrejreznik/python-gdal:py3.8.2-gdal3.0.4
# FROM andrejreznik/python-gdal:stable as python
# define an alias for the specfic python version used in this file.
FROM ${PYTHON_VERSION} as python

# Python build stage
FROM python as python-build-stage

# args
ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1
ARG BUILD_ENVIRONMENT=local
ENV LC_CTYPE=en_US.UTF-8 \
  LANG=en_US.UTF-8
ENV PROJECT_NAME=asgroup \
  TZ=America/Lima

# Install apt packages
RUN apt-get update && apt-get install --no-install-recommends -y build-essential libssl-dev libffi-dev python3-dev
# postgis libs
RUN apt-get update && apt-get install -y binutils libproj-dev gdal-bin libgeos-dev libgdal-dev
# build essential
RUN apt-get install -y libxml2-dev libxslt1-dev zlib1g-dev
# Requirements are installed here to ensure they will be cached.
COPY ./requirements .

# Create Python Dependency and Sub-Dependency Wheels.
RUN pip wheel --wheel-dir /usr/src/app/wheels  \
  -r ${BUILD_ENVIRONMENT}.txt


# Python 'run' stage
FROM python as python-run-stage

ARG BUILD_ENVIRONMENT=local
ARG APP_HOME=/app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV BUILD_ENV ${BUILD_ENVIRONMENT}

WORKDIR ${APP_HOME}

# Install required system dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
  # psycopg2 dependencies
  libpq-dev \
  # Translations dependencies
  gettext \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

# All absolute dir copies ignore workdir instruction. All relative dir copies are wrt to the workdir instruction
# copy python dependency wheels from python-build-stage
COPY --from=python-build-stage /usr/src/app/wheels  /wheels/

# use wheels to install python dependencies
RUN pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/* \
	&& rm -rf /wheels/
RUN  pip install --upgrade pip
COPY ./compose/production/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./compose/local/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

# Update C env vars so compiler can find gdal
ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal
ENV GDAL_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu/gdal


# copy application code to WORKDIR
COPY . ${APP_HOME}

ENTRYPOINT ["/entrypoint"]
