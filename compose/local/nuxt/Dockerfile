FROM node:21.6-alpine3.19

RUN mkdir -p /usr/src/app
# Set the working directory in the container
WORKDIR /usr/src/app

ARG LOCAL_APP_PATH=./finance-tracker
RUN apk update && apk upgrade
# Copy package.json and package-lock.json (if available)
COPY ${LOCAL_APP_PATH}/package*.json ./

# Copy the rest of the application's files into the container
COPY ${LOCAL_APP_PATH}/ .

RUN npm config delete proxy
RUN npm config delete http-proxy
RUN npm config delete https-proxy

# Install project dependencies
RUN npm install

RUN npm run build

# # Expose port 8080
EXPOSE 3000
#
# # Use the local version of vue-cli-service
CMD ["npm", "run", "dev", "--", "-o"]
# CMD ["tail", "-f", "/dev/null"]
