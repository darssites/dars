# dars [![Build Status](https://travis-ci.org/darssites/dars.svg?branch=master)](https://travis-ci.org/darssites/dars)
The webpage making thing written in Python. Meant to give a different approach to web development; for those who are good with scripting languages and want to do web dev.

## Setup

To install all the dependencies, run
	
	make install

If you don't have [make](https://www.gnu.org/software/make/), either get it, or run

	pip install -r requirements
    
Which installs all the dependencies.

## How to

You'll be putting all your code in the `user.py` file.

A basic site:

    from classes.Header import Header

    def code(page):

      title = Header("Your Dars Site")
      page.append(title)

      page.close()
    
Then, save the file as `user.py` to the same folder as `dars.py`. Next, open up your favorite prompt with Python 3 installed, and say:

    python dars.py make

The "make" command means generate and then serve. Assuming all's well, you'll get a little webserver hosting your code in the command line. Now open your browser and go to:

    localhost
    
By default, it'll run on port 80 so your browser can see it as a webserver.
