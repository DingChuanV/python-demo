import random

# 生命次数
lives = 3
# 神秘单词 随机选择
words = ['pizza', 'fairy', 'teeth', 'shirt', 'shirt', 'plane']
secret_word = random.choice(words)

print(secret_word)

clue = list('????')
heart_symbol = u'\u2764'

guess_word_correctly = False


def update_cule(guessed_letter, secret_word, clues):
  index = 0

  while index < len(secret_word):
    if guessed_letter == secret_word[index]:
      clues[index] = guessed_letter
    index = index + 1


while lives > 0:
  print(clue)
  print('剩余的生命次数：' + heart_symbol * lives)
  guess = input('猜测字母或者是整个单词:')

  if guess == secret_word:
    guess_word_correctly = True
    break

  if guess in secret_word:
    update_cule(guess, secret_word, clue)
  else:
    print("错误。你丢了一条命\n")
    lives = lives - 1

if guess_word_correctly:
  print('你赢了! 秘密单词是 ' + secret_word)
else:
  print('你输了! 秘密单词是 ' + secret_word)
