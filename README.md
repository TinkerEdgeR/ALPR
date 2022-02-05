# ASUS IoT ALPR Dev Kit
![](https://iot.asus.com/_nuxt/img/2527929.png)  

## Introduction
ASUS IoT ALPR Edge AI Dev Kit is a comprehensive automatic license-plate recognition (ALPR) solution that includes both the necessary hardware and software to enable systems integrators (SIs) to create edge applications that mesh seamlessly with existing ALPR infrastructure. [See Product Flyer](https://github.com/TinkerEdgeR/ALPR/blob/107683b959fd6aa8a2c791ec8256e62e5f4db7ea/ALPR%20FLYER_Eng_220114_compressed.pdf)

## Workflow
* Get Tinker Edge R AI board (where to buy: https://tinker-board.asus.com/where-to-buy.html)
* Complete Tinker Edge R OS installation and environment runtime
* Contact your business representative to get the latest ALPR demo docker image. 

## Prerequisite



Get the latest Debian image and flash the OS
https://tinker-board.asus.com/download-list.html?product=tinker-edge-r
Contact your business representative to get the latest ALPR demo package.
Copy zip file to Tinker Edge R, unzip to retrieve 4 files

In Debian Terminal, use “chmod + x *.sh” to make batch file executable.
Install ASUS ALPR UK demo version to Tinker Edge R

Install Docker environment (First time) 
In Debian Terminal, run ./<path of batch script>/install_docker.sh
This process might take 10-20 mins depending on your network connection, Tinker Edge R will get rebooted after complete installation.

Loading the ALPR container image (First time)
In Terminal, run docker load < alpr-native_20210316_UK.tar
Wait a few minutes to complete the dock loading process.
Execute the ALPR demo
This demo version supports two video input sources, USB camera and file base video clip. This Is recommended to try the UK demo clip to make sure docker deployment is ready.
Create a new folder and move the UK demo clip to the folder. 
In Terminal, run ./<path of batch scrit>alpr_uk_beta_v1.1.sh, learn about the parameters definition. 

For the quick try, run sh with below parameters
./alpr_uk_beta_v1.1.sh -s file -d <full path of folder where demo video inside> -p yes  -m alpr/img -c alpr/csv -f 5 -a 0.25 -l /log
Docker initializing takes 20 secs then preview shows up.

To test USB camera by changing two parameters
-s camera -d 10 
Close the terminal windows to stop the ALPR demo.
