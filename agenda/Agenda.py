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
