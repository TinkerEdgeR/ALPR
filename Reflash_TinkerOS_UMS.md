# Reflash Tinker OS via UMS mode
The UMS mode (USB mass storage) enable user to mount Tinker Edge R as common usb storage, it bring convenience for reflashing new OS image cross PC or Mac without installing device driver.</br> 
</br>
Although OS installation on Tinker Edge R supports either SD card or eMMC, `eMMC is recommanded` due to uncontrollable SD card qualities. This article shows reflash Tinker OS in eMMC.


##	Preparation 
* A micro-SD card
* A micro-SD card reader
* A USB Type-C cable (Type-C to Type A)
* Tinker Edge R
* Power Adaptor, 12~19V DC

## Steps
(1) Get the Tinker OS (Debian for example)
* >https://tinker-board.asus.com/download-list.html?product=tinker-edge-r

(2) Download tool either one of below list: (Using Etcher for this demo)
* >Etcher, https://www.balena.io/etcher/ 
* >Win32DiskImager, https://sourceforge.net/projects/win32diskimager/ 

(3).	Flash recovery image to micro-SD card
3-1.	Insert micro-SD card into the card reader.
3-2.	Insert the card reader to the Laptop/PC.
3-3.	Run Etcher utility.
 

(4).	Click “Flash from file”, then browse file name “Tinker_Edge_R-Debian-Stretch-vX.X.XX.X-YYYYMMDD-Recovery.img”.
 

(5).	Click “Select target” to choose the micro-SD card.
 

(6).	Then clicking “Flashing!” beginning to flash recovery image to SD card.
 

(7).	It will show the progress as below shown:
   

(8).	Then finished.
 
(9).	Flash image to the eMMC of Tinker Edge R
* >Remove the micro-SD and insert it into SD slot of Tinker Edge R.
* >Connect USB Type-C cable between Tinker Edge R and Laptop/PC.
* >Connect power adaptor to Tinker Edge R.
* >The Laptop/PC should detect several USB disks which come from Tinker Edge R after Tinker Edge R power on. Please DO NOT format any of the detected disks when popping up the format warning.
* >Run Etcher utility. (The following steps are the same as above.)
* >Click “Flash from file” and browse the image file, such as “Tinker_Edge_R-Debian-Stretch-vX.X.XX.X-YYYYMMDD.img”.
   

* >Click “Select target” and select “ASUS Tinker UMS USB Device”.
   

* >Click “Flash!” beginning to flash the image and waiting for it finishes.
   

* >You could remove the micro-SD card, USB Type-C cable and power adaptor from Tinker Edge R once flashed completely.

`NOTE: This procedure needs to execute once on each Tinker Edge R, as long as the image version still keeps in V1.0.13 or higher. Afterwards, you just flash an image following steps 3-5 to 3-9 with a USB Type-C connection.`
