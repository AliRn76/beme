#! /bin/bash

cd beme-backend
git pull origin master
docker compose build backend
docker compose down backend
docker compose up backend -d