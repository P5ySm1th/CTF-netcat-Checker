FROM python:3.10.11-slim

WORKDIR /chall

RUN apt-get update && \
    apt-get install -y socat && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY src/ /chall/

RUN chmod +x server.py flag.py verify.py

EXPOSE 1259

CMD ["socat", "-d", "tcp-listen:1259,reuseaddr,fork", "exec:'./server.py',stderr"]
