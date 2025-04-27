# This python code explores the animation facilities
# of Matplotlib. It creates animated plots of several
# ballistic trajectories 
# this code is written for educational purposes
# in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from matplotlib import pyplot as plt 
import numpy as np 
from matplotlib.animation import FuncAnimation  

# parameters
v_initial_m_s = 20
alpha_degrees = tuple((a * 15 for a in range(6)))
time_interval_s = 4.5
number_of_frames = 300
number_of_points = number_of_frames
frame_interval_ms = 17 # comes into play when viewing in matplotlib
frames_per_second = 60 # comes into play when saving as mp4
x_min, x_max, y_min, y_max = -1, 45, -5, 20
color_background = "#303030"
color_plot = ("red", "blue", "green", "yellow", "magenta", "cyan") * 2
color_axis = "#D0D0D0"
text_size = 14
file_name = "ballistic.mp4"

# contants
g_N_kg = 9.81

# functions that define the x and y values for trajectories
def trajectory_x(time_s,vo_m_s,angle_radians):
    x = vo_m_s * np.cos(angle_radians) * time_s
    return x
    
def trajectory_y(time_s,vo_m_s,angle_radians):
    y = vo_m_s * np.sin(angle_radians) * time_s - 0.5 * g_N_kg * time_s ** 2
    return y

# numpy array with time values
t = np.linspace(0, time_interval_s, number_of_points)

# lists of numpy arrays with x and y values of trajectories
x = [trajectory_x(t, v_initial_m_s, np.radians(alpha)) for alpha in alpha_degrees]
y = [trajectory_y(t, v_initial_m_s, np.radians(alpha)) for alpha in alpha_degrees]

# define plot window, colors etc.
fig = plt.figure(num = "Ballistic trajectories", figsize = (10,8), facecolor =  color_background) 
axis = plt.axes(xlim = (x_min, x_max), ylim = (y_min, y_max)) 
plt.box(False)
axis.set_title("Ballistic trajectories", fontsize = text_size + 5, color = color_axis, y = 1.02)
axis.set_facecolor(color_background)
axis.set_xlabel("X", fontsize = text_size, color = color_axis)
axis.set_ylabel("Y", fontsize = text_size, color = color_axis)
axis.grid(visible = True, which = "both", color = color_axis, linestyle = "dotted")
plt.axline((x_min, 0), (x_max, 0), color = color_axis, linewidth = 2)
plt.axline((0, y_min), (0, y_max), color = color_axis, linewidth = 2)
axis.tick_params(axis = 'both', which = 'major', labelsize = text_size, color = color_axis, labelcolor = color_axis)
axis.tick_params(axis = 'both', which = 'minor', labelsize = text_size-2, color = color_axis, labelcolor = color_axis)
axis.spines['bottom'].set_color(color_axis)
axis.spines['top'].set_color(color_axis) 
axis.spines['right'].set_color(color_axis)
axis.spines['left'].set_color(color_axis)

# initiate a list of plots with empty data for now
lines = [axis.plot([], [], linewidth = 3, color = color_plot[index]) for index in range(len(alpha_degrees))]

# the function called for each frame
def animate(frame): 
    lines_ani = [lines[index][0].set_data(x[index][:frame], y[index][:frame]) for index in range(len(lines))]
    print(f"Generating frame number {frame}\r", end = "")
    return lines_ani

# create FuncAnimation object specifying animation
anim = FuncAnimation(fig, animate, frames = number_of_frames, interval = frame_interval_ms, 
                     cache_frame_data = False, blit = False) 

# view animation
plt.show()


# optionally save animation
answer = input(f"Save animation as {file_name}? (y/n)").lower()
if answer == "y":
    print(f"Generating {number_of_frames} frames")
    anim.save(file_name, writer = 'ffmpeg', fps = frames_per_second, dpi = 100, bitrate = 1000) 
    print(f"\nSaved as {file_name}")

