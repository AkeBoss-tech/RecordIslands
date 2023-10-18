import os

current = input("Enter the household you are on right now\n> ")

# Load households from households.txt
households = []
with open(os.path.join(os.path.dirname(__file__), 'houses.txt'), 'r') as f:
    households = f.read().split('\n')

# get index of current household
current_index = households.index(current)
if current_index == -1:
    print("Household not found")
    current_index = 0

def search_text_between(text, start, end):
    start_index = text.find(start)
    if start_index != -1:
        rest = text[start_index + len(start):]
        return rest[:rest.find(end)]
    return None

while input("Copy paste text to person.txt then press enter otherwise exit\n> ") != 'exit':
    # Read the contents of person.txt
    contents = None
    with open(os.path.join(os.path.dirname(__file__), 'person.txt'), 'r') as f:
        contents = f.read()

    # Search the text for Logout and get the text between it and \n
    name = search_text_between(contents, 'Logout', '\n')
    occupation = search_text_between(contents, 'old\n', '\n$')
    if occupation.count('\n') > 1:
        occupation = "None"
    money = search_text_between(contents, '$', '\n')

    # Count instances of Friends, Unemployment, Graduated, No longer friends, Dating
    friends = contents.count('Friends')
    lost_friends = contents.count('No longer friends')
    unemployment = contents.count('Unemploy')
    graduated = contents.count('Graduated')
    dating = contents.count('Dating')
    vacation = contents.count('Vacation')
    hospital_admission = contents.count('admission')

    store_string = f"{households[current_index]} - {name} - {occupation} - {money} - {friends} - {lost_friends} - {unemployment} - {graduated} - {dating} - {vacation} - {hospital_admission} \n"
    # append to data file
    with open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'a') as f:
        f.write(store_string)

    print("Storing String")
    print(store_string)
    print(f"The next person is {households[current_index + 1]}")
    current_index += 1

