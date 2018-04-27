# OpenSSL-Message-Board
A secure message board written with OpenSSL and Python for CS419 S2018

Groups Members
  - David Parsons (dwp35)
  - Fahad Syed (fbs14)
  - Michael Allen (mwa27)
  - Kaitlin Coventry-Cox (klc223)
  
For this project we used Python3 in order to implement the client and server. The server checks that a user is authenticated and makes use of timeouts for clients. The client does the same thing but accepts the commands as specified in the directions. When the client is first started the user is prompted for their username and password. If the user does not yet exist, the password entered is added to the user_db.txt file but is salted and hashed in order to protect the passwords especially in the case of duplicate passwords. If the username entered already exists, the password is checked against the password for that given username that is saved in the user_db.txt file. Once authenticated, the GET, POST, and END commands become available. You can get any of the existing groups, or post to an existing group or create a new group. If you post go a group that does not yet exist, it is created as a new group. In each group whatever messages that are posted are saved with a timestamp and the username of the user that posted it so it can be viewed by either the same user or others later. Our clients can be run at the same time and we implemented multithreading for this process. Some things we tested include:

  -Create a username and password 
  -Use already created username with an invalid password
  -Run each command with just one user
  -Create New Group 
  -Input invalid group name
  -Post blank messages
  -Changing the server’s certificate information 

Some things to note about our implementation/testing include:

  -Blank messages are allowed to post
  -Invalid group name should just go back to the “enter a command” screen
  -Changing the server’s certificate information should cause the connection to be rejected and the client to exit
  -We also tried to access the password file from the client but could not find a way to do so

