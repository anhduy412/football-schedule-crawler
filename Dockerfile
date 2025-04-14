FROM apache/airflow:2.6.0
COPY ./requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt
# docker build . -f ./Dockerfile -t football_schedule:1.1