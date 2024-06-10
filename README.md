# WHOIS Checker

![GitHub Workflow Status](https://img.shields.io/github/workflow/status/YOUR_USERNAME/YOUR_REPOSITORY/CI)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/YOUR_USERNAME/YOUR_REPOSITORY)
![GitHub](https://img.shields.io/github/license/YOUR_USERNAME/YOUR_REPOSITORY)

A Dockerized WHOIS checker tool that monitors the expiration date of a specified domain and alerts via Discord when it's within a configurable threshold of expiration.

---

## Table of Contents

- [About](#about)
- [Features](#features)
- [Usage](#usage)
  - [Prerequisites](#prerequisites)
  - [Configuration](#configuration)
  - [Running with Docker](#running-with-docker)
- [Contributing](#contributing)
- [License](#license)

---

## About

This tool is designed to help users monitor the expiration date of a domain and receive timely alerts when it's within a configurable threshold of expiration. It leverages the WHOIS protocol to retrieve domain information and sends alerts via Discord webhook integration.

---

## Features

- **Automated Monitoring**: Automatically checks the expiration date of the specified domain at regular intervals.
- **Alert Notifications**: Sends alerts via Discord webhook when the domain is within a configurable threshold of expiration.
- **Flexible Configuration**: Easily configurable via environment variables for domain and Discord webhook URL.

---

## Usage

### Prerequisites

Before running the WHOIS checker tool, ensure you have the following prerequisites installed:

- Docker: [Install Docker](https://docs.docker.com/get-docker/)
- Discord webhook URL: Obtain a Discord webhook URL to receive alert notifications.

### Configuration

Set the following environment variables before running the tool:

- `DOMAIN`: Specify the domain you want to monitor.
- `WEBHOOK_URL`: Provide the Discord webhook URL for receiving alerts.

### Running with Docker

1. Clone the repository:

   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git




---

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests for any improvements or new features you'd like to see. Please make sure to follow the contribution guidelines.

---

## License

This project is licensed under the MIT License.
