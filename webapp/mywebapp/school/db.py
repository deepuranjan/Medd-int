import pickle
from django.conf import settings
import os

DB_FILE_NAME = os.path.join(settings.DB_FILE_PATH, 'StudentRecord.p')


def read_entry(student_id=None):
    try:
        if os.path.getsize(DB_FILE_NAME) > 0:
            with open(DB_FILE_NAME, "rb+") as f:
                obj = pickle.load(f)
                if student_id is None:
                    return obj
                elif student_id not in obj:
                    return None
                else:
                    return obj[student_id]
    except IOError:
        print("Record doesn't exist please add  your entry")
        return None


def write_entry(obj):
    try:
        content = {}
        if os.path.exists(DB_FILE_NAME) and os.path.getsize(DB_FILE_NAME) > 0:
            with open(DB_FILE_NAME, 'rb+') as f:
                content = pickle.load(f)
            with open(DB_FILE_NAME, 'wb') as f:
                content[obj.student_id] = obj
                pickle.dump(content, f)
        else:
            with open(DB_FILE_NAME, 'wb') as f:
                content = {}
                content[obj.student_id] = obj
                pickle.dump(content, f)
        return True

    except IOError as e:
        print("Unable to write the data {}".format(e))
        return False


def delete_entry(student_id):
    try:
        if os.path.exists(DB_FILE_NAME) and os.path.getsize(DB_FILE_NAME) > 0:
            with open(DB_FILE_NAME, "rb+") as f:
                content = pickle.load(f)

            with open(DB_FILE_NAME, 'wb') as f:
                if content.get(student_id):
                    del content[student_id]
                    pickle.dump(content, f)
                    return True
                else:
                    return False

        return False
    except IOError:
        print("Invalid Input..!")
