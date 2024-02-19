FROM node:21.6-alpine3.19

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json (if available)
COPY ./my-nuxt-app/package*.json ./

# Install project dependencies
RUN npm install

# # Copy the rest of the application's files into the container
COPY ./my-nuxt-app/ .
#
# # Expose port 8080
EXPOSE 3000
#
# # Use the local version of vue-cli-service
# npm run dev -- -o
CMD ["npm", "run", "dev", "--", "-o"]

