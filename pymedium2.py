#Exercise 2


#prompt user to enter bill total (converts string to decimal), then prompt user to describe service
bill = float(input('How much is the bill? '))
service = input('Was the service good, fair, or bad? ')

#prompt user to provide number of people to divide bill among
group = int(input('How many people in your group? '))

#conditional statements that calculate tip based on a percentage associated with the level of service. 
if service == 'good':
    tip = bill * .20
    print('Tip amount: $%s' %('%.2f' %(tip))) #round decimal to two places
    total = tip + bill
    print('Your total is $%s' %('%.2f' %(total)))
    per_each = (total/group)
    print('Amount per person: $%s' %('%.2f' %(per_each)))
elif service == 'fair':
    tip = bill *.15
    print('Tip amount: $%s' %('%.2f' %(tip)))
    total = tip + bill
    print('Your total is $%s' %('%.2f' %(total)))
    per_each = (total/group)
    print('Amount per person: $%s' %('%.2f' %(per_each)))
elif service == 'bad':
    tip = bill * .10
    print('Tip amount: $%s' %('%.2f' %(tip)))
    total = tip + bill
    print('Your total is $%s' %('%.2f' %(total)))
    per_each = (total/group)
    print('Amount per person: $%s' %('%.2f' %(per_each)))
else:
    print('Womp-womp!')