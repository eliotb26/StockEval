PYLINT = flake8

FORCE:

requirements: FORCE
	pip3 install -r requirements-dev.txt

venv: 
	source venv/bin/activate
