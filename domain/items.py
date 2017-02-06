definition = {
    'item_title': 'item',

    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/nicolaiarocci/cerberus) for details.
    'schema': {
        'name': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 50,
            'required': True,
        }
    }
}
