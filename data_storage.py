import time
import shelve

shelve_file_name = 'last_update'
LAST_UPDATE_KEY = 'last_update'

last_updated = time.mktime(time.localtime())

def get_last_updated_time():
    result = last_updated
    with shelve.open(shelve_file_name) as storage:
        if LAST_UPDATE_KEY in storage:
            result = storage[LAST_UPDATE_KEY]
        storage.close()
    return result

def save_last_updated_time():
    last_updated = time.mktime(time.localtime())
    with shelve.open(shelve_file_name) as storage:
        storage[LAST_UPDATE_KEY] = last_updated
        storage.close()
