# basic python image slim is lighter
FROM python:3.9-slim

# set the working directory in the image
WORKDIR /app

# copy the requirements.txt file to the working directory
COPY requirements.txt .

# install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# copy the remaining project files (app.py) to the image
COPY . .

# define the default command to run the application
CMD ["python", "app.py"]