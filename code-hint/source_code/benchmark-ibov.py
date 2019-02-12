first_purchase = (6000 * .43)
second_purchase = (6000 * .17)
third_purchase = (12500 * .08)

cogitation_purchase = (99900 * .01)

amount_paid = first_purchase + second_purchase + third_purchase + cogitation_purchase

stock_quantity = 6000 + 6000 + 12500 + 99900 + 666

average_price = (first_purchase + second_purchase + third_purchase + cogitation_purchase) / stock_quantity

print('{0:.2f}'.format(average_price))

print('R$ {0:.2f}'.format(amount_paid))

print(stock_quantity)

print(stock_quantity*.05)
