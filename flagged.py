import subprocess

from flask import request


def run_from_request():
    cmd = request.args.get("cmd")
    return subprocess.check_output(cmd, shell=True)
