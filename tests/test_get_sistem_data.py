import pytest
from scr.get_sistem_data import get_text_with_consol



@pytest.mark.parametrize(
    "text",
    ['helo world', 'привет мир', 'I\nwhiz\nbobr'],
)
def test_get_text_with_consol(text):
    comand = f"echo '{text}'"
    result = get_text_with_consol(comand)
    assert result == text