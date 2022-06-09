from unittest import TestCase

from hamcrest import assert_that, equal_to
from look_and_say.generator.sequence_generator import SequenceGenerator


class TestSequenceGenerator(TestCase):
    def test_next_value_returns_initial_value_on_first_call(self):
        generator = SequenceGenerator(1)
        assert_that(generator.next_value(), equal_to("1"))

    def test_next_value_returns_11_on_second_call_when_start_value_is_1(self):
        generator = SequenceGenerator(1)
        _ = generator.next_value()
        assert_that(generator.next_value(), equal_to("11"))
