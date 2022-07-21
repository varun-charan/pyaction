"""
    Wrapper around hvac (Hashicorp Vault)
"""
import logging
import os
import os.path
import sys

import hvac
import hvac.exceptions
import requests


def get_secret(secret_path, secret_key=None):
    """
        Reads a secret from a given Vault path.
    """
    logger = logging.getLogger('Vault')
    try:
        vault = Vault()
        return vault.get_secret(secret_path, secret_key)
    except (hvac.exceptions.InternalServerError,
            hvac.exceptions.Unauthorized,
            hvac.exceptions.Forbidden,
            hvac.exceptions.VaultNotInitialized) as excpt:
        logger.error(excpt)
        sys.exit(-1)


def get_login_token(**kwargs):
    """
       Returns a Vault login token.
    """
    logger = logging.getLogger('Vault')
    try:
        vault = Vault()
        return vault.get_login_token()
    except (hvac.exceptions.InternalServerError, hvac.exceptions.Unauthorized, hvac.exceptions.Forbidden) as excpt:
        logger.error(excpt)
        sys.exit(-1)


class Vault:
    """ Wrapper class around Vault functionalities """

    def __init__(self):

        self.logger = logging.getLogger('Vault')
        self.__client = hvac.Client(url=os.getenv('VAULT_ADDR'))

        if 'VAULT_TOKEN' in os.environ:
            self.logger.info('Using Token Auth Method - environment Vault token from VAULT_TOKEN')
            self.__client.token = os.environ.get('VAULT_TOKEN')
            self._check_authentication()
            return

        path_local_token = os.path.expanduser('~/.vault-token')
        if os.path.exists(path_local_token):
            self.logger.info(f'Using Token Auth Method - cashed Vault token file from {path_local_token}')
            with open(path_local_token) as token_file:
                self.__client.token = token_file.readline()
            self._check_authentication()
            return

        raise hvac.exceptions.VaultNotInitialized("Couldn't figure out authorization scheme")

    def _check_authentication(self):
        if not self.__client.is_authenticated():
            error_msg = 'Provided address and/or token is not correct'
            raise hvac.exceptions.Unauthorized(error_msg)

        self.logger.info('Authentication successful, injected VAULT_TOKEN into current environment')
        os.environ['VAULT_TOKEN'] = self.__client.token

    def get_login_token(self):
        """
           Returns a Vault login token.
        """
        return self.__client.token

    def get_secret(self, path, key=None):
        """
        Get secret from the specified path.
        If secret_key is present then return the value of this specific key.
        :param path: Path to the secret
        :param key: Key to return, if None then the whole wey is returned
        :return: secret
        """

        # vault CLI requires to pass path with 'secret/' in the beginning of the path.
        # to avoid user mistakes where to pass what - strip it here (as not required)
        if path.startswith('secret/'):
            path = path.replace('secret/', '', 1)
        self.logger.debug(f'Reading from \'{path}\'')

        try:
            read_response = self.__client.secrets.kv.read_secret_version(path=path)
            if key:
                if key in read_response['data']['data'].keys():
                    return read_response['data']['data'][key]
                else:
                    self.logger.error(f'Couldn\'t find key \'{key}\' in secret')
                    sys.exit(-1)

            return read_response['data']['data']

        except (hvac.exceptions.Unauthorized, hvac.exceptions.Forbidden, requests.exceptions.ConnectionError) as expt:
            self.logger.fatal(f'Couldn\'t read secret: {expt}')
            sys.exit(-1)
            