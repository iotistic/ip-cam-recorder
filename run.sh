#!/bin/bash

# check if ffmpeg is installed
if ! [ -x "$(command -v ffmpeg)" ]; then
  echo 'Error: ffmpeg is not installed.' >&2
  echo 'Installing ffmpeg'
  sudo apt install ffmpeg -y
fi

# Run the script.
python3 ip_cam_recorder.py --directory /home/mnvr/recordings
