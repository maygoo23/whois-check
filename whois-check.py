import whois
from discord_webhook import DiscordWebhook
import schedule
import time
from datetime import datetime, timedelta
import os

# Configuration
DOMAIN = os.environ.get('DOMAIN', '')  # Get domain from environment variable, default to empty string
WEBHOOK_URL = os.environ.get('WEBHOOK_URL', '')  # Get webhook URL from environment variable, default to empty string

# Last expiration date checked
last_expiry_date = None

def log_message(message):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{timestamp}] {message}")

def check_domain():
    global last_expiry_date

    if DOMAIN:
        try:
            log_message(f"Checking WHOIS information for domain: {DOMAIN}")
            domain_info = whois.whois(DOMAIN)
            expiry_date = domain_info.expiration_date

            log_message(f"WHOIS information retrieved: {domain_info}")

            if isinstance(expiry_date, list):
                expiry_date = expiry_date[0]

            if expiry_date:
                now = datetime.now()

                # Check if the expiration date has changed
                if expiry_date != last_expiry_date:
                    send_alert(f"Domain {DOMAIN} expiration date has changed to {expiry_date}")
                    last_expiry_date = expiry_date

                # Check if we are within 7 days of expiration
                if (expiry_date - now).days <= 7:
                    send_alert(f"Domain {DOMAIN} is expiring soon! Expiry date: {expiry_date}")

            else:
                log_message(f"Could not find expiry date for domain {DOMAIN}")

        except Exception as e:
            log_message(f"Error checking domain {DOMAIN}: {e}")
    else:
        log_message("No domain specified. Please provide a domain.")

def send_alert(message):
    if WEBHOOK_URL:
        log_message(f"Sending alert: {message}")
        webhook = DiscordWebhook(url=WEBHOOK_URL, content=message)
        response = webhook.execute()
        log_message(f"Alert sent. Response status: {response.status_code}")
    else:
        log_message("No webhook URL specified. Please provide a webhook URL.")

if __name__ == "__main__":
    # Announce that the script is starting up
    send_alert(f"Starting up WHOIS checker for domain {DOMAIN}")

    # Perform an initial WHOIS check
    check_domain()

    # Schedule the job every 8 hours
    schedule.every(8).hours.do(check_domain)

    while True:
        schedule.run_pending()
        time.sleep(1)
