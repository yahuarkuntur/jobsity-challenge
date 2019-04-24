JOBSITY - CHAT
==============


Requirements:
-------------

- Python 2.7
- RabbitMQ
- Redis


Installation:
-------------

- pip install -r requirements.txt
- Copy `config/main.config.dist` to `config/main.config` and modify 
    according to your needs.


How to run the project:
-----------------------

- Start the webserver with the command `python src/server.py`.
- Start the chatbot with the command `python src/chatbot.py`.
- Log messages will be displayed on the console.
- The webpage will be server as default on `127.0.0.1:5000`.


How to register users:

To register users use the command `python src/register_user.py` and enter
  the username and password. This command requires a valid bcrypt salt string 
  to be provided in `config/main.config`.


How to run the tests:
---------------------

To run the test suite execute the command `python -m unittest discover` 
  inside the `src` folder.

