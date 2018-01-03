#!/usr/bin/env python3 

import baby_sitter_kata
import unittest

class babysitterKataTDD(unittest.TestCase):

	def testBabySitterHoursGreaterThanOrEqualToSeventeenReturnsTrue(self):
		self.assertEqual(True, baby_sitter_kata.getBabySitterStartHours(17))
		self.assertEqual(True, baby_sitter_kata.getBabySitterStartHours(18))

	def testBabySitterHoursLessThanSeventeenReturnsFalse(self):
		self.assertEqual(False, baby_sitter_kata.getBabySitterStartHours(16))	

	def testBabySitterFinishingHoursMoreThanStartingHoursAndLessThanFourReturnFalse(self):
		self.assertEqual(False, baby_sitter_kata.getBabySitterFinishHours(4))	

if __name__ == '__main__':
	unittest.main()		