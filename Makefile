# dars Makefile.
#
# NOTE: This will only generate; use "python dars.py make" to generate and serve.

all:
	python dars.py --generate

install:
	@echo Installing dars...
	pip install -r requirements # Install requirements

cleanup:
	# remove all __pycache__-related stuff
	@echo Removing __pycache__...
	find . | grep -E \(__pycache__\|\.pyc\|\.pyo\) | xargs rm -rf
	@echo Remember to check the version number!
