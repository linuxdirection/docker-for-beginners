# Use an official Node.js runtime as a parent image
FROM node:14-alpine

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install any dependencies
RUN npm install

# Bundle app source
COPY . .

# Expose port 3000 for the application
EXPOSE 3000

# Define environment variable
ENV NODE_ENV=production
ENV SERVICE_NAME=myservice
ENV DEBUG=1

# Healthcheck
HEALTHCHECK CMD curl --fail http://localhost:3000 || exit 1 

# Define the command to run the app
CMD ["node", "app.js"]
