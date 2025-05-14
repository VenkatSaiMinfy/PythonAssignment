def add_contact(contacts, name, **details):
    if name not in contacts:
        contacts[name] = {}
    contacts[name].update(details)

contacts = {}
n = int(input("Enter the number of contacts: "))

for _ in range(n):
    name = input("Enter the contact name: ")
    details = {}
    
    while True:
        field = input("Enter detail field (or 'done' to stop): ")
        if field == 'done':
            break
        value = input(f"Enter {field}: ")
        details[field] = value
    
    add_contact(contacts, name, **details)

print(contacts)
