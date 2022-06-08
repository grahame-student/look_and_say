from unittest import TestCase

from hamcrest import assert_that, equal_to

from sequence_generator import SequenceGenerator


class TestSequenceGenerator(TestCase):
    def test_next_value_returns_initial_value_on_first_call(self):
        generator = SequenceGenerator(1)

        assert_that(generator.next_value(), equal_to("1"))
