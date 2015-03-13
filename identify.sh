#!/bin/bash


echo "{username: \"$1\", token: \"QCNct7Qb9JcNkqF\"}" 

curl -i -H "Content-Type: application/json" -X POST -d "{\"username\": \"$1\", \"token\": \"QCNct7Qb9JcNkqF\"}" http://188.166.9.128:9090/create
