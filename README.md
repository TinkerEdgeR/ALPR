# ASUS IoT ALPR Dev Kit
![](https://iot.asus.com/_nuxt/img/2527929.png)  

## Introduction
ASUS IoT ALPR Edge AI Dev Kit is a comprehensive automatic license-plate recognition (ALPR) solution that includes both the necessary hardware and software to enable systems integrators (SIs) to create edge applications that mesh seamlessly with existing ALPR infrastructure. [See Product Flyer](https://github.com/TinkerEdgeR/ALPR/blob/107683b959fd6aa8a2c791ec8256e62e5f4db7ea/ALPR%20FLYER_Eng_220114_compressed.pdf)

## Workflow
### Preparation
* Get Tinker Edge R AI board (where to buy: https://tinker-board.asus.com/where-to-buy.html)
* Complete Tinker Edge R OS installation and environment runtime
* Contact your business representative to get the latest ALPR docker image. 
* Docker load image file, wait few minutes for loading process.
*      docker load  < alpr-restful_XXXX_TW.tar
### Execute docker image

*      docker run -d --restart unless-stopped --privileged --network host -v /home/linaro/MyImg:/MyImg alpr-restful:XXXX_TW --obj-thresh=0.5
#### Description
* -d -–restart unless-stopped  // Executed in the background, automatically started when the Edge R is restarted
* --privileged, --network host  // Grant container system access permissions 
* -v  // Pre-mount directory,  images to be processed
* --obj-thresh // License plate object detection threshold (default 0.5)
#### log
docker logs <container ID>
啟動一分鐘後，看到” Server started”開始運作
* 停止服務
* docker ps ->確認執行中的container ID
* docker stop <container ID>


## License Plate Check Resful-API



