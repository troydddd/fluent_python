# -*- coding: utf-8 -*-

import re

content = '333STR1666STR299'
regex = r'([A-Z]+(\d))'

if __name__ == '__main__':
	print(re.match(regex, content))

	match = re.search(regex, content)
	print('\nre.search() return value:' + str(type(match)))
	print(match.group(0), match.group(1), match.group(2))

	result1 = re.findall(regex, content)
	print('\nre.findall() return value:'+str(type(result1)))
	for m in result1:
		print(m[0], m[1])

	result2 = re.finditer(regex, content)
	print('\nre.finditer() return value:' + str(type(result2)))
	for m in result2:
		print(m.group(0), m.group(1), m.group(2))