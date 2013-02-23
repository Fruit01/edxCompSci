# Problem Description: Using bisection find the lowest payment possible to pay the loan off in a year


balance = 320000
annualInterestRate = 0.2

minMonthlyPayment = 0
monthlyInterestRate = annualInterestRate / 12.0
epsilon = 0.01

monthlyLowerBound = balance / 12.0
monthlyUpperBound = (balance * (1 + monthlyInterestRate) * 12) / 12.0

success = False
updatedBalance = balance

while(success == False):
	minMonthlyPayment = (monthlyUpperBound + monthlyLowerBound)/2.0
	updatedBalance = balance
	i = 1
	while i <= 12:
		monthlyUnpaidBalance = updatedBalance - minMonthlyPayment
		updatedBalance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
		i = i + 1

	
	if round(updatedBalance,2) == epsilon:
		success = True
		print('Lowest Payment: ' + str(round(minMonthlyPayment,2)))
	elif updatedBalance > epsilon:
		monthlyLowerBound = minMonthlyPayment
	elif updatedBalance < epsilon:
		monthlyUpperBound = minMonthlyPayment