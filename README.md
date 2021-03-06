# ASUS IoT ALPR Dev Kit
![](https://iot.asus.com/_nuxt/img/2527929.png)  

## Introduction
ASUS IoT ALPR Edge AI Dev Kit is a comprehensive automatic license-plate recognition (ALPR) solution that includes both the necessary hardware and software to enable systems integrators (SIs) to create edge applications that mesh seamlessly with existing ALPR infrastructure. [See Product Flyer](https://github.com/TinkerEdgeR/ALPR/blob/788a7fc3c2e313d94afb5ac5656757120bdc64eb/material/ALPR%20FLYER_Eng_220114_compressed.pdf)

## Workflow
### Preparation
* Get Tinker Edge R AI board (where to buy: https://tinker-board.asus.com/where-to-buy.html)
* Complete [Tinker Edge R OS installation](https://github.com/TinkerEdgeR/ALPR/blob/1b515fcac068c28fbc833088bf509bb74b9dc9b4/Flash_TinkerOS_UMS.md) and [environment runtime](https://github.com/TinkerEdgeR/ALPR/blob/10a99b33971e23f2939654e8bf9345f2c838b2ec/alpr_runtime.md)
* Contact your business representative to get the latest ALPR docker image. Side load TAR file to Edge R.
* Load ALPR docker image, wait few minutes for loading process.
*      docker load  < alpr-restful_XXXX_TW.tar
### Execute docker image
Run ALPR Service
*      docker run -d --restart unless-stopped --privileged --network host -v /home/linaro/MyImg:/MyImg alpr-restful:XXXX_TW --obj-thresh=0.5

#### Description
>* <b>-d -–restart unless-stopped</b>     // Executed in the background, automatically started when the Edge R is restarted
>* <b>--privileged, --network host</b>      // Grant container system access permissions 
>* <b>-v</b>      // Pre-mount directory,images to be processed
>* <b>--obj-thresh</b>      // License plate object detection threshold (0.5~0.9, default 0.5)
#### Basic Docker command
>List all running container 
*     docker ps 

>Check docker status , "Server started" shows docker is running properly.
*     docker logs <container ID>
![Alt text](image/docker_log_ok.png?raw=true "Title")
`(Note: Tinker Edge R requires ineternet connection to get license key at first time)`

  
>Stop docker service.
*     docker stop <container ID>


## License Plate Check Restful-API

### Get image recognition from file path
*      curl -X GET http://[ip]:8080/file/image/recognize?path=[image file]
* Example:
>*      curl http://localhost:8080/file/image/recognize?path=/MyImg/20210621000148367_1_ASM8888.jpg

### Get image recognition from Base64 format
>*      curl "base64 string"  -X POST http://localhost:8080/data/image/recognize
[Example](https://github.com/TinkerEdgeR/ALPR/blob/c768ace2d9cabd8c0d70cc0f04fac6280a5b2a38/sample%20code/base64_call.sh)
  
### Direct recognition from camera stream
*      curl -X GET http://[ip]:8080/camera/image/recognize?camera_id=[Device ID]
* Example - web camera is located at /dev/video10
>*      curl -X GET http://localhost:8080/camera/image/recognize?camera_id=10

### JSON Return
![Alt text](image/API_return_JSON.png?raw=true "Title")
#### Description
>A List stores N license plate recognition results
  >><B>Confidence</B>:confidence score<br>
>><B>Plate</B>:license plate string<br>
>><B>Plate_size</B>:license plate size<br>
>><B>Polygon</B>:The coordinates of the four endpoints of the license plate(x,y)
>>>List of points
  
 ![Alt text](image/API_image_ok.png?raw=true "Title")
* Correct: return JSON string, status HTTP_OK(200)
* Error: Error message returned, status HTTP_BAD_REQUEST(400)…
{ "error" : "error message..." }


## Sample Codes

### Batch testing of numerous car-plate photos
* Prepare the validation photos.
* Side load photos to Edge R storage
* Run docker service
* Run [sample code](https://github.com/TinkerEdgeR/ALPR/blob/6dba7e19075267e1ba8c720d80370c7afff92559/sample%20code/ALPR_API_base64_1229.py) 
  *      python3 ALPR_API_base64_1229.py [directory absolute path]
* Example 
>*        python3 ALPR_API_base64_1229.py  /home/linaro/Desktop/Customer_photos/
* Output CSV include:
>* File name
>* Recognition result
>* Confidence scope
>* Time taken of each photo

### Rendering the recognition result

This sample demonstrates OSD info on screenshot, help you to identify the car-plate boundary, recognition result and confidence score. </br>
</br>
ALPR engine supports multiple car-plate recognition from single image, feel free to modify the code to fit your needs.

* Get [sample code](https://github.com/TinkerEdgeR/ALPR/blob/ea4ffa8f276cdd583a98ae45a90ad3a4c4e477c9/sample%20code/osd_rendering.py)
*      python3 osd_rendering.py -o [host file path] -c [container file path] -i [camera node id]
* Example:
>*     python3 sample.py -o /home/linaro/images/usbcam -c /images/usbcam -i 10
  
![Alt text](image/rendering-OSD.png?raw=true "Title")
