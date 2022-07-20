"""
    Execute commands module.
"""
import os
import subprocess
import sys


def update_env_and_fork(command, envs=None, capture_output=False):
    """
        Forks a new process running the specified command.
        All envs from current process are extended by the 'envs'
        and passed to the forked process.

        new_envs are expected to be a dict object.
    """

    if envs is None:
        envs = {}
    new_env = os.environ.copy()
    new_env.update(envs)

    if isinstance(command, str):
        command = command.split(' ')

    try:
        if capture_output:
            return subprocess.run(command, env=new_env, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        else:
            return subprocess.run(command, env=new_env, check=True)
    except subprocess.CalledProcessError as expt:
        print(expt.stderr.decode())
        sys.exit(-1)


def execute(command, env=None):
    """
        Executes a command with credentials in the environment.
        env is in the form of ['ENV=VALUE', ]
    """

    if env is None:
        env = []
    envs = dict()
    for option in env:
        name, value = str.split(option, '=')
        envs[name] = value

    update_env_and_fork(command, envs)