"""
This script runs the helloSuggestions application using a development server.
"""

from os import environ
from helloSuggestions import run
from helloSuggestions import settings

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', settings.DEFAULT_SERVER_HOST)
    PORT = int(environ.get('SERVER_PORT', settings.DEFAULT_PORT))
    run(HOST, PORT)