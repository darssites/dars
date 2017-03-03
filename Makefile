# dars Makefile.
#
# NOTE: This will only generate; use "python dars.py make" to generate and serve.

all:
	python dars.py generate

install:
	@echo Installing dars...
	pip install -r requirements # Install requirements