import unittest
import os
from agenda import *

class TestAgenda(unittest.TestCase):
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

  def test_trying_to_get_incomplete_moment(self):
    agenda = Agenda()
    with self.assertRaises(ValueError):
      agenda.get_time({ })

  def test_trying_to_set_incomplement_event(self):
    agenda = Agenda()
    with self.assertRaises(ValueError):
      agenda.set_time({ })

  def test_trying_to_set_and_get_a_valid_event(self):
    agenda = Agenda()
    event = self.get_real_event()
    agenda.set_time(event)
    events = agenda.get_time(event)
    no_events = len(events)
    self.assertEqual(1, no_events)

  def test_trying_to_get_past_event(self):
    moment = self.get_past_event()
    agenda = Agenda()
    events = agenda.get_time(moment)
    no_events = len(events)
    self.assertEqual(0, no_events)

  def get_past_event(self):
    return {
      'date': '19940525',
      'hour': [12, 14]
    }

  def get_real_event(self):
    return {
      'date': '20190813',
      'hour': [10, 12],
      'description': 'nothing actually'
    }

if __name__ == '__main__':
  unittest.main()
