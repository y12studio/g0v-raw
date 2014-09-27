FROM y12docker/pbase

ADD . /opt/app
RUN pip install -r /opt/app/requirements.txt
WORKDIR /opt/app

CMD ["/sbin/my_init"]
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*