from read_data import read_data 
from find_all_users_id import find_all_users_id

def find_user_message_count(data: dict, user_ids: list) -> dict:
    """
    This function will find the user's message count.

    Parameters:
        data (dict): Dictionary containing the data of the JSON file
        user_ids (list): User IDs of the users (as a list)
    Returns:
        dict: Number of messages for each user
    """

    message_count = {}

    for message in data['messages']:
        if message['user_id'] in user_ids:
            user_id = message['user_id']
            if user_id in message:
                message[user_id] += 1
            else:
                message[user_id] = 1

    return message

data = get("result.json")