import json

def read_contacts(file_path):
    """
    Function to display contact lists from json load 
    Return contact list if exist in the file else empty 

    Args:
        file_path (_type_): json file path
    """
    
    try:
        with open(file_path,"r") as f:
            contacts = json.load(f)["contacts"]
            
    except FileNotFoundError:
        contacts = []
        
    return contacts
def write_contacts_file(file_path,contacts):
    """_summary_

    Args:
        file_path (_type_): _description_
        contacts (_type): _description
    """
    with open(file_path,"w") as f:
        contacts = {"contacts" : contacts}
        json.dump(contacts,f)
        
