FROM python:3.6
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
RUN python models.py
RUN python manage.py
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["routes.py"]