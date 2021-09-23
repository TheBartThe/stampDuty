import pytest
from stampDuty import stampDuty

'''
def testInput(monkeypatch):
	monkeypatch.setattr('builtins.input', lambda a: 20000)
	assert stampDuty.main() == 10
'''

def testFTBNeg1():
	assert stampDuty.firstTimeBuyer(-100000) == 0

def testFTBNeg2():
	assert stampDuty.firstTimeBuyer(-1) == 0

def testFTBFree1():
	assert stampDuty.firstTimeBuyer(0) == 0

	'''
def testFTBFree2():
	assert stampDuty.firstTimeBuyer(10000) == 0

def testFTBFree3():
	assert stampDuty.firstTimeBuyer(100000) == 0
'''

def testFTBFree4():
	assert stampDuty.firstTimeBuyer(250000) == 0
	
def testFTBLow1():
	assert stampDuty.firstTimeBuyer(300000) == 2500

def testFTBLow2():
	assert stampDuty.firstTimeBuyer(925000) == 33750

def testFTBMid1():
	assert stampDuty.firstTimeBuyer(950000) == 36250

def testFTBMid2():
	assert stampDuty.firstTimeBuyer(1500000) == 91250

def testFTBHigh1():
	assert stampDuty.firstTimeBuyer(1600000) == 103250