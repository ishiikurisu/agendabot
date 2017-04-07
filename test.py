import unittest
import os
from agenda import *
from functools import reduce

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

  def test_generate_list_of_events_from_event_description(self):
    event = self.get_real_event()
    agenda = Agenda()
    list_of_events = agenda.generate_event(event)
    string_of_events = ''
    for event in list_of_events:
      string_of_events += event + '\n'
    self.assertEqual('10;nothing actually\n11;nothing actually\n', string_of_events)

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
