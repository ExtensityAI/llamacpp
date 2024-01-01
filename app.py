import subprocess


def run():
    subprocess.call(['python', '-m', 'llama_api_server', '--host=0.0.0.0'])


if __name__ == '__main__':
    run()
