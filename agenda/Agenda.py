import agenda.Model as M

class Agenda:
  def __init__(self):
    pass

  def clear(self):
    files = M.get_files('data')
    for f in files:
      M.remove_file('data/' + f)

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
