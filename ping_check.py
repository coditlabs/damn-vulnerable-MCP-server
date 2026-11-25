import subprocess

from flask import request


def ping():
    host = request.args.get("host")
    return subprocess.check_output(["ping", "-c", "1", "--", host])
