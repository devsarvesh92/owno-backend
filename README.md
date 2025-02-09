# Owno Backend

Owno Backend is a FastAPI-based backend service for managing real estate properties and user interactions. It includes features such as user registration, OTP generation, and property management.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Running Tests](#running-tests)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- User registration with OTP verification
- Real estate property management
- Redis caching for OTP storage
- PostgreSQL database integration

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/owno_backend.git
    cd owno_backend
    ```

2. Install dependencies using PDM:

    ```sh
    pdm install
    ```

3. Set up environment variables:

    Create a  file in the root directory with the following content:

    ```env
    DB_USER=user
    DB_PASSWORD=password
    DB_HOST=localhost
    DB_PORT=5432
    DB_NAME=owno_db
    ```

4. Run database migrations:

    ```sh
    make migrate
    ```

## Usage

1. Start the FastAPI server:

    ```sh
    make run-server
    ```

2. Access the API documentation at `http://localhost:8000/docs`.

## Running Tests

To run the tests, use the following command:

```sh
pytest