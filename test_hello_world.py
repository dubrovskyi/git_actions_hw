import pytest

from hello_world import sum_def


def test_sum_def():
    assert(sum_def(5,5), 10)
