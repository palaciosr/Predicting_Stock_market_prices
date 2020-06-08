FROM python:3.7


# COPY . /Stock_predictions
COPY requirements.txt requirements.txt

# WORKDIR /Stock_predictions
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
