# ASUS IoT ALPR Dev Kit
![](https://iot.asus.com/_nuxt/img/2527929.png)  

## Introduction
ASUS IoT ALPR Edge AI Dev Kit is a comprehensive automatic license-plate recognition (ALPR) solution that includes both the necessary hardware and software to enable systems integrators (SIs) to create edge applications that mesh seamlessly with existing ALPR infrastructure. [See Product Flyer](https://github.com/TinkerEdgeR/ALPR/blob/107683b959fd6aa8a2c791ec8256e62e5f4db7ea/ALPR%20FLYER_Eng_220114_compressed.pdf)

## Workflow
### Preparation
* Get Tinker Edge R AI board (where to buy: https://tinker-board.asus.com/where-to-buy.html)
* Complete Tinker Edge R OS installation and environment runtime
* Contact your business representative to get the latest ALPR docker image. Side load TAR file to Edge R.
* Load ALPR docker image, wait few minutes for loading process.
*      docker load  < alpr-restful_XXXX_TW.tar
### Execute docker image
Run ALPR Service
*      docker run -d --restart unless-stopped --privileged --network host -v /home/linaro/MyImg:/MyImg alpr-restful:XXXX_TW --obj-thresh=0.5

#### Description
* -d -–restart unless-stopped     // Executed in the background, automatically started when the Edge R is restarted
* --privileged, --network host      // Grant container system access permissions 
* -v      // Pre-mount directory,images to be processed
* --obj-thresh      // License plate object detection threshold (0.5~0.9, default 0.5)
#### Docker basic command
>List all running container 
*     docker ps 

>Check docker status , "Server started" shows docker run properly.
*     docker logs <container ID>
![Alt text](image/docker_log_ok.png?raw=true "Title")

  
>Stop docker service.
*     docker stop <container ID>


## License Plate Check Resful-API

### JSON Return
![Alt text](image/API_return_JSON.png?raw=true "Title")
#### Description
>一個List存放 N筆車牌辨認結果
>>List of results
>每一筆結果包含<br>
>>Confidence: 信心分數<br>
>>Plate: 車牌字串<br>
>>Plate_size: 車牌大小<br>
>>Polygon: 車牌的四個頂點座標(x,y)
>>>List of points
  
![image](https://user-images.githubusercontent.com/61956751/152634980-a25ca631-bc80-406c-894e-d9983c279d26.png)

 ![Alt text](image/API_image_ok.png?raw=true "Title")
