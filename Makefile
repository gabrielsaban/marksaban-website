.PHONY: setup run check

setup:
	python3 -m venv .venv
	.venv/bin/pip install -r requirements.txt

run:
	.venv/bin/python app.py

check:
	.venv/bin/python -m unittest discover -s tests
