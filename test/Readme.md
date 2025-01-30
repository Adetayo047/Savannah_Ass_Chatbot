# Savannah_Ass_Chatbot

![demo](./test/Screenshot 2025-01-30 093015.jpg)

**Run the tests using `pytest`:**

   In the root directory of the project, run the following command to execute the tests:

   ```bash
   pytest test/test_faq.py -v
   ```


## Testing with `pytest`

This project includes unit tests to ensure that all critical functionality is working correctly. The tests are located in the `tests` directory. Some important tests include:

- **`test_extract_contact_info`**: Verifies contact information is correctly extracted from user messages.
- **`test_create_directory`**: Checks that directories are created successfully.
- **`test_chat_function`**: Ensures that the `ChatService` correctly handles user input and returns the expected response.
- **`test_save_contact_info`**: Tests that contact information is saved correctly to a CSV file.

### Mocking and Patching
- We use `unittest.mock` for mocking external API calls (like OpenAI's API) during testing. This ensures that tests run without needing an active internet connection or valid API keys.

### Example Test Output:

Running `pytest` should give you an output similar to the following:

```
================================================== test session starts ===================================================
collected 10 items                                                                                                 

pytest test/test_faq.py -v                                                                        [100%]

================================================== 10 passed in 0.12 seconds ================================================
```

If any tests fail, the output will provide detailed error messages to help you debug the issue.

---
