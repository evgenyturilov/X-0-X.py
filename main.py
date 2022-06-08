from random import randint

field = [
          [' ', '1', '2', '3'],
          ['1', '-', '-', '-'],
          ['2', '-', '-', '-'],
          ['3', '-', '-', '-']
        ]
count = 0

def print_game_field(field):
  print()
  for i in range(len(field)):
    for j in range(len(field[i])):
      print(field[i][j], end = ' ')
    print()

def user_X_input():
  print('\nГде вы хотите поставить X?\n')
  x = int(input('   Введите позицию по оси X (от 1 до 3): '))
  y = int(input('   Введите позицию по оси Y (от 1 до 3): '))
  if x in (1,2,3) and y in (1,2,3):
    for i in range(len(field)):
      for j in range(len(field[i])):
        str = field[x][y]
    if str == '-':
      field[x][y] = 'X'
    else:
      print('\nПоле занято, введите другие значения!')
      return user_X_input()
    return field
  else:
    print('Введены некорректные данные')
    return user_X_input()
  

def user_0_input():
  print('\nГде вы хотите поставить 0?\n')
  x = int(input('   Введите позицию по оси X (от 1 до 3): '))
  y = int(input('   Введите позицию по оси Y (от 1 до 3): '))
  if x in (1,2,3) and y in (1,2,3):
    for i in range(len(field)):
      for j in range(len(field[i])):
        str = field[x][y]
    if str == '-':
      field[x][y] = '0'
    else:
      print('\nПоле занято, введите другие значения!')
      return user_0_input()
    return field
  else:
    print('Введены некорректные данные')
    return user_0_input()

def computer_X_input():
  x = randint(1,3)
  y = randint(1,3)
  for i in range(len(field)):
    for j in range(len(field[i])):
      str = field[x][y]
  if str == '-':
    field[x][y] = 'X'
  else:
    return computer_X_input()
  return field

def computer_0_input():
  x = randint(1,3)
  y = randint(1,3)
  for i in range(len(field)):
    for j in range(len(field[i])):
      str = field[x][y]
  if str == '-':
    field[x][y] = '0'
  else:
    return computer_X_input()
  return field

def check_X(field):
  for i in range(len(field)):
      for j in range(len(field[i])):
        if ((field[1][1] == 'X' and field[1][2] == 'X' and field[1][3] == 'X') or
            (field[2][1] == 'X' and field[2][2] == 'X' and field[2][3] == 'X') or
            (field[3][1] == 'X' and field[3][2] == 'X' and field[3][3] == 'X') or
            (field[1][1] == 'X' and field[2][1] == 'X' and field[3][1] == 'X') or
            (field[1][2] == 'X' and field[2][2] == 'X' and field[3][2] == 'X') or
            (field[1][3] == 'X' and field[2][3] == 'X' and field[3][3] == 'X') or
            (field[1][1] == 'X' and field[2][2] == 'X' and field[3][3] == 'X') or
            (field[3][1] == 'X' and field[2][2] == 'X' and field[3][1] == 'X')):
              print('\nПобедил игрок X!')
              exit('\nИгра окончена!')
        else:
          continue
def check_0(field):
  for i in range(len(field)):
      for j in range(len(field[i])):
        if ((field[1][1] == '0' and field[1][2] == '0' and field[1][3] == '0') or
            (field[2][1] == '0' and field[2][2] == '0' and field[2][3] == '0') or
            (field[3][1] == '0' and field[3][2] == '0' and field[3][3] == '0') or
            (field[1][1] == '0' and field[2][1] == '0' and field[3][1] == '0') or
            (field[1][2] == '0' and field[2][2] == '0' and field[3][2] == '0') or
            (field[1][3] == '0' and field[2][3] == '0' and field[3][3] == '0') or
            (field[1][1] == '0' and field[2][2] == '0' and field[3][3] == '0') or
            (field[3][1] == '0' and field[2][2] == '0' and field[3][1] == '0')):
              print('\nПобедил игрок 0!')
              exit('\nИгра окончена!')
        else:
          continue


def settings():
  sett = input('\nПротив кого вы хотите играть?\n  Человек - 1\n  Компьютер - 2\n  Выйти из игры - 3\n')
  if sett == '1' or sett == '2':
    return sett
  elif sett == '3':
    exit('До скорой встречи!')
  else:
    print('Некорректный ввод!')
    return settings()



def game(field, count, sett):
  if sett == '1':
    while count < 9:
      user_X_input()
      count += 1
      check_X(field)
      print_game_field(field)
      print(f'\nЧисло ходов: {count}')
      user_0_input()
      count += 1
      check_0(field)
      print_game_field(field)
      print(f'\nЧисло ходов: {count}')
      return game(field, count, sett)
    else:
      print('Нет свободных полей! Ничья!')
      exit('Игра окончена!')
  elif sett == '2':
    while count < 9:
      user_X_input()
      count += 1
      check_X(field)
      print_game_field(field)
      print(f'\nЧисло ходов: {count}')
      computer_0_input()
      count += 1
      check_0(field)
      print_game_field(field)
      print(f'\nЧисло ходов: {count}')
      return game(field, count, sett)
  else:
    print('Нет свободных полей! Ничья!')
    exit('Игра окончена!')
  

sett = settings()
print_game_field(field)
game(field, count, sett)