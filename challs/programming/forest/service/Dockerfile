FROM ubuntu:latest
ENV user=forestuser
RUN apt-get update
RUN apt-get install -y xinetd python cmake python-pip libglib2.0-dev git
RUN useradd -m $user
RUN echo "$user     hard    nproc       20" >> /etc/security/limits.conf
COPY ./forest.py /home/$user/
COPY ./flag /
COPY ./forestservice /etc/xinetd.d/
COPY ./make_unicorn.sh /opt/
RUN chown -R root:$user /home/$user
RUN chmod -R 750 /home/$user
RUN chown root:$user /flag
RUN chmod 440 /flag
RUN sh /opt/make_unicorn.sh
RUN mkdir /opt/eggcache
RUN chown -R $user:$user /opt/eggcache
RUN sudo pip install keystone-engine
EXPOSE 31337
CMD ["/usr/sbin/xinetd", "-d"]
