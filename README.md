## Instructions

This project runs a API server with 4 endpoints. It runs docker containers for FLASK and MongoDB.

#### Requirements
* Docker
* docker-compose (v3 file version)

Run `docker-compose up` to start the application.

Default port used for http access is **8080**.

### Endpoints 

* /load - load data into MongoDB.
* /metrics - Expose API metrics using prometheus client.
* /health - Basic status 200 return for health checks.
* / - Get random data from MongoDB.
