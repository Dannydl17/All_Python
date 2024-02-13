import json
accounts_dict = {'account': [{'account': 100, 'name': 'Jones', 'balance': 24.98},
                             {'account': 200, 'name': 'Doe', 'balance': 345.67}]}

with open('../accounts.json', 'w') as accounts:
    json.dump(accounts_dict, accounts)


with open('../accounts.json', 'r') as accounts:
    accounts_json = json.load(accounts)