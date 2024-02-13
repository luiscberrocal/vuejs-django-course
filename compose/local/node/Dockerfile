FROM node:21.6-alpine3.19

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy package.json and package-lock.json (if available)
COPY ./vuejs-frontend/src/package*.json ./

# Install project dependencies
RUN npm install

# # Copy the rest of the application's files into the container
COPY ./vuejs-frontend/ .
#
# # Expose port 8080
EXPOSE 8080
#
# # Use the local version of vue-cli-service
CMD ["npx", "vue-cli-service", "serve"]

