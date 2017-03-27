import unittest
import os
from agenda import *

class TestAgenda(unittest.TestCase):
  def test_true(self):
    self.assertTrue(True)

  def test_empty_directory(self):
    # Creating file
    with open('data/something.txt', 'w+') as fp:
      fp.write('else\n')
    # Deleting directory
    agenda = Agenda()
    agenda.clear()
    # Checking if data directory is empty
    only_files = [f for f in os.listdir('data') if os.path.isfile(os.path.join('data', f))]
    no_files = len(only_files)
    self.assertEqual(no_files, 0)

if __name__ == '__main__':
  unittest.main()
