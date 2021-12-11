"""Pytest configuration."""

import pytest

@pytest.fixture(autouse=True)
def light_jeyson_one():
    return """{
  "light-bh1745": {
    "values": [
      42,
      10000,
      25
    ]
  }
}
"""

@pytest.fixture(autouse=True)
def light_jeyson():
    return """{
  "light-bh1745": {
    "values": [
      42,
      10000,
      25
    ]
  }
}
{
  "light-bh1745": {
    "values": [
      42,
      10000,
      25
    ]
  }
}
{
  "light-bh1745": {
    "values": [
      42,
      10000,
      25
    ]
  }
}
{
  "light-bh1745": {
    "values": [
      41,
      10000,
      25
    ]
  }
}
{
  "light-bh1745": {
    "values": [
      42,
      10000,
      25
    ]
  }
}
"""