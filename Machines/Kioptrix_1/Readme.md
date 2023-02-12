<h1>Kioptrix_1 Walkthrough</h1>


<h2>Description</h2>
A write up on how to get root in Kioptrix level 1 machine found in vulnhub. It is useful to learn about basic exploitation and vulnerability enumeration.
<br />


<h2>Utilities and Technologies Used</h2>

- <b>Virtual box</b>
- <b> Kioptrix_1 Machine </b>
- <b>Nmap</b>
- <b>Nikto</b>
- <b>Metasploit</b>



<h2>Environments Used </h2>

- <b>Kali linux</b>

<h2> Walkthrough </h2>

1. Download the vulnerable Kioptrix Machine from vulnhub.
2. Import the virtual machine into Virtual box. In settings make sure the network is NAT network.
3. Verify your kali machine is on the same network in settings.
4. Discover the IP address of new machine in kali using command: sudo arp-scan -l 
5. Run a nmap and nikto scan against the machine. <br/> <img src="Nmap_Scan.png?raw=true" width="800" height="500" /> <br/> <img src="Nikto_Scan.png?raw=true" width="800" height="800" />
6. Nikto shows that the machine is vulnerable to the mod_ssl 2.8.4. Enumerating this will lead to the manual exploitation of Open****.
7. Enumerate the SMB port to get the trans2open exploit.
7. Metasploit exploitation: Search for trans2open, set rhosts, set payload and run the exploit to get the root.
8. Manual Exploitation: Download  the github code for it and follow the instructions in the code and run it to get root.
  


<h2> Credits </h2>
To all the tool and environment creators and also the blog pages which helped me when I got stuck. Can be found underneath in the vulnhub page.

