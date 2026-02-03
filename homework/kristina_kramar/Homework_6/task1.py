text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
        'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
)

words = text.split()
final_text = []
punctuation = ".,"

for word in words:
    temp_punctuation = ''
    if word[-1] in punctuation:
        temp_punctuation = word[-1]
        word = word[:-1]
    word = word + 'ing' + temp_punctuation
    final_text.append(word)

print(' '.join(final_text))
