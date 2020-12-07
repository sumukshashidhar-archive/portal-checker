FROM python3:alpine

WORKDIR /src/app

COPY . .

RUN pip install -r requirements.txt

ADD crontab /etc/cron.d/hello-cron

RUN chmod 0644 /etc/cron.d/hello-cron

RUN apt-get update
RUN apt-get -y install cron

CMD cron
