#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Extract images from a rosbag.
Author: phideltaee 
"""

# Standard libraries
import os
import argparse

# Computer vision libraries 
import cv2

# ROS libraries
import rosbag
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

def main():
    """Extract a folder of images from a rosbag.
    """
    
    # Load variables from docker env. variables in the format "docker run -e BAG=test.bag -e OUT_DIR=/path/ ..."
    bag_file_docker = os.environ['BAG']
    output_dir_docker = os.environ['OUT_DIR']
    img_topic_docker = os.environ['TOPIC']

    # Parsing arguments from terminal.
    parser = argparse.ArgumentParser(description="Extract images from a ROS bag.")
    parser.add_argument("bag_file", help="Input ROS bag.", default=bag_file_docker, nargs='?')
    parser.add_argument("output_dir", help="Output directory.", default=output_dir_docker, nargs='?')
    parser.add_argument("image_topic", help="Image topic.", default=img_topic_docker, nargs='?')

    args = parser.parse_args()

    print(f"Extract images from {args.bag_file} on topic {args.image_topic} into {args.output_dir}")

    bag = rosbag.Bag(args.bag_file, "r")
    bridge = CvBridge()
    count = 0
    for topic, msg, t in bag.read_messages(topics=[args.image_topic]):
        cv_img = bridge.imgmsg_to_cv2(msg, desired_encoding="passthrough")
        cv_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)

        # [-2] accesses the name before bag, and [-1] omits previous paths
        filename = args.bag_file.split(".")[-2].split("/")[-1]
        cv2.imwrite(os.path.join(args.output_dir, filename+"_frame%06i.png" % count), cv_img)
        print(f"Wrote image {count} from {filename}")

        count += 1

    bag.close()

    return

if __name__ == '__main__':
    main()
