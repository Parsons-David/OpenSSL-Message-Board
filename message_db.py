#!/usr/bin/python3
import threading
import state, copy
import os
import json
import datetime
lock = threading.Lock()
db = "db.json"

# Returns an array of strings representing the group names
# of all the groups stored in the database
# ex: return ["CS", "Math", "Physics", "Security", "Art", "Music", "Sports"]

def build_dict():
    open(db, 'a+')
    with open(db, 'r+') as json_file:
        string = json_file.read()
        json_file.close()
        if string == "":
            return {}
        else:
            dict = json.loads(string)
            return dict

def write_file(board):

    with open(db, 'a') as myfile:    
        myfile.seek(0)
        myfile.truncate()
        myfile.write(json.dumps(board))
        myfile.close()

def get_groups():
    grouplist = []
    lock.acquire()
    board = build_dict()
    try:
        for group in board:
            grouplist.append(group)
    finally:
        lock.release()
    return grouplist

# Returns an array of Dictonaries representing the messages stored
# in the databse for the given group.
# The Dictonary structure can be seen above.
def get_messages(group):
    # return db.get_messages(group)
    
    pm = copy.deepcopy(state.get_message)
    pm["GROUP"] = group
    retval = []
    lock.acquire()
    board = build_dict()
    try:
        if group in board:
            retval = copy.deepcopy(board[group])
    finally:
        lock.release()
    return retval

# Adds a new message to a given group, cretes the
# group if it does not yet exist
# DOES NOT RETURN ANYTHING
def post_message(username, group, message):
    
    pm = { "MESSAGE" : "" }
    pm["MESSAGE"] = message
    pm["USERNAME"] = username
    pm["TIMESTAMP"] = datetime.datetime.now().time().isoformat()
    
    lock.acquire()
    try:
        board = build_dict()
        if group not in board:
            board[group] = [pm]
        else:
            msglist = board[group]
            msglist.append(pm)
            board[group] = msglist
        write_file(board)
    finally:
        lock.release()
    

# Write your testing in here
def main():
    print("posting.")
    message = [{
        "COMMAND" : "open",
        "BODY" : "this is a test!"
    }]
    
    print(message)
    
    post_message("fahad", "CS", message)
    post_message("fahad", "PIZZA", message)
    messages = get_messages("CS")
    
    print("getting")
    for mes in messages:
        print(mes)
    
    print("getting groups")
    grouplist = get_groups()
    for g in grouplist:
        print(g)

if __name__ == '__main__':
    main()
