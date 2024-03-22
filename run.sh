ffmpeg -i /Users/rojass/Documents/Resultados_controlnerf/DATENeRF/static/videos/SuppMat/Fig1/bear/a\ corgi/in2n-masks.mp4 -i /Users/rojass/Documents/Resultados_controlnerf/DATENeRF/static/videos/SuppMat/Fig1/bear/a\ corgi/ours.mp4 -filter_complex \
"[0:v][1:v]hstack=inputs=2[stacked]; \
 [stacked]drawbox=y=0:x=0:w=200:h=50:color=white@1[withbox1]; \
 [withbox1]drawbox=y=0:x=W-w:w=200:h=50:color=white@1[withbox2]; \
 [withbox2]drawtext=fontfile=cmunbx.ttf:text='Instruct-NeRF-2-NeRF':fontcolor=black:fontsize=24:x=10:y=10[withtext1]; \
 [withtext1]drawtext=fontfile=cmunbx.ttf:text='Ours':fontcolor=black:fontsize=24:x=W-tw-10:y=10" \
output.mp4
