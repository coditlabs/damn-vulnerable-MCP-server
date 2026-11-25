import requests
import subprocess


def fetch_and_run(url):
    cmd = requests.get(url).text
    return subprocess.check_output(cmd, shell=True)
