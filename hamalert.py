import argparse
import telnetlib
import json
import requests
import logging

# Replace with your HamAlert username and password
HAMALERT_USERNAME = "USERNAME"
HAMALERT_PASSWORD = "PASSWORD"

# Replace with your Discord webhook URL
DISCORD_WEBHOOK_URL = "INSERT DISCORD WEBHOOK HERE"

def send_discord_webhook(content):
    data = {"content": content}
    headers = {"Content-Type": "application/json"}
    response = requests.post(DISCORD_WEBHOOK_URL, json=data, headers=headers)
    if response.status_code == 204:
        logging.info("Discord webhook sent successfully.")
    else:
        logging.error("Failed to send Discord webhook. Status code:", response.status_code)

def telnet_listener(host, port, username, password):
    try:
        with telnetlib.Telnet(host, port) as tn:
            tn.read_until(b"login: ")
            tn.write(username.encode("utf-8") + b"\n")
            tn.read_until(b"password: ")
            tn.write(password.encode("utf-8") + b"\n")

            while True:
                data = tn.read_until(b"\n").decode("utf-8").strip()
                logging.info("Received data:", data)

                # Split the received data into separate pieces
                pieces = data.split()

                # Ensure that the data has enough pieces to extract relevant information
                if len(pieces) >= 5 and pieces[1] == "de":
                    source_call = pieces[2].strip(':')
                    destination_call = pieces[3]
                    frequency = pieces[4]
                    timestamp = pieces[-1]

                    # Construct the message for Discord webhook
                    message = f"DX de {source_call} @ {timestamp}\n"
                    message += f"{frequency} on {destination_call}"

                    send_discord_webhook(message)
                else:
                    logging.warning("Received data is not in the expected format. Skipping.")
                    logging.warning("Number of pieces:", len(pieces))
                    logging.info("Received data:", pieces)

    except ConnectionRefusedError:
        logging.error("Telnet connection refused. Make sure the server is running and reachable.")
    except Exception as e:
        logging.error("An error occurred:", e)

def setup_args():
    # Create an argument parser
    parser = argparse.ArgumentParser()

    # Add an argument for the logging level
    parser.add_argument('-l', '--log-level', help='The logging level', choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'])

    # Parse the arguments
    args = parser.parse_args()

    # Set the logging level
    logging.basicConfig(level=args.log_level)

if __name__ == "__main__":
    # HAM ALERT TELNET INFORMATION
    HOST = "hamalert.org"
    PORT = 7300

    setup_args()
    telnet_listener(HOST, PORT, HAMALERT_USERNAME, HAMALERT_PASSWORD)
