#!/bin/bash

python -m venv venv
source venv/bin/activate

pip install --upgrade pip

pip install aiohttp

pip install aiomysql

pip freeze > requirements.txt