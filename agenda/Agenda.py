import agenda.Filesystem as fs

class Agenda:
  def __init__(self):
    pass

  def clear(self):
    files = fs.get_files('data')
    for f in files:
      fs.remove_file('data/' + f)

  def get_time(self, moment):
    outlet = [ ]

    if ('date' not in moment) and ('hour' not in moment):
       raise ValueError()

    # TODO Actually get the event

    return outlet

  def set_time(self, event):
    if ('date' not in event) and ('hour' not in event) and ('description' not in event):
      raise ValueError()
    # TODO Save event
    current_day_file = self.get_current_day_file(event['date'])
    hourly_events = self.generate_event(event)
    for description in hourly_events:
        fs.add_line_to_file(current_day_file, description)

  def generate_event(self, event):
    # TODO Generate a list of events, each item with a hour event
    hour_limits = list(map(int, event['hour']))
    lower_limit = hour_limits[0]
    upper_limit = hour_limits[1]
    hourly_events = [ ]

    for hour in range(lower_limit, upper_limit):
      table_line = '%d;%s' % (hour, event['description'])
      hourly_events.append(table_line)

    return hourly_events

  def get_current_day_file(date):
    return 'data/' + date + '.csv'
