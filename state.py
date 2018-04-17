# Netwok Messages
MESSAGE = {
    "COMMAND" : "",
    "BODY" : ""
}

# Commands
AUTHENTICATE = "AUTHENTICATE"
GET = "GET"
POST = "POST"
END = "END"

# Authentication

# Dictonary that holds plain text
# username and password entered by user
username_password = {
    "USERNAME" : "",
    "PASSWORD" : ""
}

# Authentication response from the server
# AUTHENTICATED represents a succesful authentication
# TODO : Created vs Authenticated vs Failed?
authentication_response = {
    "AUTHENTICATED" : False,
    "GROUPS" : []
}

# End Authentication

# GET
get_message = {
    "GROUP" : ""
}

get_response = {
    "GROUP" : "",
    "MESSAGES" : [],
    "GROUPS" : []
}

# End GET

# POST
post_message = {
    "GROUP" : "",
    "MESSAGE" : ""
}

post_response = {
    "GROUPS" : []
}
# End POST

# END
end_message = {
    "END_SESSION" : True
}

end_response = {
    "SESSION_ENDED" : True
}
# End END
