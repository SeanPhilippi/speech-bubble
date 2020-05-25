speech_input = input('Give the cat something to say:')
text = 'Pet me and I will purr'

if len(speech_input) != 0:
	text = speech_input
text_length = len(text)

print('            {}'.format('-' * text_length))
print('          < {0} >'.format(text))
print('            {}'.format('--' * (text_length // 2))) 
print('           /                       ')
print(' /\_/\   /                         ')
print('( o.o )')
print(' > ^ <')

