import pytest
from scr import sql_bot

@pytest.fixture(autouse=True)
def db():
    db = sql_bot.My_db('test_bd', '192.168.0.102', 'mikhaylov_yv')
    return db

def test_conect(db):
    assert db.do_request('SELECT CURRENT_USER;').values[0][0] == 'mikhaylov_yv@192.168.0.103'

def test_insert_sensors(db):
    add = """INSERT INTO light_sensors(NAME_SENSOR)
    VALUES('test mashine')
    """
    db.cursor.execute(add)
    db.con.commit()
    # print(db.do_request('select * from light_sensors;'))

def test_insert_light_data(db):
    val = 50
    db.add_light(228, val)
    print(db.do_request('select * from light;'))