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
	band1Rate = 0.05
	band2Rate = 0.1
	band3Rate = 0.12
	band0Price = 250000
	band1Price = 925000
	band2Price = 1500000
	if (price <= band0Price):
		return 0
	elif (price <= band1Price):
		tax = band1Rate * (price - 250000)
		return tax
	elif (price <= band2Price):
		band1 = price - 925000
		band2 = 675000
		tax = (0.1 * band1) + (0.05 * band2)
		return tax
	else:
		band1 = price - 1500000
		band2 = 575000
		band3 = 675000
		tax = (0.12 * band1) + (0.1 * band2) + (0.05 * band3)
		return tax

if __name__ == "__main__":
    main()
