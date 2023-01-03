<h1>Kioptrix_4 Walkthrough</h1>


<h2>Description</h2>
A write up on how to get root in Kioptrix level 4 machine found in vulnhub. It is useful to learn about mysql UDF privilege escalation.
<br />


<h2>Utilities and Technologies Used</h2>

- <b>Hyper-V</b>
- <b> Kioptrix_4 Machine </b>
- <b>Nmap</b>
- <b>Nikto</b>
- <b>smbclient</b>
- <b>Linenum.sh</b>


<h2>Environments Used </h2>

- <b>Kali linux</b>

<h2> Walkthrough </h2>

1. Download the vulnerable Kioptrix Machine from vulnhub. (https://www.vulnhub.com/entry/kioptrix-level-13-4,25/)
2. Create a new generation 1 virtual machine in hyper-V and connect the virtual hard disk to it. In settings remove the default network adapter and add the legacy network adapter.
3. Connect the network adapter and your kali machine to the same network in settings.
4. Discover the IP address of new machine in kali using command: sudo arp-scan -l
5. Run a nmap and nikto scan against the machine.
6. Enumerate the apache server and smb ports.
7. Enumerating the smb port gives you the usernames in the machine.
8. There are no public shares to connect in the smb.
9. The Apache server gives a login page which has sql injection vulnerability.
10. Use the vulnerability to get the passwords for the user.
11. Use this to ssh into the system.
12. Escape the limited shell with the command: echo os.system('/bin/bash')
13. Transfer the Linenum.sh from the kali and run it.
14. We see the mysql server can be accessed without root password and is running as root user. Therefore we can misuse it to get root privileges using mysql UDF vulnerability.
15. Use the command select sys_exec('usermod -a -G admin john') to add the user john to the admin group.
16. Now exit and login again with sudo su to get root privilege.


<h2> Credits </h2>
To all the tool and environment creators and also the blog pages which helped me when I got stuck. Can be found underneath in the vulnhub page.


<figure><img src="scanner_1.png?raw=true" width="500" height="500" /><figcaption>Output</figcaption></figure> 

