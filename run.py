import os
from eve import Eve

# Load the settings file using a robust path so it works when
# the script is imported from the test suite.
this_directory = os.path.dirname(os.path.realpath(__file__))
settings_file = os.path.join(this_directory, 'settings.py')

port = os.environ.get('PORT')
if port:
    # Heroku
    host = '0.0.0.0'
    port = int(port)
else:
    host = '127.0.0.1'
    port = 5000

app = Eve(settings=settings_file)

if __name__ == '__main__':
    app.run(host=host, port=port)
