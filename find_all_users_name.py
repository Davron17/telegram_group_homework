from read_data import read_data as read

def find_all_users_name(data: dict)->list:
    """
    This function will find all the users in the json file and return the list of users name.
 
    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        list: List containing all the users name.
    """
    l=[]
    for i in data["messages"]:
        if "actor" in i and i["actor"] not in l:
            l.append(i["actor"])
    return l


data = read("result.json") 
print(find_all_users_name(data))
    
