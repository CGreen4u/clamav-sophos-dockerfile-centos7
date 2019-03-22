#Chris Green

#set up centos
FROM centos:7
RUN yum -y update

#install clamav
WORKDIR  /root/
RUN  yum -y install epel-release \
&& yum -y install clamav \
&& freshclam \
#install sophos
&& yum -y install wget \
&& wget https://github.com/maliceio/malice-av/raw/master/sophos/sav-linux-free-9.tgz \
&& tar xzvf sav-linux-free-9.tgz \
&& ./sophos-av/install.sh /opt/sophos --update-free --acceptlicence --autostart=False --enableOnBoot=False --automatic --ignore-existing-installation --update-source-type=s \
#install GNU Privacy Guard
&& yum install gnupg

RUN mkdir -p /product
WORKDIR /product
RUN mkdir -p /usr/src/app

FROM python:3-onbuild
COPY requirements.txt /usr/src/app/requirements.txt
WORKDIR /usr/src/app

COPY main.py .

CMD ["python", "main.py"]

EXPOSE 5001
