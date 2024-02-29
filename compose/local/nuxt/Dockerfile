FROM node:21.6-alpine3.19

# Set the working directory in the container
WORKDIR /app

ARG LOCAL_APP_PATH=./portfolio

# Copy package.json and package-lock.json (if available)
COPY ${LOCAL_APP_PATH}/package*.json ./

# Install project dependencies
RUN npm install

# # Copy the rest of the application's files into the container
COPY ${LOCAL_APP_PATH}/ .
#
# # Expose port 8080
EXPOSE 3000
#
# # Use the local version of vue-cli-service
CMD ["npm", "run", "dev", "--", "-o"]
# CMD ["tail", "-f", "/dev/null"]
