import openai
from config.config import OPENAI_API_KEY
from src.system_prompt import generate_system_prompt
from utils.utils import load_conversation_history, save_conversation_history, save_contact_info
from utils.contact_parser import extract_contact_info

openai.api_key = OPENAI_API_KEY

class ChatService:
    def chat_function(self, message, user_id, Full_Name=None, Email=None, Phone_Number=None):
        """Handle chat interactions with the user."""
        history = load_conversation_history(user_id)
        system_prompt = generate_system_prompt(Full_Name, Email, Phone_Number)

        history.append({"role": "user", "content": message})
        messages = [{"role": "system", "content": system_prompt}] + history

        try:
            response = openai.ChatCompletion.create(
                messages=messages,
                model="gpt-4o",
            )
            assistant_message = response.choices[0].message.content

            contact_info = extract_contact_info(message)
            Full_Name = contact_info['Full_Name']
            Email = contact_info['Email']
            Phone_Number = contact_info['Phone_Number']

            if all(contact_info.values()):
                save_contact_info(Full_Name, Email, Phone_Number)
                assistant_message += "\n\nYour contact information has been saved. A representative will reach out to you shortly."

            if "human representative" in assistant_message.lower() and not all(contact_info.values()):
                assistant_message += "\n\nPlease provide your full name, email, and phone number to connect with a representative."

            history.append({"role": "assistant", "content": assistant_message})
            save_conversation_history(user_id, history)

            return assistant_message

        except Exception as e:
            print(f"Error during OpenAI API call: {e}")
            return "I'm sorry, but I encountered an error while processing your request."



