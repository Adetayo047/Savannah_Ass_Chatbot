import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# OpenAI API configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# File paths
USERS_DIRECTORY = "./data/USERS"
CONTACTS_CSV_PATH = "./data/user_contacts.csv"

# Logger configuration
LOG_LEVEL = "INFO"