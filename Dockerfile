FROM python:3.7-alpine

WORKDIR /usr/src/app
RUN apk update && apk add --no-cache gcc musl-dev linux-headers

ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_RUN_PORT=8080

COPY . .
RUN pip install -r requirements.txt

EXPOSE 8080
CMD ["flask", "run"]