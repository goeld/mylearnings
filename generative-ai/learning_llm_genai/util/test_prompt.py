import os
from unittest.mock import Mock

import pytest

from prompt import get_chat_response

def test_get_chat_response():
    # Mock the client and its chat.completions.create method
    client = Mock()
    client.chat.completions.create.return_value = Mock(choices=[Mock(message=Mock(content="Assistant response"))])

    # Set the environment variable
    os.environ['MODEL_NAME'] = 'gpt-3.5-turbo'

    # Call the function with a user message
    user_message = "Hello, how can I help you?"
    response = get_chat_response(user_message)

    # Assert that the client's chat.completions.create method was called with the correct arguments
    client.chat.completions.create.assert_called_once_with(
        model='gpt-3.5-turbo',
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message},
        ],
    )

    # Assert that the response is the content of the first choice
    assert response == "Assistant response"

    # Reset the environment variable
    os.environ.pop('MODEL_NAME')

if __name__ == "__main__":
    pytest.main()