FROM python:3.7

#C:\Users\palac\Desktop\Deep_learning_stock_movements\Stock_predictions\ml_sp500.py
#relative
#C:\Users\palac\Desktop\Deep_learning_stock_movements\Dockerfile

COPY . /Stock_predictions
COPY ./requirements.txt requirements.txt

WORKDIR /Stock_predictions
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["main.py"]
