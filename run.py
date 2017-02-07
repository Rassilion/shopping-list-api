import os
from eve import Eve
from flask_swagger_ui.flask_swagger_ui import get_swaggerui_blueprint
from eve_swagger import swagger

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

# eve swagger
app.register_blueprint(swagger)

# swagger ui
SWAGGER_URL = '/docs'  # URL for exposing Swagger UI (without trailing '/')
API_URL = '/api-docs'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'supportedSubmitMethods': ['get', 'post', 'put', 'delete', 'patch']
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
    app.run(host=host, port=port)
