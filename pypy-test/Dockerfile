FROM 10.160.32.188:8079/pypy:3-5.8

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Run python's package manager and install the flask package
RUN pip install -r requirements.txt --index-url http://10.160.32.188:8082/repository/pypi-proxy/simple --trusted-host 10.160.32.188

# Configure ports
EXPOSE 80

# start scripts

# supervisor config

# Run the chmod command to change permissions on above file in the /bin directory
RUN chmod 755 /app/run.sh
RUN chmod 755 /app/run_fastapi.sh
# Default environmental variables

# run commands in supervisor
#CMD ["bash", "/app/run.sh"]
CMD ["bash", "/app/run_fastapi.sh"]

