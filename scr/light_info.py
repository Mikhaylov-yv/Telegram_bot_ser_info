# import numpy as np
import subprocess
from scr.get_sistem_data import get_text_with_consol, lod_jeson, save_to_csv
import time
from datetime import datetime
import statistics
from scr.sql_bot import My_db

class Light_info:
    def __init__(self, step_min = 15, test = False):
        self.step_min = step_min
        self.test = test
        self.db = My_db(db='SmartHouse', host = 'localhost', user = 'home_bot')
        self.get_comand()


    def get_comand(self):
        self.comand = 'termux-sensor -s "light-bh1745" -n 5'


    def save_light(self, path):
        w = True
        i = 0
        while w == True:
            result = lod_jeson(get_text_with_consol(self.comand))
            vals = []
            for res in result:
                vals.append(res['light-bh1745']['values'][0])
            light = int(statistics.mean(vals))
            # Сохранение в csv файл
            # sring_out = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\t{light}"
            # save_to_csv(path, sring_out)
            # Сохранение в базу данных
            self.db.add_light(id = 1, light = light)
            # Выход при тестовом запуске
            if self.test == True and i >= 5: break
            time.sleep(self.step_min * 60)
            i += 1






if __name__ == '__main__':
    l_inf = Light_info()
    l_inf.save_light(path='../data/light_info.csv')