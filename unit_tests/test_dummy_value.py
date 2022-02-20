# Context sets up paths to be able to import from source
import context

# Module we're unit testing
import sample

# Unit testing framework
import unittest

# Each unit test class is dedicated to unit testing a source code class
# These classes must derive from unittest.TestCase
# Each unit test function tests an aspect of the class
class TestDummyValue(unittest.TestCase):

    def test_getting_dummy_value(self):
        
        # Create sample
        dummy = sample.Sample()
        
        # Get dummy value
        dummy_value = dummy.get_dummy_value()

        # Assert dummy value is a list
        assert isinstance(dummy_value, list)

        # Assert dummy value is correct
        assert dummy_value == ['dummy', 'value']