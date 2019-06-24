from subprocess import PIPE, run


def out(command):
    result = run(
        command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True
    )
    return result.stdout
