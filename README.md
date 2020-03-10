# VoIP-Sniffer

VoIP Sniffer is a python script set to run on an raspberry pi. The script aims at intercepting VoIP packets inside a network environment. The packets are captured and stored in pcap which can further be analyzed for call replaying, identification of SIP extensions etc inside wireshark.

Configurign Raspberry pi..
VNC has been the best way to access any computer remotely on the same network. Recently, VNC Connect also came out to make it easy to access your Raspberry Pi from anywhere using a cloud connection. Once it’s set up, you can access your Raspberry Pi’s graphic interface from any other computer or smartphone using the VNC Viewer app.
VNC Connect comes packed in for free with the most recent versions of the Raspberry Pi operating system. 
VNC can be set up in few simple steps. Open up a terminal and run the following commands:
$ sudo apt-get update
$ sudo apt-get install realvnc-vnc-server realvnc-vnc-viewer
Once that’s complete, type in 
$ sudo raspi-config 
and press Enter. Scroll down to VNC and set it to Enabled.
Once that’s finished downloading, you can set up VNC Connect:
    • Head to the RealVNC Raspberry Pi sign up page and enter your email address in the sign up box.
    • Follow the on-screen instructions to finish setting up your account with a password.
    • Back on your Raspberry Pi, click the VNC icon in the top-right corner of the screen to open VNC. Then click the status menu and select Licensing.
    • Enter the email address and password you created in step one.
    • When prompted, select “Direct and cloud connectivity.” Your Raspberry Pi is now accessible online.
    • Download the VNC Viewer application on the computer you want to control the Raspberry Pi from, like the laptop or smartphone you’ll have when you travel.
Open the VNC Viewer application and enter the credentials you created in step one.
Your Raspberry Pi will pop up as an option automatically. Select it to open up the connection. When prompted, enter your Raspberry Pi’s username and password (by default this is the username “pi” and “toor” raspberry). Within a few second it’ll connect.
You’re now able to log into your Raspberry Pi’s graphic desktop from anywhere as long as your Raspberry Pi has internet access.
5.2 Installing Required Packages 
The following packages need to be installed as the would be needed by our custom script.
Let’s begin by install tcpdump.
Tcpdump is a common packet analyser that runs under the command line. It allows the user to display TCP/IP and other packets being transmitted or received over a network to which the computer is attached. Distributed under the BSD license, tcpdump is free software. 
$ sudo apt-get install tcpdump -y
Now user needs to install Ettercap. We will be using Ettercap text only version for ARP Spoofing.
Ettercap is a free and open source network security tool for man-in-the-middle attacks on LAN. It can be used for computer network protocol analysis and security auditing. It runs on various Unix-like operating systems including Linux, Mac OS X, BSD and Solaris, and on Microsoft Windows.
$ sudo apt-get install Ettercap-text-only -y
Next up, user needs to install python PyDrive library which will be useful for pushing files to the google drive.
PyDrive is a wrapper library of google-api-python-client that simplifies many common Google Drive API tasks. 
$ pip install PyDrive

Head towards https://console.developers.google.com/apis/ . Create a new project and inside this project enable Google Drive API. Download the clientID json file and replace the client-secrets.json.example with your json file.
Lets, begin with exploitation now..

Inside upload.py file, replace "path_to_download" string with path to user's download folder.

The first step is to find the IP address of softphone, for that the investigator needs to run a nmap scan.
Once the IP address is known, the investigator needs to proceed by calling the custom python script which we have named as “sip_exploitation.py”.
Sip_exploitation.py will ask for victim IP address. Enter the softphone IP address found through nmap scan.
The script will then try to perform an ARP spoof on the victim using Ettercap API.

Consecutively, the script will also try to capture UDP packets belonging to the victim. Once the packet capture is completed the script will try to upload the pcap file on to google drive.

A web browser will be prompted asking to choose an account to which the script would be updated.

Note: Network congestion issues were seen when the script tried to upload the pcap on the drive. To avoid this, it is advisable to force shut the thread performing ARP spoofing once the packet capture is completed. For this press “Ctrl+C” on the terminal instance performing ARP spoofing.

Now open the packet capture file in wireshark.
For viewing all VoIP packets, apply the following filter “sip || rtp”.

For viewing the call packets, go to Telephony -> VoIP Calls

Select the VoIP call and click on “Play Stream”.
Here, the investigator will be able to hear the conversation that took place between the two suspects. 
