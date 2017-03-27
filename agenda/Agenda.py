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
       raise RuntimeError()

    return outlet
