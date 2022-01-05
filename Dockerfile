FROM ros:noetic-ros-base

RUN mkdir -p rosbags/raw & mkdir rosbags/extracted

COPY ./scripts/bag_to_images.py /rosbags/

# install ros packages
RUN apt-get update && apt-get install -y \
      ros-${ROS_DISTRO}-image-view #&& \
#      rm -rf /var/lib/apt/lists/*

# installing additional useful tools
RUN apt-get -y install tree
RUN apt-get -y install iputils-ping
RUN apt-get -y install nano

# Installing the opencv required files
RUN apt-get -y install pip # this install python3-pip
RUN pip3 install opencv-python


# Installnig the mjpeg tools and image_view packages  for processing ros images
RUN apt-get -y install mjpegtools

# change the working directory to the rosbags folder
WORKDIR /rosbags

# adding an entry point to run python script directly. 
# ENTRYPOINT ["python", "/rosbags/scripts/bag_to_images.py"]

# Additional functionality, run the rosbag processing
RUN chmod +x ./bag_to_images.py

CMD python3 ./bag_to_images.py