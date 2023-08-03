# mortgage.py
#
# Exercise 1.7-11

principal = 500000
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment_start_month = 61
extra_payment_end_month = 108
current_month = 0
extra = 0

while principal > 0:  

    if extra_payment_start_month <= current_month < extra_payment_end_month:
        extra = 1000
    else:
        extra = 0

    principal = principal * (1 + rate / 12) - (payment + extra)

    total_paid += (payment + extra)

    if principal < 0:
        total_paid += principal
        principal = 0

    current_month += 1

    print(total_paid, principal)
print('total paid:', total_paid)