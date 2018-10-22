FROM python:alpine

RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src /src

ENTRYPOINT [ "python3" ]
CMD [ "/src/index.py" ]