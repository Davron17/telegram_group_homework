from read_data import read_data as read

def find_number_of_messages(data: dict) -> int:
    """
    Get the total number of messages.

    Parameters:
        data (dict): Dictionary containing the data of the JSON file.
    Returns:
        int: Total number of messages.
    """
    a=data["messages"]
    return len(a)
data = read("result.json")
total_messages = find_number_of_messages(data)
print(total_messages)
