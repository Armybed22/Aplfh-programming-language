import aplfh
while True:
	text = input('aplfh > ')
	result, error = aplfh.run('<stdin>', text)

	if error: print(error.as_string())
	elif result: print(repr(result))
	if text == "exit()":
		break