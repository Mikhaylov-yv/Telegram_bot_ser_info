import pytest
from scr.get_sistem_data import get_text_with_consol, lod_jeson, save_to_csv
from scr.light_info import Light_info


@pytest.mark.parametrize(
    "text",
    ['helo world', 'привет мир', 'I\nwhiz\nbobr'],
)
def test_get_text_with_consol(text):
    comand = f"echo '{text}'"
    result = get_text_with_consol(comand)
    assert result == text

@pytest.fixture(autouse=True)
def test_open_jeyson(light_jeyson):
    result = get_text_with_consol(f"echo '{light_jeyson}'")
    assert result == light_jeyson
    return result


def test_lod_jeson(light_jeyson):
    result = lod_jeson(light_jeyson)
    assert type(result).__name__ == 'list'
    for _ in result:
        assert type(_).__name__ == 'dict'

def test_lod_jeson(light_jeyson_one):
    result = lod_jeson(light_jeyson_one)
    assert type(result).__name__ == 'list'
    assert len(result) == 1
    assert type(result[0]).__name__ == 'dict'


@pytest.mark.parametrize(
    "text",
    ['31.01.20 21:00 40', '31.01.20 21:15 45', '31.01.20 21:30 50'],
)
def test_save_to_csv(text):
    save_to_csv(path='../data/test_light_info.csv', text = text)



# Тест работы всего процесса по сценарию
# Запрос 5 результатов измерения света
# Получение медианы
# Запись в csv файл значения с индексащией по времени.

def test_main_from_test_data(light_jeyson):
    obj = Light_info(step_min = 0.001, test=True)
    obj.comand = f"echo '{light_jeyson}'"
    obj.save_light(path='../data/test_light_info.csv')
