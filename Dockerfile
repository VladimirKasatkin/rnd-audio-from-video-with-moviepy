FROM docker.saritasa.com/centos7-python361-nginx-uwsgi
WORKDIR /home/www/app
COPY requirements.txt /home/www/app/requirements.txt
COPY install.py /home/www/app/install.py
RUN /bin/bash -c "pip3 install -r requirements.txt"
RUN /bin/bash -c "python3 install.py"
### Add source code to container
ADD . /home/www/app/
