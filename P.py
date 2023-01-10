import json
a = open('D.json')
data = json.load(a)

print('''
1.melatih bot
2.berbicara dengan bot
''')

while True:
  input_awal = int(input("masukan kode: "))
  if input_awal == 1:
    while True:
      X = str(input("User\t: "))
      if X == "keluar":
         break
      else:
        Y = str(input("Bot\t: "))
        data[X] = Y
        b = open('bot.json', "w")
        json.dump(data,b)
        b.close()
        
  elif input_awal == 2:
    while True:
      X = str(input("User\t: "))
      if X == 'keluar':
        break
      if X in data:
        print(f'Bot\t: {data[X]}')
      else:
        print("Bot\t: itu kata baru")
  else:
    pass