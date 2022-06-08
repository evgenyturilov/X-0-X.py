# Игра в крестики - нолики. Есть возможность играть против человека или бота (бот принимает случайные решения)

from random import randint
import time

field = [
          [' ', '1', '2', '3'],
          ['1', '-', '-', '-'],
          ['2', '-', '-', '-'],
          ['3', '-', '-', '-']
        ]                            # Создаем игровое поле, которое будет меняться в процессе игры
count = 0    # Счетчик для подсчета количества ходов

def print_game_field(field):        # Функция выводит на экран игровое поле
  print()
  for i in range(len(field)):
    for j in range(len(field[i])):
      print(field[i][j], end = ' ')
    print()

def user_input(var):    # Функция для ввода значения от игрока
  print(f'\nГде вы хотите поставить {var}?\n')
  x = int(input('   Введите позицию по оси X (от 1 до 3): '))
  y = int(input('   Введите позицию по оси Y (от 1 до 3): '))
  if x in (1,2,3) and y in (1,2,3):
    for i in range(len(field)):
      for j in range(len(field[i])):
        str = field[x][y]
    if str == '-':
      field[x][y] = var
    else:
      print('\nПоле занято, введите другие значения!')
      return user_input(var)
    return field
  else:
    print('Введены некорректные данные')
    return user_input(var)
  

def computer_input(var): # Функция для ввода значения от компьютера
  print('\n    Ход искина')
  time.sleep(1)
  x = randint(1,3)
  y = randint(1,3)
  for i in range(len(field)):
    for j in range(len(field[i])):
      str = field[x][y]
  if str == '-':
    field[x][y] = var
  else:
    return computer_input(var)
  return field

def check(field, var):  # Проверка условия выигрыша
  for i in range(len(field)):
      for j in range(len(field[i])):
        if ((field[1][1] == var and field[1][2] == var and field[1][3] == var) or
            (field[2][1] == var and field[2][2] == var and field[2][3] == var) or
            (field[3][1] == var and field[3][2] == var and field[3][3] == var) or
            (field[1][1] == var and field[2][1] == var and field[3][1] == var) or
            (field[1][2] == var and field[2][2] == var and field[3][2] == var) or
            (field[1][3] == var and field[2][3] == var and field[3][3] == var) or
            (field[1][1] == var and field[2][2] == var and field[3][3] == var) or
            (field[3][1] == var and field[2][2] == var and field[1][3] == var)):
              print(f'\nПобедил игрок {var}!')
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
    while count <= 8:
      user_input('X')
      count += 1
      check(field, 'X')
      print_game_field(field)
      print(f'\nЧисло ходов: {count}')
      user_input('0')
      count += 1
      check(field, '0')
      print_game_field(field)
      print(f'\nЧисло ходов: {count}')
      return game(field, count, sett)
    else:
      print('Нет свободных полей! Ничья!')
      exit('Игра окончена!')
  elif sett == '2':
    while count <= 8:
      user_input('X')
      count += 1
      check(field, 'X')
      print_game_field(field)
      print(f'\nЧисло ходов: {count}')
      computer_input('0')
      count += 1
      check(field, '0')
      print_game_field(field)
      print(f'\nЧисло ходов: {count}')
      return game(field, count, sett)
  else:
    print('Нет свободных полей! Ничья!')
    exit('Игра окончена!')
  

sett = settings()
print_game_field(field)
game(field, count, sett)