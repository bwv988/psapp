"""
NoseTests for the Batch class.
"""

from batch import Batch
from nose.tools import eq_

def print_batch(obj):
    print("Batch after update: \n")
    print(obj.get_batch())

def test_batch1():
    c = Batch(3)
    c.set_col(1, Batch.MATTE)
    eq_(c.set_col(1, Batch.GLOSSY), 0)
    print_batch(c)

def test_batch2():
    c = Batch(3)
    c.set_col(1, Batch.GLOSSY)
    eq_(c.set_col(1, Batch.MATTE), 0)
    print_batch(c)  

def test_batch3():
    c = Batch(3)
    c.set_col(1, Batch.GLOSSY)
    eq_(c.set_col(1, Batch.GLOSSY), 1)
    print_batch(c)

def test_batch4():
    c = Batch(3)
    c.set_col(1, Batch.GLOSSY)
    eq_(c.set_col(2, Batch.MATTE), 1)
    print_batch(c)