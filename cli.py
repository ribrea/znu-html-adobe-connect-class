#!/usr/bin/python
import requests
from dotenv import load_dotenv
from os import environ

load_dotenv()


def class_link(class_id):
    return 'https://lms.znu.ac.ir/mod/onlineclass/view.php?id={class_id}&action=join'.format(class_id=class_id)


def get_nice_link(class_id, cookies=None):
    r = requests.get(class_link(class_id), cookies=cookies, allow_redirects=False)

    if not r.next:
        raise Exception("Invalid class_id")

    if "login" in r.next.url:
        raise Exception("Session expired")

    return r.next.url + "&proto=true"


def get_moodle_session(cookie: str):
    return {'MoodleSession': cookie}


def main():
    cookie = environ.get('COOKIE', None)
    class_ids = environ.get('CLASS_IDS', None)

    if not cookie:
        cookie = str(input("Please require Your cookie: "))
    if not class_ids:
        class_ids = str(input("Please require Your class_ids: "))

    class_ids = class_ids.strip().split(',')

    cookie = get_moodle_session(cookie)

    for class_id in class_ids:
        print(get_nice_link(class_id, cookie))


if __name__ == "__main__":
    main()
