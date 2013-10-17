#!/usr/bin/env python 
import sys, os
thisdir = os.path.dirname(__file__)

import unittest
from serwer4 import Server
from protocolObjects import *

class STestCase(unittest.TestCase):

	def setUp(self):
		self.s = Server()
		
	def tearDown(self):
		self.s = None

unittest.main()
