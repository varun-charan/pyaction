"""
    Main CLI module
"""
import logging
import os

#  Click documentation and examples can be found here:
#  https://click.palletsprojects.com/en/7.x/quickstart/
import click

# click-option-group is a Click-extension package that adds option groups missing in Click.
# https://click-option-group.readthedocs.io/en/latest/
import click_option_group

import devops.cheeseshop
import devops.execute
import devops.vault
import devops.logconfig

# ----------------------------------------------------------------------------
# GLOBAL
# ----------------------------------------------------------------------------
@click.group()
@click.version_option()
@click.option("--verbose", "-v", is_flag=True, help="Enables verbose mode.")
def cli(verbose):
    devops.logconfig.configure_logging(verbose=verbose)

# ----------------------------------------------------------------------------
# Cheesehop
# ----------------------------------------------------------------------------
@cli.group()
def cheeseshop():
    """
    Cheeseshop commands
    """
    pass


@cheeseshop.command('server-up')
@click.option('-p', '--port', required=False, type=str, default="5050", help='Server Port for accepting traffic')
@click.option('--team', '-t', required=True,
              type=click.Choice(['devops', 'application', ], case_sensitive=False), help='Select target team')
def server_up(port, team):
    """
        Bring the cheeseshop application server up
    """
    return devops.cheeseshop.server_up(port, team)


@cheeseshop.command('server-down')
@click.option('-p', '--port', required=False, type=str, default="5050", help='Server Port for accepting traffic')
@click.option('--team', '-t', required=True,
              type=click.Choice(['devops', 'application', ], case_sensitive=False), help='Select target team')
def server_down(port, team):
    """
        Bring the cheeseshop application server down
    """
    return devops.cheeseshop.server_down(port, team)

# ----------------------------------------------------------------------------
# Execute
# ----------------------------------------------------------------------------
@cli.command('exec')
@click.option('--env',
              help='Sets environment variable, usage: --env NAME1=VALUE --env NAME2=VALUE',
              multiple=True)
@click.argument('command')
def execute(env, command):
    """
        Executes a command with the environment.
    """

    devops.execute.execute(command, env)

# ----------------------------------------------------------------------------
# Vault
# ----------------------------------------------------------------------------
@cli.group()
def vault():
    """
        Vault commands.

        Assumes VAULT_ADDR is in the env.

        If VAULT_SA_TOKEN and VAULT_ROLE_NAME are set in env, authentication with k8s-prd03 mount point will be attempted.

        If VAULT_SA_TOKEN, VAULT_ROLE_NAME and VAULT_MOUNT_POINT are set in env, they are used for authentication.

        If called without options, assumes either VAULT_TOKEN is in the env or ~/.vault_token holds a valid token.

        See subcommands' help messages for option details.

    """


@vault.command('get')
@click.argument('secret_path')
@click.argument('secret_name')
def get_vault_secret(secret_path, secret_name):
    """
        Get a Vault secret.

        Assumes VAULT_ADDR is in the env.

        If VAULT_SA_TOKEN and VAULT_ROLE_NAME are set in env, authentication with k8s-prd03 mount point will be attempted.

        If VAULT_SA_TOKEN, VAULT_ROLE_NAME and VAULT_MOUNT_POINT are set in env, they are used for authentication.

        If called without options, assumes either VAULT_TOKEN is in the env or ~/.vault_token holds a valid token.
    """

    return click.echo(devops.vault.get_secret(
        secret_path,
        secret_name))


@vault.command('get-login-token')
def get_login_token():
    """
        Get a Vault login token.

        Assumes VAULT_ADDR is in the env.

        If VAULT_SA_TOKEN and VAULT_ROLE_NAME are set in env, authentication with k8s-prdtwo mount point will be attempted.

        If called without options, assumes either VAULT_TOKEN is in the env or ~/.vault_token holds a valid token.
    """

    return click.echo(devops.vault.get_login_token())

