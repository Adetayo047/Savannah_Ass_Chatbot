from utils.utils import create_directory, create_csv_file
from src.chat_service import ChatService
from config.config import USERS_DIRECTORY, CONTACTS_CSV_PATH

class FAQ:
    def __init__(self):
        self.create_required_files()
        self.chat_service = ChatService()

    def create_required_files(self):
        """Create necessary directories and files."""
        create_directory(USERS_DIRECTORY)
        create_csv_file(CONTACTS_CSV_PATH, ['Full_Name', 'Email', 'Phone_Number'])

    def chat_function(self, message, user_id, Full_Name=None, Email=None, Phone_Number=None):
        """Wrapper for chat service function."""
        return self.chat_service.chat_function(message, user_id, Full_Name, Email, Phone_Number)