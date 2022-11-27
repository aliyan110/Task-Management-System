import json



def write_json(new_data, filename='entries.json'):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        content['Entries'].append(new_data)
        file_data.update(content)
        file.seek(0)
        json.dump(file_data, file, indent = 4)
 
f = open('entries.json', 'r+')
content = json.load(f)

out_file = open('entries2.json', 'w')

print('Welcome to our company!')
print('Please enter your username here to login.')

name = input('Enter name: ')

for c in content:

    for e in content['Entries']:

        if name == e['User name']:
            print('Please enter your password.')
            password = input('Enter password: ')
            if password == e['Password']:
                print('Welcome,', name, 'you are now logged in!')
            else:
                print('Wrong password.')
            break

    else:
        print('Your name is not in the file.')
        print('You need to register.')
        new_name = input('Please enter your name: ')
        new_password = input('Please enter your password: ')
        id = len(content['Entries'])
    
        new_full = {"User name":f"{new_name}",
                        "Password": f"{new_password}",
                        "ID": f"{id + 1}"
                        }

        write_json(new_full)
        print(new_full)
        print('Your name is added in the file.')




