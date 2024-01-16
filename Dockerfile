# Use an official Python runtime as a parent image
FROM alpine:latest

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app


# Run echo hi when the container launches
CMD ["echo", "hi"]
