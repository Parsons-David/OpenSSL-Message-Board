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
    "AUTHENTICATED" : False
}

# End Authentication

# GET
# End GET

# POST
# End POST

# END
end_message = {
    "END_SESSION" : True
}

end_response = {
    "SESSION_ENDED" : True
}
# End END
