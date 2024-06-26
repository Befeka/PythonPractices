
from utils import verify_phone_number, verify_email_address,get_contact_by_name
from storage import read_contacts, write_contacts_file

CONTACT_FILE_PATH = "contacts.json"


def add_contact(contacts):
    """
    """
    first_name = input("First Name: ").lower().strip()
    last_name = input("Last Name: ").lower().strip()
    mobile = input("Mobile Phone Number: ").strip()
    home = input("Home Phone Number: ").strip()
    email = input("Email Address: ").strip()
    address = input("Address : ").strip()
    
    if not first_name or not last_name:
        print("Contacts must have first and last name")
    
    elif mobile and not verify_phone_number(mobile):
        print("Invalid mobile phone number.")
    elif home and not verify_phone_number(home):
        print("Invalid home phone number.")  
                 
    elif not verify_email_address(email):
        print("Invalid email address")
        
    elif get_contact_by_name(first_name,last_name,contacts):
        print("A contact with this name already exists.")
    
    else:
        contact_to_add = {"first_name": first_name,
                          "last_name": last_name,
                          "mobile": mobile,
                          "home":home,
                          "email":email,
                          "address": address
                          }
        contacts.append(contact_to_add)
        print("Contact Added")
        return
    
    print("You entered invalid information, this contact was not added.")
    
def delete_contacts(contacts):
    """_summary_

    Args:
        contacts (_type_): _description_
    """
    first_name = input("First Name: ").lower().strip()
    last_name = input ("Last Name: ").lower().strip()
    
    if not first_name or not last_name:
        print("Contacts must have first and last name")
    
    contact = get_contact_by_name(first_name,last_name,     contacts)
    
    if not contact:
        print("No contact by this name exists!!!!!!")
    else:
        verify = input("Are you sure you would like to delete this contact (y/n)?: ").lower()
        if verify == "y":
            contacts.remove(contact)
            print("Contact deleted")
        
def search_for_contact(contacts):
    
    """Search for contacts by looking firt and last name

    Args:
        contacts (_type_): _description_
        
    """
    first_name_search_string = input("First Name: ").lower().strip()
    last_name_search_string = input ("Last Name: ").lower().strip() 
    
    matching_contacts = []
    
    for contact in contacts:
        first_name = contact["first_name"]
        last_name = contact["last_name"]
        
        if first_name_search_string and  first_name_search_string not in first_name:
            continue
        if last_name_search_string and last_name_search_string not in last_name :
            continue
        matching_contacts.append(contact)
        print(f"Found {len(matching_contacts)} matching contacts.")
        
        list_contacts(matching_contacts)
             
         


def get_contact_string(contact):
    """
    store and returns contact fields in readable way

    Args:
        contact (dictionary): single contact 
    """
    string = f"{contact['first_name'].capitalize()} {contact['last_name'].capitalize()}"
    for field in ["mobile","home","email","address"]:
        value = contact[field]
        if not value:
            continue
        string += f"\n\t{field.capitalize()}: {value}"
    return string
    
def list_contacts(contacts):
    """List all the available contacts in format suitable for reading 

    Args:
        contacts (list): list of contacts stored as json format 
    """
    sorted_contact = sorted(contacts,key=lambda x :x['first_name'])
    
    for i, contact in enumerate(contacts):
        print(f"{i+1} . {get_contact_string(contact)}")

def main(contact_path):
    
    print("Welcome to your contact list!")
    print("The following is a list of usable commands:\n")
    print("\"add\": Adds a contact.")
    print("\"delete\": Deleates a contact.")
    print("\"list\": Lists all contacts.")
    print("\"search\": Searches for a contact by name.")
    print("\"q\": Quits the program and save the contact list.\n")
    
    contacts = read_contacts(contact_path)
    
    while True:
        
        command = input("Type a command: ").lower().strip()
        if command == "q":
            write_contacts_file(contact_path, contacts)
            print("Contacts were saved successfully.")
            break
        elif command == "add":
            add_contact(contacts)
        elif command == "delete":
            delete_contacts(contacts)
        elif command.lower() == "search":
            search_for_contact(contacts)
        elif command == "list":
            list_contacts(contacts)
        else:
            print(f"{command} is not known command!!!!!!!!!!")


if __name__=="__main__":
    main(CONTACT_FILE_PATH)
    
        
    
    

