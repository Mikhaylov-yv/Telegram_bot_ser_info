import subprocess
import ast

def get_text_with_consol(comand):
    result = subprocess.run(comand, shell=True, stdout=subprocess.PIPE).stdout

    return result.decode('utf8')[:-1]

def lod_jeson(text, l = 9 ):
    result_list = text.splitlines(True)
    result_list = [''.join(result_list[i:i+l]) for i in  range(0, len(result_list), l)]
    result_list = [ast.literal_eval(text) for text in result_list]
    return result_list

def save_to_csv(path, text):
    with open(path, 'a') as f:
        f.write('\n' + text)

