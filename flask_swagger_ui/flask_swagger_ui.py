import json
from flask import Blueprint, render_template


def get_swaggerui_blueprint(base_url, api_url, config=None):
    swagger_ui = Blueprint('swagger_ui',
                           __name__,
                           static_folder='ui',
                           template_folder='templates')

    default_config = {
        'client_realm': 'null',
        'client_id': 'null',
        'client_secret': 'null',
        'app_name': 'null',
        'docExpansion': "none",
        'jsonEditor': False,
        'defaultModelRendering': 'schema',
        'showRequestHeaders': False,
        'supportedSubmitMethods': ['get', 'post', 'put', 'delete', 'patch']
    }

    if config:
        default_config.update(config)

    fields = {
        # Some fields are used in functions etc, so we treat them special
        'base_url': base_url,
        'api_url': api_url,
        'app_name': default_config.pop('app_name'),
        'client_realm': default_config.pop('client_realm'),
        'client_id': default_config.pop('client_id'),
        'client_secret': default_config.pop('client_secret'),

        # Rest are just serialized into json string for inclusion in the .js
        'config_json': json.dumps(default_config)
    }

    @swagger_ui.route('/')
    def show():
        return render_template('index.template.html', **fields)

    return swagger_ui
