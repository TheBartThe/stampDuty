import pytest
from stampDuty import stampDuty

'''
def testInput(monkeypatch):
	monkeypatch.setattr('builtins.input', lambda a: 20000)
	assert stampDuty.main() == 10
'''

def testFTBNeg1():
	assert stampDuty.firstTimeBuyer(-100000) == -1

def testFTBNeg2():
	assert stampDuty.firstTimeBuyer(-1) == -1

def testFTBFree1():
	assert stampDuty.firstTimeBuyer(0) == 0

def testFTBFree2():
	assert stampDuty.firstTimeBuyer(10000) == 0

def testFTBFree3():
	assert stampDuty.firstTimeBuyer(100000) == 0

def testFTBFree4():
	assert stampDuty.firstTimeBuyer(250000) == 0