from moviepy.editor import VideoFileClip, clips_array
import os
corgi_folder = "/Users/rojass/Documents/Resultados_controlnerf/DATENeRF/static/videos/SuppMat/Fig5. Comparisons/teddy/raiinbow"
file1 = 'in2n-masks.mp4'
file2 = 'ours.mp4'
output_file = 'both.mp4'
target_height = 492  # The target height for all videos

file1_path = os.path.join(corgi_folder, file1)
file2_path = os.path.join(corgi_folder, file2)
output_file_path = os.path.join(corgi_folder, output_file)

# Load the video clips
clip1 = VideoFileClip(file1_path)
clip2 = VideoFileClip(file2_path)

# Resize the videos to the target height while maintaining aspect ratio
clip1_resized = clip1.resize(height=target_height)
clip2_resized = clip2.resize(height=target_height)

# Concatenate the videos side by side
final_clip = clips_array([[clip1_resized, clip2_resized]])

# Write the output video file
final_clip.write_videofile(output_file_path, codec='libx264')