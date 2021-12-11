import pytest
from scr.get_sistem_data import get_text_with_consol, lod_jeson



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

# Тест работы всего процесса по сценарию
# Запрос 5 результатов измерения света
# Получение медианы
# Запись в csv файл значения с индексащией по времени.

def test_main_from_test_data(test_open_jeyson):
    print(test_open_jeyson)

