import os
import threading
import argparse
import subprocess # For executing the FFMPEG command
from datetime import datetime # For getting the current date and time

# This function  is used to record the video from the IP cameras using FFMPEG and save them to the local disk.

# Input:
#   - ip_cam_url: the url of the IP camera
#   - ip_cam_id: the id of the IP camera
#   - directory: the directory where the video will be saved

# Output:
#   - None

def record_video(ip_cam_url, ip_cam_id, directory):
    # Create the directory if it does not exist
    if not os.path.exists(directory):
        os.makedirs(directory)

    if not os.path.exists(directory + "/cam_" + ip_cam_id):
        os.makedirs(directory + "/cam_" + ip_cam_id)

    # Create the file name
    file_name = directory + "/cam_" + ip_cam_id + "/" + "%s.mp4"


    # Create the FFMPEG command
    command = "ffmpeg -i " + ip_cam_url + " -c copy -map 0 -f segment -segment_time 10 -reset_timestamps 1 -strftime 1 " + file_name
    
    # Execute the FFMPEG command in the background
    subprocess.call(command, shell=True)


if __name__ == "__main__":
    # Record the video from the IP camera as threads
    parser = argparse.ArgumentParser()
    parser.add_argument("--directory", help="The directory where the video will be saved", default="/home/mnvr/recordings")
    args = parser.parse_args()

    # record_video("rtsp://admin:123456@107.157.16.101:554/stream1", "1", "/home/iotistic-mnvr/videos/")
    cam1_thread = threading.Thread(target=record_video, args=("rtsp://admin:123456@107.157.16.101:554/stream1", "1", args.directory),)
    cam1_thread.start()

    cam2_thread = threading.Thread(target=record_video, args=("rtsp://admin:123456@107.157.16.102:554/stream1", "2", args.directory))
    cam2_thread.start()
