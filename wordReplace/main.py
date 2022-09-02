def replace_word():
    text = "I am a very long sentence"
    word_to_replace = input('Enter word to replace: ')
    word_replacement = input('Enter word to replace with: ')
    print(text.replace(word_to_replace, word_replacement))
    print('completed successfully')

replace_word()