#!/usr/bin/python3
import threading
import state, copy
lock = threading.Lock()
board = {}

# Returns an array of strings representing the group names
# of all the groups stored in the database
# ex: return ["CS", "Math", "Physics", "Security", "Art", "Music", "Sports"]
def get_groups():
    grouplist = []
    lock.acquire()
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
    lock.acquire()
    pm = copy.deepcopy(state.get_message)
    pm["GROUP"] = group
    retval = []
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
    
    lock.acquire()
    pm = copy.deepcopy(state.post_message)
    pm["GROUP"] = group
    pm["USERNAME"] = username
    pm["MESSAGE"] = message
    try:
        if group not in board:
            print "does not exist."
            board[group] = [pm]
        else:
            print "exists."
            msglist = board[group]
            msglist.append(pm)
            board[group] = msglist
    finally:
        lock.release()
    

# Write your testing in here
def main():
    print "posting."
    message = [{
        "COMMAND" : "open",
        "BODY" : "this is a test!"
    }]
    
    print message
    
    post_message("fahad", "CS", message)
    post_message("fahad", "PIZZA", message)
    messages = get_messages("CS")
    
    print "getting"
    for mes in messages:
        print mes
    
    print "getting groups"
    grouplist = get_groups()
    for g in grouplist:
        print g

if __name__ == '__main__':
    main()
