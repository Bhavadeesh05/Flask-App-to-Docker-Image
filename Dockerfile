FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN python -m pip install --upgrade pip
RUN mkdir /new_app
WORKDIR /new_app
ADD . /new_app/
RUN apt-get update && apt-get install -y vim
RUN pip install -r requirements.txt
EXPOSE 8000
CMD python app.py
