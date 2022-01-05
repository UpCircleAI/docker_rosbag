# Working with Docker
Short description: dockerized image extractor for rosbags. 

This docker image is a simple implementation of a dockerized ros package to extract images from rosbags. It only needs docker, and nothing else. This can be run on Linux, Windows or Mac. It takes a rosbag containing image data (e.g. realsense /camera/colo/image_raw data) and outputs every frame as a jpeg file into a directory. 

# Running Instructions
There's three main directories that are relevant.
 - **data_output directory:** this is where you output images will be
 - **src:** this directory includes the files to run the bag extraction system.
 - **mount directory:** this is the directory where your rosbag is (needs to be separate from the output dir)

## Running Options [1]: Building it yourself.
To built the container just have the following.
1. Clone this repo to your local machine:

    ```
    git clone ...
    ```

2. Navigate to the directory for this file.

    ```
    cd docker_rosbag
    ```

3. build the docker image locally, and add a name (and tag) of your choice (e.g. rosbag_extractor)

    ```
    docker build -t rosbag_extractor .
    ```

4. proceed to run the container (see below)

## Running Options [2]: Get from Dockerhub.  

  To pull the image from dockerhub run the following command:
      
    docker pull autonomousrivercleanup/rosbag_extractor:v1
      
  Then, to make sure it works still with the run instructions below, add a new tag to the image:

    docker tag autonomousrivercleanup/rosbag_extractor:v1 rosbag_extractor

## Running the Container.

Use the following command to start the docker container. If you don't have it, this will pull the latest container from Dockerhub.

Running directly from the local terminal can be achieved by using environemtal variables. 

  - Step 1: mount the rosbag to the `rosbags/raw` folder. This is done by changing the "/Volumes.../:" part with the path to the directory containing your rosbag. 

  - Step 2: mount the output dir to the `rosbags/extracted` folder. This relative path should work for you (if you are running from the root folder of this repo). 

  - Step 3: pass the env. variables for `BAG`, `OUT_DIR`, `TOPIC`

  ```
  docker run \
  -v /Volumes/Untitled/2021_ARC/rosbags/:/rosbags/raw/  \
  -v /Users/fidel/Projects/0_programming/21_docker/docker_rosbag/data_output/:/rosbags/extracted/ --net=host -it  \
  -e BAG=./raw/2021-06-30-16-19-38.bag \
  -e OUT_DIR=./extracted/ \
  -e TOPIC=/camera/color/image_raw \
  rosbag_extractor
  ```

Additionally, if you want to have access to the container at runtime, add the `/bin/bash` command at the end, after the image name. 

  ```
  docker run -v /path_to_rosbag_dir/:/rosbags/raw/ -it --net=host -v /path_to_output_dir/:/rosbags/extracted/ ...[additional tags]... rosbag_extractor /bin/bash
  ```

NOTE: you must...
- Change "path_to_rosbag" with the adequate path to your won rosbag.
- Change "/path_to_output_file/" with the path to your output dir


docker run \
-v /Volumes/Untitled/2021_ARC/rosbags/:/rosbags/raw/  \
-v /Users/fidel/Projects/0_programming/21_docker/docker_rosbag/data_output/:/rosbags/extracted/ --net=host -it  \
-e BAG=./raw/2021-07-21-18-28-59.bag \
-e OUT_DIR=./extracted/ \
-e TOPIC=/camera/color/image_raw \
rosbag_extractor


Jun 30  2021 309M 2021-06-30-16-19-38.bag x
Jun 30  2021 3.9G 2021-06-30-16-21-15.bag x
Jun 30  2021 3.9G 2021-06-30-16-24-35.bag x
Jul 21 18:28  13G 2021-07-21-18-23-45.bag x
Jul 21 18:35  17G 2021-07-21-18-28-59.bag 
Aug  9 19:10 8.6G 2021-08-09-19-07-19.bag 
Aug 11 17:28  11G 2021-08-11-17-24-17.bag 
Aug 12 16:41 5.2G 2021-08-12-16-39-33.bag 
Aug 12 16:58  38G 2021-08-12-16-43-10.bag 
Aug 12 17:01 5.5G 2021-08-12-16-59-34.bag 
Aug 12 17:09 4.3G 2021-08-12-17-07-33.bag 
Aug 12 17:22  12G 2021-08-12-17-17-58.bag 
Aug 12 17:28 6.5G 2021-08-12-17-26-12.bag 
Aug 12 17:33 7.8G 2021-08-12-17-30-43.bag 
Aug 12 17:51  11G 2021-08-12-17-46-44.bag 
Aug 12 18:01 6.2G 2021-08-12-17-58-53.bag 
Aug 12 18:43  60G 2021-08-12-18-20-21.bag 
Aug 13 15:41 7.7G 2021-08-13-15-38-32.bag 
Aug 13 16:10 4.9G 2021-08-13-16-08-58.bag 
Aug 13 16:13 4.8G 2021-08-13-16-11-34.bag 
Aug 13 18:36 2.0G 2021-08-13-18-35-14.bag 
Aug 14 12:10 3.1G 2021-08-14-12-09-41.bag 
Aug 14 12:21  12G 2021-08-14-12-16-53.bag 
Aug 14 12:35  11G 2021-08-14-12-30-49.bag 
Aug 14 13:57 6.8G 2021-08-14-13-55-13.bag 
Aug 17 15:23 6.0G 2021-08-17-15-20-42.bag 
Aug 17 15:58 4.0K 2021-08-17-15-56-25.bag 
Aug 17 16:01 1.8G 2021-08-17-16-00-09.bag 
Aug 17 16:26 3.2G 2021-08-17-16-25-23.bag 
Aug 17 16:294.2G  2021-08-17-16-27-54.bag