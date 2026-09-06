prompt = 'Which word do you want a definition for?'

my_glossary = {
    'Python' : 'A programming language',
    'Linux' : 'An operating system',
    'Ruby' : 'Programming Language',
    'function' : 'Reusable block of code',
    'AWS': 'cloud platform'
}

while True:
    for key in my_glossary.keys():
        print(key)

    user_input = input(prompt)

    if user_input:
        print(my_glossary[user_input])
    else:
        break