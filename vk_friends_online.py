#!/usr/bin/env python3

import vk
from getpass import getpass
import sys


APP_ID = 6273768


def get_user_login():
    return input('Enter login: ')


def get_user_password():
    return getpass()


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    vk_api = vk.API(session)
    return vk_api.getProfiles(user_ids=vk_api.friends.getOnline())


def output_friends_to_console(list_friends_online):
    for number, online_friend in enumerate(list_friends_online, 1):
        print("{}) {f[first_name]} {f[last_name]}".format(
            number, f=online_friend))
        

if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
