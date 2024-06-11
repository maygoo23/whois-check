# WHOIS Domain Expiry Checker

![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/maygoo23/whois-check/docker-publish.yml?branch=main)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/maygoo23/whois-check)
![GitHub](https://img.shields.io/github/license/maygoo23/whois-check)
![GitHub Commits](https://img.shields.io/github/commit-activity/t/maygoo23/whois-check)
![GitHub Downloads](https://img.shields.io/github/downloads/maygoo23/whois-check/total)

This project is a simple WHOIS domain expiry checker. It periodically checks the expiry date of a specified domain and sends alerts via a Discord webhook if the expiration date changes or is nearing.

---

## Table of Contents

- [About](#about)
- [How It Works](#how-it-works)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

---

## About

This tool is designed to help users monitor the expiration date of a domain and receive timely alerts when it's within a configurable threshold of expiration. It leverages the WHOIS protocol to retrieve domain information and sends alerts via Discord webhook integration.

---

## How It Works

- The script retrieves the WHOIS information for the specified domain.
- It checks if the expiration date of the domain has changed or is within 7 days of expiration.
- If either condition is met, an alert is sent to the specified Discord webhook.

---

## Usage

### Prerequisites

Before running the WHOIS checker tool, ensure you have the following prerequisites installed:

- Docker: [Install Docker](https://docs.docker.com/get-docker/)
- Discord webhook URL: Obtain a Discord webhook URL to receive alert notifications.

### Configuration

Set the following environment variables in the `docker-compose.yml` file or the `.env` file before starting the container:

- `DOMAIN`: Specify the domain you want to monitor.
- `WEBHOOK_URL`: Provide the Discord webhook URL for receiving alerts.

### Running with Docker-Compose

```yaml
services:
  whois-check:
    image: ghcr.io/maygoo23/whois-check:latest
    container_name: whois-check
    environment:
      - DOMAIN=${DOMAIN}
      - WEBHOOK_URL=${WEBHOOK_URL}
    restart: unless-stopped
```

---

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests for any improvements or new features you'd like to see. Please make sure to follow the contribution guidelines.

---

## License

This project is licensed under the MIT License.
