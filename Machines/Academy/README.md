<h1>Academy Walkthrough</h1>


<h2>Description</h2>
A write up on how to get root in Academy vulnerable machine found in the Practical Ethical Hacking Course by TCM Security. Useful for learning about basic file upload vulnerability and cron job based privilege escalation.
<br />


<h2>Utilities and Technologies Used</h2>

- <b>Virtual Box</b>
- <b> Academy Machine </b>
- <b>Nmap</b>
- <b>LinPEAS</b>
- <b>ffuf</b>
- <b>pspy</b>


<h2>Environments Used </h2>

- <b>Kali linux</b>

<h2> Walkthrough </h2>

1. Download the Academy vulnerable machine from the PEH capstone by TCM security.
2. Import the vulnerable machine into virtual box with the help of the import appliance option. Set the networking option to NAT network for the machine in settings. Add the number of processors to 2 ( important, can cause the VM to not boot).
3. Either log into the machine with the provided credentials or use arp-scan -l to find the ip address of the machine. <br/> <img src="arp_scan.png?raw=true" width="800" height="500" />
4. Scan the machine with nmap and nikto. <br/> <img src="nmap.png?raw=true" width="800" height="500" /> <br/> <img src="nikto.png?raw=true" width="800" height="500" />
5. Run a directory busting with your preffered tool to find hidden pages. <br/> <img src="directory_busting.png?raw=true" width="800" height="500" />
6. Enumerate the ftp port. <br/> <img src="ftp.png?raw=true" width="800" height="500" />
7. Go through the note to get credentials for the website. (hint: the password is hashed.) <img src="note.png?raw=true" width="800" height="500" /> <br/> <img src="hashes.png?raw=true" width="800" height="500" />
8. Login the page, to find a file upload page in the profile. Use it to get a reverse shell to your machine (The payload can be any reverse shell php according to your choice, I personally used the pentester monkey's one). <br/> <img src="initial_access.png?raw=true" width="800" height="500" />
9. Transfer LinPEAS into the new machine (use simple python server or any other preffered method, might need to go into the tmp folder for read and write permissions) and run it to get credentials for another user on the machine. <br/> <img src="python_server.png?raw=true" width="800" height="500" /> <br/> <img src="linpeas.png?raw=true" width="800" height="500" /> 
10. Use this credentials to ssh into the machine and run LinPEAS again to find a vulnerable cron job. <br/> <img src="ssh.png?raw=true" width="800" height="500" />
11. Verify it using the tool pspy to find all the running cron jobs. <br/> <img src="pspy.png?raw=true" width="800" height="500" />
12. Use it to run a reverse shell with root access.<br/> <img src="Rooted.png?raw=true" width="800" height="500" />


<h2> Credits </h2>
To all the tool and environment creators and also TCM Security for the Practical Ethical Hacking Course .
