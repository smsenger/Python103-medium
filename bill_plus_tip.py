#Exercise 1

#prompt user to enter bill total (converts string to decimal), then prompt user to describe service
bill = float(input('How much is the bill? '))
service = input('Was the service good, fair, or bad? ')

#conditional statements that calculate tip based on a percentage associated with the level of service. 
if service == 'good':
    tip = bill * .20
    print('Tip amount: $%s' %('%.2f' %(tip))) #round decimal to two places
    total = tip + bill
    print('Your total is $%s' %('%.2f' %(total))) #round decimal to two places
elif service == 'fair':
    tip = bill *.15
    print('Tip amount:$%s' %('%.2f' %(tip)))
    total = tip + bill
    print('Your total is $%s' %('%.2f' %(total)))
elif service == 'bad':
    tip = bill * .10
    print('Tip amount: $%s' %('%.2f' %(tip)))
    total = tip + bill
    print('Your total is $%s' %('%.2f' %(total)))
else:
    print('Womp-womp!')
