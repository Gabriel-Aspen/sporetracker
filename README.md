# Sporetracker

## Docker
For local development run a postgresql docker image in the background

`docker pull postgres`

`docker run --name my_postgres_container -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -d postgres`
