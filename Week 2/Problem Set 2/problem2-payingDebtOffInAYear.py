# Problem Description: Iteratively find the lowest required payment to pay the loan off in 1 year

balance = 320000
annualInterestRate = 0.2


minMonthlyPayment = 0
monthlyInterestRate = annualInterestRate / 12.0

success = False
numLoops = 0

while(success == False):
	numLoops = numLoops + 1
	i = 1
	minMonthlyPayment = minMonthlyPayment + 10
	updatedBalance = balance
	while i <= 12:
		numLoops = numLoops + 1
		monthlyUnpaidBalance = updatedBalance - minMonthlyPayment
		updatedBalance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
		if(i == 12 and updatedBalance <= 0):
			success = True
		i = i + 1

print('Lowest Payment: ' + str(minMonthlyPayment))
print('Number of Loops: ' + str(numLoops))