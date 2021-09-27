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
	band0Rate = 0
	band1Rate = 0.05
	band2Rate = 0.1
	band3Rate = 0.12
	band0Price = 250000
	band1Price = 925000
	band2Price = 1500000
	tax = 0
	while (price > 0):
		if (price <= band0Price):
			taxAdded = price * band0Rate
			tax += taxAdded
			price = 0
		elif (price <= band1Price):
			taxAdded = band1Rate * (price - band0Price)
			tax += taxAdded
			price = band0Price
		elif (price <= band2Price):
			taxAdded = band2Rate * (price - band1Price)
			tax += taxAdded
			price = band1Price
		else:
			taxAdded = band3Rate * (price - band2Price)
			tax += taxAdded
			price = band2Price
	return tax

if __name__ == "__main__":
    main()
