FROM python:3.11

RUN apt-get update

# install flask, gunicorn
RUN pip3 install flask gunicorn

WORKDIR /app

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app3:app", "--reload"]