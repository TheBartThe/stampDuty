import pytest
from stampDuty import stampDuty

'''
def testInput(monkeypatch):
	monkeypatch.setattr('builtins.input', lambda a: 20000)
	assert stampDuty.main() == 10
'''

def testFTB():
	assert stampDuty.firstTimeBuyer(20000) == 10