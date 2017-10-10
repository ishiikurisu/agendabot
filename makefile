default: test

do:
	python main.py

test:
	python test/test_google_calendar.py
	python test/test_agenda.py
