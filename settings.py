import os
import domain

# not on heroku
if os.environ.get('PORT') is None:
    DEBUG = True

# database settings, defaults to locals
MONGO_HOST = os.environ.get('MONGO_HOST', 'ds143449.mlab.com')
MONGO_PORT = os.environ.get('MONGO_PORT', 43449)
MONGO_USERNAME = os.environ.get('MONGO_USERNAME', 'user1')
MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD', 'iamthe1')
MONGO_DBNAME = os.environ.get('MONGO_DBNAME', 'shopping_list_db')

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH) and deletes of individual items
# (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'DELETE']

# We enable standard client cache directives for all resources exposed by the
# API. We can always override these global settings later.
CACHE_CONTROL = 'max-age=20'
CACHE_EXPIRES = 20

XML = False

# swagger information
SWAGGER_INFO = {
    'title': 'ShoppingList Api',
    'version': '0.1',
    'description': 'an API description',
    'termsOfService': '',
    'contact': {
        'name': 'fregram',
        'url': 'http://fregram.com'
    }
}

# The DOMAIN dict explains which resources will be available and how they will
# be accessible to the API consumer.
DOMAIN = domain.DOMAIN
