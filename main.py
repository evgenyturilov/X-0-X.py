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
        if field[x][y] != '0':
          field[x][y] = 'X'
        else:
          print('\nПоле занято, введите другие значения!')
          return user_0_input()
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
        if field[x][y] != 'X':
          field[x][y] = '0'
        else:
          print('\nПоле занято, введите другие значения!')
          return user_0_input()
    return field
  else:
    print('Введены некорректные данные')
    return user_0_input()

def game(field, count):
  while count < 9:
    user_X_input()
    print_game_field(field)
    count += 1
    print(f'Число ходов: {count}')
    user_0_input()
    print_game_field(field)
    count += 1
    print(f'Число ходов: {count}')
    return game(field, count)
  else:
    print('Нет свободных полей!Ничья!')
    exit('Игра окончена!')

  
print_game_field(field)
game(field, count)