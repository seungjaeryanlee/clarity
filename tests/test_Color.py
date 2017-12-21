#!/usr/bin/env python3
"""
This file defines unit tests for the Color enum.
"""
import unittest
from Color import Color


class TestColorEnum(unittest.TestCase):
    """
    This class tests the Color enum.
    """

    def test_switch(self):
        """
        Tests the switch() function of the Color enum.
        """
        self.assertEqual(Color.WHITE, Color.switch(Color.BLACK))
        self.assertEqual(Color.BLACK, Color.switch(Color.WHITE))
        self.assertEqual(Color.NEITHER, Color.switch(Color.NEITHER))
        self.assertEqual(Color.BLACK, Color.switch(Color.WHITE))
