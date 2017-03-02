# dars Makefile.
#
# NOTE: This will only generate; use "python dars.py make" to generate and serve.

all:
	python dars.py generate

install:
	@echo Installing dars...
	pip install -r requirements # Install requirements
	while true; do
	    read -p "Would you like to clone dars-manager?" yn
	    case $yn in
		[Yy]* ) git clone http://github.com/darssites/dars-manager; break;;
		[Nn]* ) exit;;
		* ) echo "Please answer yes or no.";;
	    esac
	done
	
