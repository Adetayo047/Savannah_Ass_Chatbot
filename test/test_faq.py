import pytest
import os
import csv
import json
from unittest.mock import Mock, patch
from src.faq import FAQ
from src.chat_service import ChatService
from utils.contact_parser import extract_contact_info
from utils.utils import (
    create_directory,
    create_csv_file,
    load_conversation_history,
    save_conversation_history,
    save_contact_info
)

# Test fixtures
@pytest.fixture
def test_directory(tmp_path):
    """Create a temporary directory for testing."""
    return str(tmp_path)

@pytest.fixture
def mock_openai():
    """Mock OpenAI API responses."""
    with patch('openai.ChatCompletion.create') as mock:
        mock.return_value.choices = [
            Mock(message=Mock(content="This is a test response"))
        ]
        yield mock

@pytest.fixture
def chat_service():
    """Create a ChatService instance."""
    return ChatService()

@pytest.fixture
def test_csv_path(test_directory):
    """Create a test CSV file path."""
    return os.path.join(test_directory, 'contacts.csv')

@pytest.fixture
def faq_instance(test_directory, test_csv_path):
    """Create an FAQ instance with temporary directory."""
    with patch('src.faq.USERS_DIRECTORY', test_directory), \
         patch('src.faq.CONTACTS_CSV_PATH', test_csv_path), \
         patch('utils.utils.CONTACTS_CSV_PATH', test_csv_path), \
         patch('config.config.USERS_DIRECTORY', test_directory), \
         patch('config.config.CONTACTS_CSV_PATH', test_csv_path):
        faq = FAQ()
        yield faq

# Test Contact Parser
def test_extract_contact_info():
    """Test contact information extraction from messages."""
    test_message = """
    Full Name: John Doe
    Email: john@example.com
    Phone Number: 123-456-7890
    """
    result = extract_contact_info(test_message)
    
    assert result['Full_Name'] == 'John Doe'
    assert result['Email'] == 'john@example.com'
    assert result['Phone_Number'] == '123-456-7890'

def test_extract_contact_info_different_formats():
    """Test contact extraction with various format variations."""
    test_messages = [
        "fullname: Jane Doe, email: jane@example.com, phone: 987-654-3210",
        "Full_Name: Bob Smith\nEmail_Address: bob@example.com\nPhone_Number: 555-0123",
    ]
    
    for message in test_messages:
        result = extract_contact_info(message)
        assert all(value is not None for value in result.values())

# Test File Operations
def test_create_directory(test_directory):
    """Test directory creation."""
    new_dir = os.path.join(test_directory, 'test_dir')
    create_directory(new_dir)
    assert os.path.exists(new_dir)

def test_create_csv_file(test_directory):
    """Test CSV file creation with headers."""
    csv_path = os.path.join(test_directory, 'test.csv')
    headers = ['Header1', 'Header2']
    create_csv_file(csv_path, headers)
    
    assert os.path.exists(csv_path)
    with open(csv_path, 'r', newline='') as file:
        reader = csv.reader(file)
        assert next(reader) == headers

def test_conversation_history(test_directory):
    """Test saving and loading conversation history."""
    user_id = "test_user"
    history = [
        {"role": "user", "content": "Hello"},
        {"role": "assistant", "content": "Hi there"}
    ]
    
    with patch('config.config.USERS_DIRECTORY', test_directory):
        save_conversation_history(user_id, history)
        loaded_history = load_conversation_history(user_id)
        assert loaded_history == history

def test_save_contact_info(test_directory, test_csv_path):
    """Test saving contact information to CSV."""
    with patch('utils.utils.CONTACTS_CSV_PATH', test_csv_path):
        # First create the CSV file with headers
        create_csv_file(test_csv_path, ['Full_Name', 'Email', 'Phone_Number'])
        
        # Then save the contact info
        save_contact_info('Test User', 'test@example.com', '123-456-7890')
        
        # Verify the file exists and contains the correct data
        assert os.path.exists(test_csv_path)
        with open(test_csv_path, 'r', newline='') as file:
            rows = list(csv.reader(file))
            assert len(rows) == 2  # Headers + 1 data row
            assert rows[0] == ['Full_Name', 'Email', 'Phone_Number']
            assert rows[1] == ['Test User', 'test@example.com', '123-456-7890']

# Test Chat Service
def test_chat_function(mock_openai, chat_service, test_directory):
    """Test the main chat function."""
    with patch('config.config.USERS_DIRECTORY', test_directory):
        response = chat_service.chat_function(
            "Hello, I need help",
            "test_user",
            "Test User",
            "test@example.com",
            "123-456-7890"
        )
        assert response == "This is a test response"

def test_chat_service_with_contact_info(mock_openai, chat_service, test_directory, test_csv_path):
    """Test chat service when contact information is provided."""
    message = """
    Full Name: Test User
    Email: test@example.com
    Phone Number: 123-456-7890
    I need to speak with a representative
    """
    
    with patch('config.config.USERS_DIRECTORY', test_directory), \
         patch('utils.utils.CONTACTS_CSV_PATH', test_csv_path):
        create_csv_file(test_csv_path, ['Full_Name', 'Email', 'Phone_Number'])
        response = chat_service.chat_function(message, "test_user")
        assert "contact information has been saved" in response.lower()

def test_chat_service_error_handling(chat_service):
    """Test chat service error handling."""
    with patch('openai.ChatCompletion.create', side_effect=Exception("API Error")):
        response = chat_service.chat_function("Hello", "test_user")
        assert "error" in response.lower()

# Test FAQ Class
def test_faq_initialization(test_directory, test_csv_path):
    """Test FAQ class initialization and file creation."""
    with patch('src.faq.USERS_DIRECTORY', test_directory), \
         patch('src.faq.CONTACTS_CSV_PATH', test_csv_path), \
         patch('utils.utils.CONTACTS_CSV_PATH', test_csv_path):
        faq = FAQ()
        assert os.path.exists(test_directory)
        # Create the CSV file first
        create_csv_file(test_csv_path, ['Full_Name', 'Email', 'Phone_Number'])
        assert os.path.exists(test_csv_path)

def test_faq_chat_function(faq_instance, mock_openai):
    """Test FAQ chat function wrapper."""
    response = faq_instance.chat_function(
        "Hello",
        "test_user",
        "Test User",
        "test@example.com",
        "123-456-7890"
    )
    assert response == "This is a test response"
