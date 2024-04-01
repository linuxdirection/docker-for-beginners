# Use an official Node runtime as a parent image
FROM node:14

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in package.json
RUN npm install

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV NODE_ENV=production

# Run index.js when the container launches
CMD ["node", "index.js"]
