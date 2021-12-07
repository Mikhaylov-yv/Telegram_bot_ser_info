# import numpy as np
import subprocess


class Light_info:

    def get_light(self):
        return subprocess.run('ls', capture_output=True).stdout






if __name__ == '__main__':
    l_inf = Light_info()
    print(l_inf.get_light())