# HAM Alert Discord Integration
HamAlerts to Discord Webook


Using an Ubuntu Linux Machine follow the below steps:

----------------------------------------------------------------------------------------------------
To Set up HamAlert and Discord Connections:
1. Create trigger on https://hamalert.org and have it action "Telnet"
2. Create a linux machine and install python3
   sudo apt install python3-pip
   pip install requests
3. Create your python file and copy the information from hamalert.py
4. Edit HAMALERT USERNAME, PASSWORD, and DISCORD WEBHOOK to be your information
5. Follow the following guide to run python as a service in your operating system. This works for Ubuntu as well!
https://gist.github.com/emxsys/a507f3cad928e66f6410e7ac28e2990f
6. Enjoy!

----------------------------------------------------------------------------------------------------
To create a discord webhook follow the below instructions:
1. Server Settings
2. Integrations
3. Webooks
4. New Webhook
5. Change Name to anything you desire and set channel to where you want spots to output
6. Copy the URL and paste into your hamalert.py

----------------------------------------------------------------------------------------------------

Created by W2ORT
Matthew O.
https://w2ort.com

Updated and heavily corrected by:
Dylon N6MX
Devin KN6PHZ

Special Thanks to:
Mark KD7DTS and the W6TRW Club!
