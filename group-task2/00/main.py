import sys

PHONE_NUMBER = "9123669948"
def main(argv):
	result = 9.8*float(argv[0])
	print(round(result,2))


if __name__ == "__main__":
	main(sys.argv[1:])
