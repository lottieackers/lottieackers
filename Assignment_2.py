

#User inputs their name 
user_name = input('What is your name?')

#User chooses an animal which assigns them to a Hogwarts house using an if/elif statement
personality = input('Please choose an animal: Snake, Owl, Badger, Eagle')

user_house = ''

if personality.lower() == 'snake':
    user_house = 'Slytherin'
elif personality.lower() == 'owl':
    user_house = 'Ravenclaw'
elif personality.lower() == 'badger':
    user_house = 'Hufflepuff'
elif personality.lower() == 'eagle':
    user_house = 'Gryffindor'
    

#Uses input data to generate a welcome message
welcome_message = 'Welcome to Hogwarts {}.\nYou have been accepted into {} house.'.format(user_name.title(), user_house)

print(welcome_message)


#List which stores a student from each Hogwarts house 
students = ['Draco', 'Luna', 'Cedric', 'Ron']



#If/elif statement which assigns the correct buddy for the corresponding user house
buddy = ''


if user_house == 'Slytherin':
    buddy = students[0]
elif user_house == 'Ravenclaw':
    buddy = students[1]
elif user_house == 'Hufflepuff':
    buddy = students[2]
elif user_house == 'Gryffindor':
     buddy = students[3]


#Message which explains the buddy that has been assigned to the user.
buddy_message = 'A buddy from {} has been assigned to you. They are called {}.'.format(user_house, buddy)

print(buddy_message)


#Harry Potter API (free, no key required) accessed to get attribute data for the buddies to help user identify. 
import requests

buddy_api = ''

if buddy == 'Draco':
    buddy_api = 'draco-malfoy'
elif buddy == 'Luna':
    buddy_api = 'luna-lovegood'
elif buddy == 'Cedric':
    buddy_api = 'cedric-diggory'
elif buddy == 'Ron':
    buddy_api = 'ronald-weasley'

endpoint = 'https://api.potterdb.com/v1/characters/{}/'.format(buddy_api)

response = requests.get(endpoint)


hp = response.json()

buddy_hair = hp['data']['attributes']['hair_color'].lower()
buddy_eyes = hp['data']['attributes']['eye_color'].lower()


buddy_attributes = f"Look out for your buddy when you arrive! They have {buddy_hair} hair and {buddy_eyes} eyes. They will help show you to the {user_house} common room."

print(buddy_attributes)


#Generate the cost of robes which is dependent on the height of the user (larger person = more fabric = more expensive!)
height = int(input('What is your height in cm?'))

def robes(height):
    if height <= 140:
        return height * 0.25
    elif height <= 160:
        return height * 0.275
    elif height <= 180:
        return height * 0.3
    elif height >=180:
        return height * 0.325

robe_cost = '{:.2f}'.format(robes(height))

#Random module imported to generate a random dorm room to be assigned to user.
import random

dorm_rooms = [1, 2, 3, 4]

user_dorm = random.choice(dorm_rooms)

#Generates a message informing user which dorm they have been assigned and how much their robes will cost. 
dorm_message = f"You have been assigned to dorm room number {user_dorm} where you will find your school robes. They are at a cost of £{robe_cost}."

print(dorm_message)

#Generates a password for the dorm room unique to the user's house using string slicing (Palindrome for Slytherin, every other letter for Ravenclaw, middle letters for Hufflepuff and every letter but first and last for Gryffindor.)
dorm_password = ''

if user_house == 'Slytherin':
    dorm_password = (user_house[::-1].lower())
elif user_house == 'Ravenclaw':
    dorm_password = (user_house[0:9:2].lower())
elif user_house == 'Hufflepuff':
    dorm_password = user_house[3:7]
elif user_house == 'Gryffindor':
    dorm_password = user_house[1:-1]

print(dorm_password)



#List of subjects and cost of subject books in a dictionary
first_books = {
    'Dark Arts': 15.80, 
    'Herbology': 12.30,
    'Charms': 21.50,
    'Potions': 28.20,
}

#For loop to calcualate the total cost of books 
books_cost = 0
for price in first_books.values():
    books_cost = books_cost + price
 
#Formats output to 2dp
books_cost_2dp = '{:.2f}'.format(books_cost)


#Output of keys from dicitonary written as a string, each one separated by commas 
book_string = ', '.join(map(str, first_books.keys()))

print(book_string)

#Generates messages about the subjects that will be studied and total cost of books. 
books_message = f'The subjects you will be studying this year are: {book_string}. Books required for these subjects are at a total cost of £{books_cost_2dp}.'
bursar_message = 'Both robes and books are to be paid to the school bursar by the 31st August.'

#Variable for headteacher. Able to be changes in case of changes of staff. 
headteacher = 'Albus Dumbledore'

#Writes a Hogwarts letter to the user with all the relevant information for their 1st September start. 
with open('hogwarts_letter.txt', 'w') as file:
    file.write(welcome_message + '\n')
    file.write('' + '\n')
    file.write(buddy_message + '\n')
    file.write(buddy_attributes + '\n')
    file.write(dorm_message + '\n')
    file.write(books_message + '\n')
    file.write(bursar_message + '\n')
    file.write('' + '\n')
    file.write('We look forward to seeing you on the 1st September.' + '\n')
    file.write('' + '\n')
    file.write('Yours magically,' + '\n')
    file.write(headteacher + "\n")
    file.write('' + '\n')
    file.write('PS. Your common room password is: ' + dorm_password)


   






  

    


