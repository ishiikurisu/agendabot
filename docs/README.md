# Introduction

The idea of the `Agenda` class is to work like a schedule to mark who is responsible for that moment in the room. For the outside user, some rules must be clear when they use this class:

- The user must (at least ideally) check if the room is available before marking a time. If that time is free, then this user can mark an _event_ on the calendar.
- Everyone can mark events using the agendabot, but only the creators of an event can unmark it.

Under this perspective, the `Agenda` class must have some methods and work with some other classes to work.

## `Agenda` Class ##

This class is the main responsible for dealing with time. It must keep track of all occupied hours of a day in the calendar.

It will fill many `*.csv` files in the `data` folder, each one named after the day they relate to. Each row in this table will have three fields:

- The reserved hour.
- The responsible for that hour (the Telegram id of the one that marked that event).
- The event description.

### Methods ###

#### `clear()`

Destroys all marked events on the calendar. Not advised to use.

#### `get_time(moment)`

Gets what event is happenning on that moment. Moment must be a dictionary as follows:

- `'date'` will return a string in YYYYMMDD format asking for which day to look for.
- `'hour'` will return a list of two integers specifying from which hour to which hour (in 24h format) the user wants to query.

If this moment dictionary does not have these keys, the method will raise a `ValueError`.

If no event is happenning in that moment is happenning in that moment, this method will return an empty list. Otherwise a list of events will be given.

#### `set_time(event)`

Sets an event through a dictionary:

- `'date'` must return a string in YYYYMMDD format asking for which day to book.
- `'hour'` must return a list of two integers specifying from which hour to which hour (in 24h format) the user wants to book.
- `'description'` must return an Unicode string describing what is being booked in that day.

If this moment dictionary does not have these keys, the method will raise a `ValueError`.

If an event is happenning in that moment, the method will raise a `RuntimeError`. Otherwise, nothing happens and the event is marked on the calendar.

#### `destroy_event(moment)`

Frees an event from the calendar. The moment must be described just like you get an event.

#### `generate_event(event)`

Creates a list of hourly events to be inserted in the data file.
