lt = {
        'new': [{
            'a': 1,
            'b': 2
            }],
        'old': [{
            'a': 1,
            'b': 2
        }]
    }

for a in lt:
    print(a)
    for b in a: 
        print(b)

for a in lt:
    print(a)
    for b in lt[a]: 
        print(b)