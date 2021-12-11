import subprocess

def get_text_with_consol(comand):
    result = subprocess.run(comand, shell=True, stdout=subprocess.PIPE).stdout

    return result.decode('utf8')[:-1]