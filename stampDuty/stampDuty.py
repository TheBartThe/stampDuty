def main():
	while True:
		price = input("Please enter the price of the house: £")
		try:
			price = int(price)
			if price < 0:
				print("Must be a positive number")
				continue
			break
		except ValueError:
			print("Input must be a number")
	tax = firstTimeBuyer(price)
	print(f'This will cost £{tax} in stamp duty')

def firstTimeBuyer(price):
	return 10

if __name__ == "__main__":
    main()
