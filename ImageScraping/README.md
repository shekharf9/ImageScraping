VIRTUALENV

virtualenv is a tool to create isolated Python environments. virtualenv creates a folder which contains all the necessary executables to use the packages that a Python project would need.

Install virtualenv via pip:

$ pip install virtualenv

Test your installation of virtualenv with command:

$ virtualenv --version


 Since the major development of the project was done with python3 and above, so to create a virtualenv with the python3.x environments run the command:

virtualenv -p python3 envname

This will generate a virtualenv with name "envname" and with python3 environments.


Once the virtualenv is created with the name envname, activate the virtualenv from the terminal with the command:

source envname/bin/activate



After activating the virtualenv, run the requirements.txt file present in the folder in the terminal to install all the dependencies and environments required for the project with the command:

$ pip install -r requirements.txt

That shall install all the environments required to run this project.



FLICKR API KEYS


First, you need to create a pair of Flickr API keys by visiting https://www.flickr.com/services/api/keys/. Note: A Yahoo! account is required to generate the API keys.

Flickr will generate two keys:

    A public key, which they call key
    A private key, which they call secret

Once the public and private keys have been generated, modify the flickrScraper.py file by entering your personal keys.




RUN THE run.py FILE TO EXECUTE THE CODE. 


##Reference
To know more about virtualenv and references, visit the link: http://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/


