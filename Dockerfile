FROM ubuntu:bionic

RUN apt-get clean && apt-get update && apt-get install -y locales
RUN locale-gen en_US.UTF-8
ENV LANG='en_US.UTF-8' LANGUAGE='en_US:en' LC_ALL='en_US.UTF-8'

RUN apt-get update && \
	apt-get -y install python3 python3-pip git mysql-server libmysqlclient-dev python3 python-dev python3-dev \
     build-essential libssl-dev libffi-dev libxml2-dev libxslt1-dev zlib1g-dev \
     python-pip && \
	rm -rf /var/lib/apt/lists/* && \
	locale-gen en_US.UTF-8 && \
	python3 -m pip install --no-cache-dir Django mysqlclient PyMySQL pytz sqlparse django-recaptcha

WORKDIR /usr/src/app
COPY . .
WORKDIR /usr/src/app/
CMD [ "python3", "manage.py", "runserver", "0.0.0.0:80" ]
