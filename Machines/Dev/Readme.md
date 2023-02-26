<h1>Dev Walkthrough</h1>


<h2>Description</h2>
A write up on how to get root in Dev vulnerable machine found in the Practical Ethical Hacking Course by TCM Security. Useful for learning about basic web application exploitation and sudo based zip privilege escalation.
<br />


<h2>Utilities and Technologies Used</h2>

- <b>Virtual Box</b>
- <b> Dev Machine </b>
- <b>Nmap</b>
- <b>Nikto</b>
- <b>ffuf</b>
- <b>fcrackzip</b>


<h2>Environments Used </h2>

- <b>Kali linux</b>

<h2> Walkthrough </h2>

1. Download the Dev vulnerable machine from the PEH capstone by TCM security.
2. Import the vulnerable machine into virtual box with the help of the import appliance option. Set the networking option to NAT network for the machine in settings. Add the number of processors to 2 ( according to preference).
3. Either log into the machine with the provided credentials or use arp-scan -l to find the ip address of the machine.
4. Scan the machine with nmap and nikto. <br/> <img src="nmap.png?raw=true" width="800" height="500" /> <br/> <img src="nikto.png?raw=true" width="800" height="500" />
5. Run a directory busting with your preffered tool to find hidden pages. <br/> <img src="ffuf.png?raw=true" width="800" height="500" /> <br/> <img src="ffuf_1.png?raw=true" width="800" height="500" />
6. Enumerate the nfs port. <br/> <img src="nfs_enum.png?raw=true" width="800" height="100" />
7. Mount the nfs share to your device, to find a zip inside it.
8. Crack the zip using fcrackzip. <br/> <img src="fcrackzip.png?raw=true" width="800" height="100" />
9. Use the password to unzip and read the contents. <br/> <img src="todo.png?raw=true" width="800" height="500" />
10. Enumerate the web app on ports 80 and 8080 to find hidden password and boltwire installation page.
11. Exploit the boltwire cms page with the exploit in this page. (https://www.exploit-db.com/exploits/48411) <br/> <img src="boltwire_exploit.png?raw=true" width="800" height="500" />
12. Use this to enumerte the usernames. With this information and the id_rsa gotten previously ssh into the device. <br/> <img src="initial_fothold.png?raw=true" width="800" height="500" />
13. Checking history gives hint that the user has a sudo privilege with zip.
14. Use this to escalate privilege to root with the exploit in gtfobins or this website. (https://www.hackingarticles.in/linux-for-pentester-zip-privilege-escalation/)<br/> <img src="escalation.png?raw=true" width="800" height="500" />
15. Cat out the flag.txt in the root folder.


<h2> Credits </h2>
To all the tools, exploits and environment creators and also TCM Security for the Practical Ethical Hacking Course .
