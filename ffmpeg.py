import os

input_dir = "C:\\Users\\zabir\\Downloads\\Ольга Василенко"
output_dir = "C:\\Users\\zabir\\Downloads\\Ольга Василенко mp3"

if not os.path.exists(output_dir):
    os.mkdir(output_dir)

input_dir_list = os.listdir(work_dir)

for sub_dir in work_dir_list:
    current_input_dir = input_dir + "\\" + sub_dir
    if os.path.isdir(current_input_dir):
        current_output_dir = output_dir + "\\" + sub_dir
        if not os.path.exists(current_output_dir):
            os.mkdir(current_output_dir)
        current_input_dir_list = os.listdir(current_input_dir)
        for input_video in current_input_dir_list:
            input_video_full_path = current_input_dir + "\\" + input_video
            if input_video_full_path[-4:].lower() == ".mp4":                # mp4 video
                output_audio_full_path = current_output_dir + "\\" + input_video[:-4] + ".mp3"            # mp3 audio
                ffmpeg_params = "-i \"" + input_video_full_path + "\" -y \"" + output_audio_full_path + "\""
                !ffmpeg $ffmpeg_params
