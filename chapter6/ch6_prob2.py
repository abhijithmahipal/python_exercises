#Problem 2: Write a function flatten_dict to flatten a nested dictionary by joining the keys with . character.

def flatten_dict(a, result=None):
	if result is None:
		result = {}
	for x in a:
		if isinstance(x, dict):
			flatten_dict(x, result)
		else:
			return result.update(x)
	return result
	
def main():
	fdict=flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4})
	print fdict

main()
