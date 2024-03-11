from datetime import datetime as dt


def get_cur():
    now = str(dt.now())
    _data, _time = now.split(' ')
    return _data.replace('-','.'), _time.split('.')[0]
