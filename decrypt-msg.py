import base64

MESSAGE = '''
E0YABgINBB8aT0FJU0YJQ1VQRBZEQVQQDgINCQgPFBZUQVQRF1RDRQ0EHhYFSU1MTg0HFRwTGkIX EQoRTwgdEBMLBQULBARUX0FJUFNZWVQeBB4WDxpGTFNIRgYdDQFSW1RUFkRBVAEADAMFHRtGU0lB SUJRV1UWREFUFQ4BRkxTSEYEGg9PFk0=
'''

KEY = 'hassanalihassan10101'

result = []
for i, c in enumerate(base64.b64decode(MESSAGE)):
	result.append(chr(c ^ ord(KEY[i % len(KEY)])))

print(''.join(result))
