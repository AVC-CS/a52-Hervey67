import pytest
import re

def regex_test(expected, content):
    pos = 0
    for token in expected:
        res = re.search(token, content[pos:])
        if res is None:
            assert False, f'Expect: {token}'
        pos += res.start() + 1

@pytest.mark.T1
def test_main_1():
    # data1.txt: 1..10, max = 10
    content = open('result1.txt').read()
    print(content)
    regex_test([r'10'], content)

@pytest.mark.T2
def test_main_2():
    # data2.txt: 5,50,3,7,12,8,44,2,1,9 max = 50
    content = open('result2.txt').read()
    print(content)
    regex_test([r'50'], content)

@pytest.mark.T3
def test_main_3():
    # data3.txt: all negative, max = -1
    content = open('result3.txt').read()
    print(content)
    regex_test([r'-1'], content)

@pytest.mark.T4
def test_main_4():
    # data4.txt: 100,50,3,7,12,8,44,2,1,9 max = 100
    content = open('result4.txt').read()
    print(content)
    regex_test([r'100'], content)
