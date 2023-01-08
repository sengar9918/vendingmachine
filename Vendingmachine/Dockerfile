FROM python:3.8-slim
RUN mkdir /Vendingmachine
WORKDIR /Vendingmachine
ADD . /Vendingmachine
RUN pip install -r requirements.txt
EXPOSE 8000
CMD python manage.py runserver 0:8000
