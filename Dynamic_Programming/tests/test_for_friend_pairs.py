"""Testing friend_pairs"""

import pytest

from Dynamic_Programming.code import friend_pairs


@pytest.mark.parametrize('inputs, outputs',
                         [('0', 0),
                          ('3', 4),
                          ('10', 9496),
                          ])
def test_itr(inputs, outputs):
    """Tests for positive results"""
    assert friend_pairs.itr(inputs) == outputs


@pytest.mark.parametrize('inputs, outputs',
                         [('-5', None),
                          ('five', None),
                          ('', None),
                          (' ', None)])
def test_itr(inputs, outputs):
    """Tests for negative results"""
    assert friend_pairs.itr(inputs) == outputs
