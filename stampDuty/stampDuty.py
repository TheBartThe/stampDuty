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
	if tax == -1:
		print('Price must be positive')
	else:
		print(f'This will cost £{tax} in stamp duty')

def firstTimeBuyer(price):
	if (price < 0):
		return -1
	elif (price <= 250000):
		return 0

if __name__ == "__main__":
    main()
