FROM node:21.6-alpine3.19

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the application's files into the container
COPY ./vuejs-frontend/gs-02-first-app-with-just-js/ .

# Install http-server globally
RUN npm install -g http-server

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Run http-server when the container launches
CMD ["http-server", "-p 8080"]
