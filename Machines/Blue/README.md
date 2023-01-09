<h1>Blue Walkthrough</h1>


<h2>Description</h2>
A write up on how to get root in Blue vulnerable machine found in the Practical Ethical Hacking Course by TCM Security. Useful for learning about the eternal blue exploit.
<br />


<h2>Utilities and Technologies Used</h2>

- <b>Virtual Box</b>
- <b> Blue Machine </b>
- <b>Nmap</b>
- <b>Metasploit</b>
- <b>Autoblue</b>


<h2>Environments Used </h2>

- <b>Kali linux</b>

<h2> Walkthrough </h2>

1. Download the blue vulnerable machine from the PEH capstone by TCM security.
2. Import the vulnerable machine into virtual box with the help of the import appliance option. Set the networking option to NAT network for the machine in settings.
3. Either log into the machine with the provided credentials or use arp-scan -l to find the ip address of the machine.
4. Scan the machine with nmap. <br/> <img src="nmap.png?raw=true" width="800" height="500" />
5. Enumerate the open ports to find port 445 running smb with windows 7 ultimate sp1.
6. Search for exploits to find that it is vulnerable to MS17-010 Eternal Blue. Now you have two ways to get root either the automatic way or the manual way.
7. Automatic way using metasploit: <br/>
  a. Run msfconsole. <br/>
  b. Search for eternalblue. <br/> <img src="msfconsole_eternalblue.png?raw=true" width="800" height="400" /> <br/>
  c. Set options by setting the Rhosts. <br/> <br/> <img src="msfconsole_options.png?raw=true" width="800" height="400" /> <br/>
  d. Run the exploit to get a meterpreter shell. <br/> <img src="msfconsole_run.png?raw=true" width="800" height="400" /> <br/>
  e. Run command getuid to see your access level. <br/> <img src="output.png?raw=true" width="800" height="100" /> <br/>
8. Manual way: <br/>
  a. Search for eternal blue exploits in google. <br/>
  b. Look for blogs and github sources for exploit script.( I have used the autoblue exploit found here:https://github.com/3ndG4me/AutoBlue-MS17-010 ). <br/>
  c. Follow the steps in your chosen exploit script. <br/>
9. Further post-exploitation can be done using hashdump, installing backdoor and much more.


<h2> Credits </h2>
To all the tool and environment creators and also TCM Security for the Practical Ethical Hacking Course .
