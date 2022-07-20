"""
    Cheeseshop utils
"""

import os
import requests
import logging
import devops.resources.app_server as app_server

def server_up(port, team):
    cheeseshop = Cheeseshop()
    cheeseshop.logger.info(f"Starting {team} server on port {port}....")
    cheeseshop._start_server(port, team)

def server_down(team):
    cheeseshop = Cheeseshop()
    cheeseshop.logger.info(f"Stopping {team} server....")
    cheeseshop._stop_server(team)


class Cheeseshop:
    """ Wrapper class around Cheeseshop """

    def __init__(self):
        self.logger = logging.getLogger('Cheeseshop')

    def _start_server(self, port, team):
        app_server.start(port, team)

    def _stop_server(self, team):
        app_server.stop(team)