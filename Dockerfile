FROM ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /var/www

RUN apt update -y && apt -y install python3 python3-pip git ffmpeg

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5500

CMD [ "python3", "app.py" ]