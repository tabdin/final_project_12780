# Lab Equipment Tracking Application Final

## Overview
This project is a Django-based lab equipment tracking application designed for CMU/ECE-style courses to manage shared hardware such as oscilloscopes, microcontrollers, sensors, and other lab equipment.

The application allows administrators to manage inventory and allows users to check out and return equipment. It also includes a dashboard visualization and data export functionality.

---

## Features
- Equipment inventory management via Django admin
- Equipment checkout and return pages
- Automatic availability tracking
- Dashboard showing active checkouts by equipment type (Chart.js)
- Excel (.xlsx) export of checkout data
- Automated tests using pytest-django
- Dockerized application
- GitHub Actions for testing and Docker builds

---

## Models

### Equipment
- Name
- Equipment type
- Serial number
- Location
- Quantity
- Availability status

### Checkout
- Equipment name and serial number
- Equipment type
- Borrower name and email
- Checkout date
- Due date
- Returned status

---

## Running the Project with Docker

Before starting, **make sure the Docker Desktop application is installed and open**.  
Docker Desktop must be running before building or running the container.

### Prerequisites
- Docker Desktop installed
- Docker Desktop application open and running

---

## Step 1: Clone the Repository

Open a terminal and run:

    git clone <your-repository-url>
    cd <your-repository-name>

---

## Step 2: Build the Docker Image

From the project root (where the Dockerfile is located), run:

    docker build -t equipment-tracker .

This command builds the Docker image for the application.

---

## Step 3: Run the Docker Container

    docker run -p 8000:8000 equipment-tracker

This command:
- Automatically runs database migrations
- Starts the Django development server inside the container

You should see output indicating the server is running at:

    http://0.0.0.0:8000/

---

## Step 4: Access the Application

Once the container is running, open a browser and visit:

- Home page:  
  http://127.0.0.1:8000/

- Checkout page:  
  http://127.0.0.1:8000/checkout/

- Dashboard:  
  http://127.0.0.1:8000/chart/

- Admin interface:  
  http://127.0.0.1:8000/admin/

---

## Creating a Django Superuser (Admin Access)

Because the application runs inside Docker, the admin user must be created inside the running container.

### Step 1: Open the Container Exec Shell

1. Open **Docker Desktop**
2. Go to **Containers**
3. Click on the running `equipment-tracker` container
4. Click **Exec** 

### Step 2: Create the Superuser

From inside the container shell, run:

    python manage.py createsuperuser

Follow the prompts to set:
- Username
- Email 
- Password

### Step 3: Log into Admin

Navigate to:

    http://127.0.0.1:8000/admin/

Log in using the superuser credentials.

From the admin interface, you can:
- Add equipment
- Set equipment types
- Manage availability

---

## Typical Usage Flow

1. Admin logs into /admin/ and adds equipment
2. Users check out available equipment via /checkout/
3. Equipment becomes unavailable automatically
4. Returned equipment becomes available again
5. Dashboard updates to reflect current checkouts
6. Checkout data can be exported as an Excel file

---

## Running Tests

This project uses pytest with pytest-django.

To run tests locally:

    pytest

Tests include:
- Model creation checks
- Page load tests
- Checkout logic validation

---

## CI and Docker

- GitHub Actions runs pytest automatically on push and pull requests
- A separate GitHub Action builds and pushes the Docker image to GHCR

---
