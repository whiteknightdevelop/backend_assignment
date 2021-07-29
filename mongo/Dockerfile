# FROM mongo:latest

# # install Python 3
# RUN apt-get update && apt-get install -y python3 python3-pip
# RUN apt-get -y install python3.7-dev
# RUN pip3 install pymongo

# EXPOSE 27017



# FROM mongo:latest

# RUN mkdir -p /data/db2 \
#     && echo "dbpath = /data/db2" > /etc/mongodb.conf \
#     && chown -R mongodb:mongodb /data/db2

# COPY . /data/db2

# RUN mongod --fork --logpath /var/log/mongodb.log --dbpath /data/db2 --smallfiles \
#     && CREATE_FILES=/data/db2/scripts/*-create.js \
#     && for f in $CREATE_FILES; do mongo 127.0.0.1:27017 $f; done \
#     && INSERT_FILES=/data/db2/scripts/*-insert.js \
#     && for f in $INSERT_FILES; do mongo 127.0.0.1:27017 $f; done \
#     && mongod --dbpath /data/db2 --shutdown \
#     && chown -R mongodb /data/db2

# VOLUME /data/db2

# CMD ["mongod", "--config", "/etc/mongodb.conf", "--smallfiles"]









