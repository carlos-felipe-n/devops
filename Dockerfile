FROM python

WORKDIR /app
COPY . .

RUN pip install flask

CMD [ "python", "-m", "flask", "run", "--host=0.0.0.0" ]
