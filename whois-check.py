import whois
from discord_webhook import DiscordWebhook
import schedule
import time
from datetime import datetime
import os

# Configuration
# Get domain from environment variable, default to empty string
DOMAIN = os.environ.get('DOMAIN', '')
# Get webhook URL from environment variable, default to empty string
WEBHOOK_URL = os.environ.get('WEBHOOK_URL', '')


def check_domain():
    if DOMAIN:
        try:
            print(f"Checking WHOIS information for domain: {DOMAIN}")
            domain_info = whois.whois(DOMAIN)
            expiry_date = domain_info.expiration_date

            print(f"WHOIS information retrieved: {domain_info}")

            if isinstance(expiry_date, list):
                expiry_date = expiry_date[0]

            if expiry_date:
                now = datetime.now()
                if expiry_date < now:
                    send_alert(f"Domain {DOMAIN} has expired!")
                else:
                    print(f"Domain {DOMAIN} is not expired. Expiry date: {expiry_date}")
            else:
                print(f"Could not find expiry date for domain {DOMAIN}")

        except Exception as e:
            print(f"Error checking domain {DOMAIN}: {e}")
    else:
        print("No domain specified. Please provide a domain.")


def send_alert(message):
    if WEBHOOK_URL:
        print(f"Sending alert: {message}")
        webhook = DiscordWebhook(url=WEBHOOK_URL, content=message)
        response = webhook.execute()
        print(f"Alert sent. Response status: {response.status_code}")
    else:
        print("No webhook URL specified. Please provide a webhook URL.")


if __name__ == "__main__":
    # Announce that the script is starting up
    send_alert(f"Starting up WHOIS checker for domain {DOMAIN}")

    # Perform an initial WHOIS check
    check_domain()

    # Schedule the job every 30 minutes
    schedule.every(30).minutes.do(check_domain)

    while True:
        schedule.run_pending()
        time.sleep(1)
