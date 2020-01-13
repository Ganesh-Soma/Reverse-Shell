# Reverse-Shell
This project contains python scripts to code a reverse shell instead of using automated tools

## Usage 1
Make sure to be connected to the same network as the victim machine.
If using VM as a target machine, set the network type to Bridged network.

Eg : 
Kali Machine (Attacker Machine)
Windows Machine ( Victim Machine )


Step 1 : Run the server.py script on the kali(attacker) machine - python3 server.py



Note: 
- Before running the client side script, ping the ip of the attacker to make sure of the connectivity.
- Also, after running the server side script, run netstat -antp | grep 8080 to check if the listener is up and listening to incoming requests.

Step 2: Run the client.py script on the windows(victim) machine - python3 client.py

On doing so, you should receive a shell on the attacker side.

Once the shell is up and running, 
You should see something like this:

[+] We got a connection from ('192.168.x.x', <port_no> )
Shell > 

Hurray! You have set up a reverse shell and are now ready to execute commands on the target!

## Usage 2
The idea of coding a low level file transfer instead of using protocols (like FTP) is to avoid detection. So, instead of making a new channel and a new connection each time we want to transfer a file, which could bring attention. So, the idea here is to transfer the file within the same channel. 
To do so, once the reverse shell is obtained, run -> grab*<file_path>

If you want to change the splitter from * to something else, feel free to change the code!  :D
