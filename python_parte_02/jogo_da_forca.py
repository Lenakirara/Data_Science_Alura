import random


def welcome_msg():
  print("""
  ************************************
  *** Boas Vindas ao Jogo da Forca ***
  ************************************
  """)


def drawing_hangman_game(error):
  print("""
  _______     
 |/      |    
  """)

  if (error == 1):
    print("""
     |      (_)   
     |
     |
     |   
    """)

  if (error == 2):
    print("""
     |      (_)   
     |      \\
     |
     |
    """)

  if (error == 3):
    print("""
     |      (_)   
     |      \|
     |
     |
    """)

  if (error == 4):
    print("""
     |      (_)   
     |      \|/
     |
     |
    """)

  if (error == 5):
    print("""
     |      (_)   
     |      \|/
     |       |
     |
    """)

  if (error == 6):
    print("""
     |      (_)   
     |      \|/
     |       |
     |      /
    """)

  if (error == 7):
    print("""
     |      (_)   
     |      \|/
     |       |
     |      / \\
    """)
  print("""
     |            
    _|___ \n
  """)


def read_file():
  file = open('secret_words.txt', 'r')
  words = []
  for line in file:
    words.append(line.strip())

  file.close()
  
  random_word = random.randrange(0, len(words))
  secret_word = words[random_word].upper()
  return secret_word


def get_guess():
  guess = input('Qual a letra? ').upper().strip()
  return guess


def get_correct_position_letter(secret_word, guess, correct_letter):
  position = 0
  for letter in secret_word:
        if (guess == letter):
          correct_letter[position] = letter
        position += 1


def msg_game_player(hit, secret_word):
  if (hit):
    print(f"""
    Parabéns, você ganhou!!!
        ____________
       '._==_==_==_.'
       .-\\:       /-.
      | (|:.       |) |
       '-|:.       |-'
         \\::.     /
          '::.  .'
            )  (
          _.'  '._
         '--------'
    """)
  else:
    print(f"""
    Puxa, você foi enforcado!
    A palavra era {secret_word}

       _______________
      /               \\
     /                 \\
    /                   \\
   |    XXXX     XXXX    |
   |    XXXX     XXXX    |
   |    XXX       XXX    |
   |                     |
   \__       XXX       __/
     |\      XXX      /|
     | |             | |
     | I I I I I I I I |
     |  I I I I I I I  |
     \_               _/
       \_           _/
         \_________/

""")


def play():
  welcome_msg()

  secret_word = read_file()

  correct_letter = ["_" for letter in secret_word]

  hanged = False
  hit = False
  error = 0
  
  while(not hanged and not hit):
    guess = get_guess()

    if (guess in secret_word):
      get_correct_position_letter(secret_word, guess, correct_letter)
    else:
      error += 1
      drawing_hangman_game(error)

    hanged = error == 7
    hit = '_' not in correct_letter

    print(correct_letter)

  hit = msg_game_player(hit, secret_word) 


if __name__ == "__main__":
  play()
