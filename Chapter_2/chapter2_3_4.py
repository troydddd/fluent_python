from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')

def main():
	tokyo = City('tokyo', 'JP', 36.933, (35.689722, 139.691667))
	print(tokyo)
	print(tokyo.name)
	print(tokyo.population)
	print(tokyo.coordinates)
	print(tokyo[1])
	print(City._fields)

main()