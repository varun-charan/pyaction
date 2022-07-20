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
