#!/usr/bin/python3

# Returns an array of strings representing the group names
# of all the groups stored in the database
# ex: return ["CS", "Math", "Physics", "Security", "Art", "Music", "Sports"]
def get_groups():
    pass

# Example Message Dictionary
# {
#     "USER": "PK",
#     "TIMESTAMP" : "NOW",
#     "MESSAGE" : "WHAT IS UP!!"
# }

# Returns an array of Dictonaries representing the messages stored
# in the databse for the given group.
# The Dictonary structure can be seen above.
def get_messages(group):
    # return db.get_messages(group)
    return [{
        "USER": "PK",
        "TIMESTAMP" : "NOW",
        "MESSAGE" : "WHAT IS UP!!"
    }]

# Adds a new message to a given group, cretes the
# group if it does not yet exist
# DOES NOT RETURN ANYTHING
def post_message(group, message):
    pass

# Write your testing in here
def main():
    pass

if __name__ == '__main__':
    main()
