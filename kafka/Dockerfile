FROM openjdk:11.0.10-jre-buster

RUN apt-get update && \
    apt-get install -y curl
         
ENV KAFKA_VERSION 2.8.0
ENV SCALA_VERSION 2.13 

RUN  mkdir /tmp/kafka && \
    curl "https://apache.mivzakim.net/kafka/${KAFKA_VERSION}/kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz" \
    -o /tmp/kafka/kafka.tgz && \
    mkdir /kafka && cd /kafka && \
    tar -xvzf /tmp/kafka/kafka.tgz --strip 1

COPY kafka/start-kafka.sh  /usr/bin
RUN chmod +x  /usr/bin/start-kafka.sh


# Not Working!!!!
# COPY kafka/kafka-topics.sh  /usr/bin
# RUN chmod +x  /usr/bin/kafka-topics.sh --create \
#     --zookeeper localhost:2181 \
#     --replication-factor 1 \
#     --partitions 1 \
#     --topic test

CMD ["start-kafka.sh"]

