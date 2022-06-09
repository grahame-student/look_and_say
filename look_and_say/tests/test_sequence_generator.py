from unittest import TestCase

from hamcrest import assert_that, equal_to
from look_and_say.generator.sequence_generator import SequenceGenerator


class TestSequenceGenerator(TestCase):
    def test_next_value_returns_1_on_first_call_when_start_value_is_1(self):
        generator = SequenceGenerator(1)
        assert_that(generator.next_value(), equal_to("1"))

    def test_next_value_returns_11_on_second_call_when_start_value_is_1(self):
        generator = SequenceGenerator(1)
        _ = generator.next_value()
        assert_that(generator.next_value(), equal_to("11"))

    def test_next_value_returns_21_on_third_call_when_start_value_is_1(self):
        generator = SequenceGenerator(1)
        _ = generator.next_value()
        _ = generator.next_value()
        assert_that(generator.next_value(), equal_to("21"))

    def test_next_value_returns_1211_on_fourth_call_when_start_value_is_1(self):
        generator = SequenceGenerator(1)
        _ = generator.next_value()
        _ = generator.next_value()
        _ = generator.next_value()
        assert_that(generator.next_value(), equal_to("1211"))
