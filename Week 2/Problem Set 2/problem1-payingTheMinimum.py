# Work out the total amount paid on a loan over a year if only the minimum repayment is made each month


balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

monthlyInterestRate = annualInterestRate / 12.0
totalPaid = 0
i = 1

while i <= 12:
	print('Month: ' + str(i))

	minMonthlyPayment = round(monthlyPaymentRate * balance,2)
	totalPaid = round(totalPaid + minMonthlyPayment,2)
	balance = balance - minMonthlyPayment
	balance = round(balance + (monthlyInterestRate * balance), 2)
	print('Minimum monthly payment: ' + str(minMonthlyPayment))
	print('Remaining balance: ' + str(balance))
	i = i + 1

print('Total paid: ' + str(totalPaid))
print('Remaining balance: ' + str(balance))