To support UMS mode for Tinker Edge R, it must flash image thru micro-SD card with recovery image. It would affect the version after Tinker Edge R Debian Stretch V1.0.13 when you would upgrade the image from an older one.


1.	Preparation 
A micro-SD card
A micro-SD card reader
A USB Type-C cable
Tinker Edge R
Power Adaptor, 12~19 VDC

Get the Tinker OS (Debian)
https://tinker-board.asus.com/download-list.html?product=tinker-edge-r

Download tool either one of below list: (This document demonstrates by using Etcher.)
Etcher, https://www.balena.io/etcher/ 
Win32DiskImager, https://sourceforge.net/projects/win32diskimager/ 

2.	Flash recovery image to micro-SD card
2-1.	Insert micro-SD card into the card reader.
2-2.	Insert the card reader to the Laptop/PC.
2-3.	Run Etcher utility.
 

2-4.	Click “Flash from file”, then browse file name “Tinker_Edge_R-Debian-Stretch-vX.X.XX.X-YYYYMMDD-Recovery.img”.
 

2-5.	Click “Select target” to choose the micro-SD card.
 

2-6.	Then clicking “Flashing!” beginning to flash recovery image to SD card.
 

2-7.	It will show the progress as below shown:
   

2-8.	Then finished.
 
3.	Flash image to the eMMC of Tinker Edge R
3-1.	Remove the micro-SD and insert it into SD slot of Tinker Edge R.
3-2.	Connect USB Type-C cable between Tinker Edge R and Laptop/PC.
3-3.	Connect power adaptor to Tinker Edge R.
3-4.	The Laptop/PC should detect several USB disks which come from Tinker Edge R after Tinker Edge R power on. Please DO NOT format any of the detected disks when popping up the format warning.
3-5.	Run Etcher utility. (The following steps are the same as above.)
3-6.	Click “Flash from file” and browse the image file, such as “Tinker_Edge_R-Debian-Stretch-vX.X.XX.X-YYYYMMDD.img”.
   

3-7.	Click “Select target” and select “ASUS Tinker UMS USB Device”.
   

3-8.	Click “Flash!” beginning to flash the image and waiting for it finishes.
   

3-9.	You could remove the micro-SD card, USB Type-C cable and power adaptor from Tinker Edge R once flashed completely.

NOTE: This procedure needs to execute once on each Tinker Edge R, as long as the image version still keeps in V1.0.13 or higher. Afterwards, you just flash an image following steps 3-5 to 3-9 with a USB Type-C connection.