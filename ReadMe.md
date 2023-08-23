# Vision Statement Project

This project is built using Django. This README provides guidelines on how to set up and run the project.

## Table of Contents

- [Getting Started](#getting-started)
- [Running the Project](#running-the-project)
  - [Locally](#locally)
  - [Using Docker](#using-docker)
- [Deployment on AWS EC2](#deployment-on-aws-ec2)
- [Integration with Google Forms](#integration-with-google-forms)


## Getting Started

1. **Navigate to the Project Directory**

   Open the directory where the project is located.


```bash
       cd path/to/vision_development
```

2. **Install Dependencies**

Make sure to install all the required packages:

```bash
       pip install -r requirements.txt
```


## Running the Project

### Locally

To run the project locally:
```bash
       python manage.py runserver
```


This will start the development server on the default port, usually `8000`. You can then navigate to `http://127.0.0.1:8000/` in your browser to view the project.

### Using Docker

If you prefer to run the project using Docker:

1. **Install Docker & Docker-Compose**

   If you haven't already, install Docker and Docker-Compose on your machine. You can follow the official installation guides for [Docker](https://docs.docker.com/get-docker/) and [Docker-Compose](https://docs.docker.com/compose/install/).

2. **Run the Project**

   With Docker and Docker-Compose installed, navigate to the project directory and execute:

```bash
       docker-compose up --build
```

This will start the development server at port `5000`. You can then navigate to `http://127.0.0.1:5000/` in your browser to view the project.


## Deployment on AWS EC2

1. **Create an EC2 instance on AWS.**

2. **Transfer the Project to the EC2 Instance.** You can use `scp` or any method you prefer to transfer files to your EC2 instance.

3. **Install Docker and Docker-Compose on the EC2 Instance.**

4. **Create docker image and Run the Project on the EC2 Instance:**

```bash
       docker-compose up --build
```

## Integration with Google Forms

1. **Create a Google Form** that collects the desired person values.

2. **Connect the Google Form to the Public IP Address of the EC2 Instance using Zapier:** Set up a Zap where a form submission in Google Forms triggers a POST request to the Django application.

3. **Handle Form Submissions:** When a person fills and submits the form, the form sends a POST request to the project via Zapier. In response, the project sends a vision statement to the sender's email address based on the provided input from the form.


