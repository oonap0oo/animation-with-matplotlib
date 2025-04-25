# This python code explores the animation facilities
# of Matplotlib. It creates a oscilloscope like lissajous pattern
# this code is written for educational purposes
# in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from matplotlib import pyplot as plt 
import numpy as np 
from matplotlib.animation import FuncAnimation  

# parameters
number_of_frames = 480
frame_interval_ms = 17 # comes into play when viewing in matplotlib
frames_per_second = 60 # comes into play when saving as mp4
color_background = "#202020"
color_plot = "#00B000"
color_axis = "#606060"
number_of_points = 2000
freq_x = 3 
freq_y = 5 
file_name = "lissajou4.mp4"

# preparing numpy arrays which stay constant trhough animation
angle = np.linspace(0, 2 * np.pi, number_of_points) 
x = 1.5 * np.cos(freq_x * angle)

# creating a matplotlib window   
fig = plt.figure(figsize = (10,8), facecolor =  color_background)  
axis = plt.axes(xlim =(-2, 2), ylim =(-2, 2))  
axis.set_facecolor(color_background)
axis.xaxis.label.set_color(color_axis)
axis.yaxis.label.set_color(color_axis)
plt.xticks(np.linspace(-2, 2, 11), "")
plt.yticks(np.linspace(-2, 2, 9), "")
for spine in axis.spines:
    axis.spines[spine].set_color(color_axis)
axis.grid(visible = True, which = "both", color = color_axis, linestyle = "--")
# add horizontal and vertical line in the middle of plot
plt.axline((-2,0),(2,0), color = color_axis)
plt.axline((0,-2),(0,2), color = color_axis)

plt.text(-2.3, 2.3, "Pytronix", fontname = "monospace", fontsize = 22, color = color_axis)

# initiate a plot with empty data for now
line, = axis.plot([], [], lw = 2, color = color_plot)  

# the function called for each frame
def animate(frame): 
    y = 1.5 * np.sin(freq_y * angle - 2 * np.pi * frame / number_of_frames) 
    line.set_data(x, y) 
    print(f"Generating frame number {frame}\r", end = "")
    return line, 

# create FuncAnimation object specifying animation
anim = FuncAnimation(fig, animate, frames = number_of_frames, interval = frame_interval_ms, 
                     cache_frame_data = False, blit = False) 

# view animation
plt.show()

# optionally save animation
answer = input(f"Save animation as {file_name}? (y/n)").lower()
if answer == "y":
    print(f"Generating {number_of_frames} frames")
    anim.save(file_name, writer = 'ffmpeg', fps = frames_per_second, dpi = 100, bitrate = 1500) 
    print(f"\nSaved as {file_name}")
