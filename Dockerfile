FROM ubuntu

RUN cd ~ \
    && apt-get update \
    && apt-get install wget sed python3 python3-pip -y \
    && pip3 install requests \

COPY entry.sh entry.sh 

ENTRYPOINT ["sh","entry.sh"]
