import adal


def get_access_token(config):
    context = adal.AuthenticationContext(authority=config['app_details']['authority_url'],
                                         validate_authority=True,
                                         api_version=None)
    token = context.acquire_token_with_username_password(resource=config['app_details']['resource_url'],
                                                         client_id=config['app_details']['client_id'],
                                                         username=config['powerbi']['username'],
                                                         password=config['powerbi']['password'])
    access_token = token.get('accessToken')
    return access_token
