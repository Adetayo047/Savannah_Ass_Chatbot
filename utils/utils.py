import os
import csv
import json
import logging
from config.config import USERS_DIRECTORY, CONTACTS_CSV_PATH, LOG_LEVEL

# Set up logging
logging.basicConfig(level=getattr(logging, LOG_LEVEL))

def create_directory(directory_path):
    """Create directory if it doesn't exist."""
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

def create_csv_file(file_path, headers):
    """Create CSV file with headers if it doesn't exist."""
    if not os.path.exists(file_path):
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)

def load_conversation_history(user_id):
    """Load conversation history for a user."""
    file_path = os.path.join(USERS_DIRECTORY, f"{user_id}_conversation.json")
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return json.load(file)
    return []

def save_conversation_history(user_id, history):
    """Save conversation history for a user."""
    file_path = os.path.join(USERS_DIRECTORY, f"{user_id}_conversation.json")
    with open(file_path, "w") as file:
        json.dump(history, file)

def save_contact_info(Full_Name, Email, Phone_Number):
    """Save contact information to CSV file."""
    try:
        with open(CONTACTS_CSV_PATH, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([Full_Name, Email, Phone_Number])
        logging.info(f"Contact info for {Full_Name} saved successfully.")
    except Exception as e:
        logging.error(f"Error saving contact info: {e}")
        raise Exception("There was an issue saving your contact information.")
