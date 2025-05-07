# Use the official Python image
FROM python:3.12.8

# Set the working directory
WORKDIR /microhub-gateway

# This command put requirements.txt in container in specific directory
COPY ./requirements.txt /microhub-gateway/requirements.txt

# This command will install dependancies in docker container
RUN pip install --no-cache-dir --upgrade -r /microhub-gateway/requirements.txt

# copy source code files and directory in docker container
COPY ./app /microhub-gateway/app

# this is default command. It will run after container start
# production
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]
# development
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000","--reload"]
