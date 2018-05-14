data = [
    {
        'identify': '0006-0000000002',
        'amount': '120000'
    },
    {
        'identify': '0006-0000000002',
        'amount': '5000'
    },
    {
        'identify': '0006-0000000002',
        'amount': '5000'
    },
    {
        'identify': '0006-0000000004',
        'amount': '5000'
    }
]

balance = [
    {
        'identify': '0006-0000000002',
        'amount': '10000'
    },
    {
        'identify': '0006-0000000004',
        'amount': '16000'
    }
]


def check_balance(account):
    for i in balance:
        if i['identify'] == account:
            current_bal = i['amount']
            return current_bal


# print(check_balance('0006-0000000004'))

for i in data:
    current_bal = check_balance(i['identify'])
    if float(i['amount']) <= float(current_bal):
        new_bal = float(current_bal) - float(i['amount'])
        print(new_bal)
    else:
        print('No balance.')



# def balance(bal):
#     current_amount = float([data]['amount']) - bal
#     return current_amount
#
#
# print(balance(100))
