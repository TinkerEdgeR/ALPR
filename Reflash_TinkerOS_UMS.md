# Reflash Tinker OS via UMS mode
The UMS mode (USB mass storage) enable user to mount Tinker Edge R as common usb storage, it bring convenience for reflashing new OS image cross PC or Mac with no device driver required.</br> 
</br>
Although OS installation on Tinker Edge R supports either SD card or eMMC, `eMMC is recommanded due to uncontrollable SD card qualities.`  There are two main steps making eMMC support UMS base OS.:
>(1) Make a bootable SD card let Edge R can be initiated by UMS mode. </br>
>(2)Reflash same image again to eMMC. 

`NOTE: This procedure needs to execute once on each Tinker Edge R, as long as the image version still keeps in V1.0.13 or higher. Afterwards, you just flash an image following steps 3-5 to 3-9 with a USB Type-C connection.`


##	Preparation 
* A micro-SD card
* A micro-SD card reader
* A USB Type-C cable (Type-C to Type A)
* Tinker Edge R
* Power Adaptor, 12~19V DC

## Steps
### Prepare bootable SD card
(1) Get the Tinker OS (Debian for example)
* >https://tinker-board.asus.com/download-list.html?product=tinker-edge-r

(2) Download tool either one of below list: (Using Etcher for this demo)
* >Etcher, https://www.balena.io/etcher/ 
* >Win32DiskImager, https://sourceforge.net/projects/win32diskimager/ 

(3).	Flash recovery image to micro-SD card
* >Insert micro-SD card into the card reader.
* >Insert the card reader to the Laptop/PC.
* >Run Etcher utility.
 

(4)	Click “Flash from file”, then browse file name “Tinker_Edge_R-Debian-Stretch-vX.X.XX.X-YYYYMMDD.img”.
 

(5)	Click “Select target” to choose the micro-SD card.</br>
![Alt text](image/SDXC_UMS_USB_Etcher.png?raw=true "Title")

(6)	Then clicking “Flashing!” beginning to flash image to SD card.
 

(7)	It will show the progress as below shown, wait process finished.

### Flash image to the eMMC of Tinker Edge R
(1) Remove the micro-SD and insert it into SD slot of Tinker Edge R.</br>
(2) Connect USB Type-C cable to Tinker Edge R and Type-A to PC/Mac</br>
(3) Connect power adaptor to Tinker Edge R.</br>
The Laptop/PC should detect several USB disks which come from Tinker Edge R. </br>
`(DO NOT format any of the mounted disks when popping up the format warning.)`</br>
(4 )Run Etcher utility. (The following steps are the same as above.)</br>
(5) Click “Flash from file” and browse the image file, such as “Tinker_Edge_R-Debian-Stretch-vX.X.XX.X-YYYYMMDD.img”.</br>
(6) Click “Select target” and select “ASUS Tinker UMS USB Device”.</br>
![Alt text](image/ASUS_Tinker_UMS_USB_Etcher.png?raw=true "Title") </br>
(7) Click “Flash!” beginning to flash the image and waiting for it finishes.</br>
(8) You could remove the micro-SD card, USB Type-C cable and power adaptor from Tinker Edge R once flashed completely.</br>

