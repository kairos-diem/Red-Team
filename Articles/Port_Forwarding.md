I first came across the concept of port forwarding when going through a video by PHD security on Youtube. In order to understand port forwarding and its use cases, we must first understand about ports, proxy servers and SOCKS servers. 

1. Ports : Just like how in an apartment complex each apartment has a designated mailbox, the computer has a predefined ports for each services it runs. 
2. Proxy servers : It is a machine that acts a middle man between the user and the network.
3. SOCKS servers: SOCKS which stand for Socket secure is a secure TCP implementation of proxy servers. 

Now we are ready to understand about Port forwarding. Port forwarding is the process of mapping ports of a remote machine to your local machine, thereby making it accessible for a user to control the data and services running on the remote machine. This is implemented with the help of the protocols ssh and rdp. It also gives you the added capability of running native tools on your machine against the ports of the remote machine. Port forwarding is generally used in Backups, CCTV cameras, torrenting, game servers and much more. There are three types of port forwarding local, remote and dynamic. 

1. Local port forwarding is when a single port of a remote server are mapped to your local machine. In Linux, with ssh enabled you can map remote ports to your machine with the following command:
    
    Syntax : ssh -L [remote_port]:[remote_IP]:[local_port] [local_IP]
    
    Example : ssh -L 6900:192.168.199.153:80 localhost
    
2. Remote port forwarding is the reverse of the above, where a local port is forwarded to a remote server. In Linux, first enable the remote server to accept the port forwarding by editing the /etc/sshd_config file. Change GatewayPorts option to yes and restart the server. Once set up, run the following command:
    
    Syntax : ssh -R [remote_port]:[local_IP]:[local_port] [remote_IP]
    
    Example : ssh -R 9999:localhost:80 192.168.199.153
    
3. Dynamic port forwarding is when the full range of TCP ports of a remote server are made accessible with the help of SOCKS proxy server. In Linux, Edit the file /etc/proxychains.conf. Set up by default on kali on port 9050, otherwise follow the link in the sources given below. Then run the following command:
    
    Syntax : ssh -D [local_IP]:[local_port] [user]@SSH_SERVER
    
    Example : ssh -D 9090 -N -f user@remote.host
    
    Notes: 
    
    1. When the [local_IP] is omitted, the ssh client binds on localhost. 
    2. When the defined port is 9050, we can run tools like nmap on the internal machines with the help of adding proxychains command. Check the video by PHD security for more info. Also check out information regarding jumping and double jumping in the same video.
    3. Dynamic port forwarding, can also be leveraged to implement jump boxes to access other machines inside the private subnet. Jump boxes as the name suggests are machines which act as jumping points which allow the user to access machines in the internal subnet.  Syntax : ssh -J user1@[machine1_IP] -D [local_IP]:[local_port] user2@[machine2_IP]

In windows, SSH port forwarding is setup with the help of PuTTY SSH client. Detailed steps can be found in the source links.


Sources:

[PHD security - Port forwarding video](https://www.youtube.com/watch?v=-yACoZ1ctHk)

[https://learn.g2.com/port-forwarding](https://learn.g2.com/port-forwarding)

[https://www.tecmint.com/create-ssh-tunneling-port-forwarding-in-linux/](https://www.tecmint.com/create-ssh-tunneling-port-forwarding-in-linux/)

[https://linuxhint.com/ssh-port-forwarding-linux/](https://linuxhint.com/ssh-port-forwarding-linux/)

[https://linuxize.com/post/how-to-setup-ssh-tunneling/](https://linuxize.com/post/how-to-setup-ssh-tunneling/)

[https://www.geeksforgeeks.org/how-to-setup-proxychains-in-linux-without-any-errors/](https://www.geeksforgeeks.org/how-to-setup-proxychains-in-linux-without-any-errors/)

Disclaimer: I have just aggregated this information from various articles and videos, Hence all credits to the makers of the respective content.
