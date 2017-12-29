#!/usr/bin/env python3
"""
This file defines unit tests for the Color enum.
"""
from clarity.Color import Color


class TestColorEnum:
    """
    This class tests the Color enum.
    """

    def test_switch(self):
        """
        Tests the switch() function of the Color enum.
        """
        assert Color.WHITE == Color.switch(Color.BLACK)
        assert Color.BLACK == Color.switch(Color.WHITE)
        assert Color.NEITHER == Color.switch(Color.NEITHER)
        assert Color.BLACK == Color.switch(Color.WHITE)
