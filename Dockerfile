#Chris Green

#install clamav
FROM centos:7 AS centos
RUN yum -y update

#clamav install
FROM centos
WORKDIR  /root/
RUN  yum -y install epel-release \
&& yum -y install clamav

#sophos install starts 
FROM centos
WORKDIR /root/
RUN yum -y install wget \
&& wget https://github.com/maliceio/malice-av/raw/master/sophos/sav-linux-free-9.tgz \
&& tar xzvf sav-linux-free-9.tgz \
&& ./sophos-av/install.sh /opt/sophos --update-free --acceptlicence --autostart=False --enableOnBoot=False --automatic --ignore-existing-installation --update-source-type=s
