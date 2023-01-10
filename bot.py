import json

# Open and load the bot.json file
with open('bot.json', 'r') as json_file:
    datas = json.load(json_file)

# Print the menu
print('''
1. Melatih bot
2. Berbicara dengan bot
''')

def menu():
    while True:
        # Get user input for the menu
        input_awal = int(input("Masukan kode: "))

        if input_awal == 1:
            while True:
                # Get user input
                X = str(input("User\t: "))

                # If the user wants to exit
                if X == "keluar":
                    break
                else:
                    # Get bot response
                    Y = str(input("Bot\t: "))

                    # Add the new data to the dictionary
                    datas={}
                    datas.update({X:Y})

                    # Write the updated data to the json file
                    with open('bot.json', 'w') as json_file:
                        json.dump(datas, json_file)
        elif input_awal == 2:
            while True:
                X = str(input("User\t: "))
                if X == 'keluar':
                    break
                if X in datas:
                    print(f'Bot\t: {datas[X]}')
                else:
                    print("Bot\t: itu kata baru")
        else:
            # Go back to the menu
            menu()

menu()
