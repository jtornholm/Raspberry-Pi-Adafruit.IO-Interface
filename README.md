# Raspberry-Pi-Adafruit.IO-Interface
Python code to interface a Raspberry Pi with a SHT-30 temp/humidity sensor and relay board via Adafruit.IO
 
This repository will provide the set up instructions to connect a SHT-30 sensor https://www.adafruit.com/product/4099 to a Raspberry pi Model B+ and display the readings via the Adafruit.io cloud service. 
 
Additionally this set up adds function to control a relay board, which will allow a user to switch on and off a light or some other device.
 
<strong>Go ahead and ssh into your Raspberry Pi via terminal or a ssh client:
ssh pi@raspberrypi.local</strong>
 
Run the standard updates:
<code>sudo apt-get update</code>
<code>sudo apt-get upgrade</code>
 
<h3> Make sure you're using Python 3! </h3>
 
If you have PIP installed (typically with <code>apt-get install python-pip</code> on a Debian/Ubuntu-based system), run:
 
<code>sudo pip3 install adafruit-io</code>
 
<code>sudo pip3 install --upgrade setuptools</code>
 
<h4>Install the SHT31D Library</h4>
<code>sudo pip3 install adafruit-circuitpython-sht31d</code>
 
<h4>Install Adafruit Blinka Library</h4>
<code>pip3 install RPI.GPIO</code>
 
<code>pip3 install adafruit-blinka</code>
