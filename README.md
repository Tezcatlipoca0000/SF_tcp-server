# Work IN PROGRESS...


### TCP Server for transfering 1 or all of the files in a folder

###### Server:
Sends the files to the Client.

Files to send must be copied in the "*send*" folder.

###### Client: 
Receives the files sent by the server. 

Files received will end up in the "*receive*" folder.

###### TODO:
- Client-side:
    - Maybe an input of IP. If left blank then localhost

###### Notes:
    - The value of "dir" in SF_Server.py **must** point to the "send" folder in your device. Apropiate editing must be done.

    - The value of src1 and src2 are the address of important files I want my server to provide and generate a recent copy for the client. It won't break the program if you leave the value as is.