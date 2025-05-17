from project import welcome, options, flatten

def test_welcome():
    assert welcome() == None

def test_options():
    assert options() == None

def test_flatten():
    assert flatten([[["QS","5H","AS"],["2H","8H"],["7C"]],[["9H","5C"],["JH"]],["7D"]]) == ['QS', '5H', 'AS', '2H', '8H', '7C', '9H', '5C', 'JH', '7D']
