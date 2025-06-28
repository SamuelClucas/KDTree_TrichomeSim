import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import numpy as np
from skimage import io
import os
import csv
import subprocess

# STARTUP///////////////////////////////////////////////////////////////////////////////////////////
stack = io.imread('/Users/samclucas/Documents/stacks_for_mt_spline_builder/base_1C_prbabilities.tif')
stack = (stack).astype(np.uint8)  # use if error 
csv_file_path = '/Users/samclucas/Desktop/base_points.csv'
threeD_path = '/Users/samclucas/Desktop/MT Plot/MT_Plot_3D.py'

# globals - bad practice
depth = 0
slice = stack[depth]
points = []
fig, ax = plt.subplots()
uncommitted = [] # uncommitted circles
committed = [] # committed circles

def points_to_committed(points):
    global committed
    i = 0
    while i < len(points) - 1:
        if points[i] == ' ':
            committed.append(' ')
            i += 1
        else:
            circle = plt.Circle((points[i], points[i + 1]), 3, color = 'orange', fill = False)
            depth = points[i + 2]
            committed.append(circle)
            committed.append(depth)
            i += 3
    if len(points) != 0:
        committed.append(' ')
            
# updates which circles to be shown on the figure
def update_circles(): 
    global depth, uncommitted, committed, slice
    ax.cla()  # Clear 
    ax.imshow(slice, cmap='gray')  # Display the new image
    ax.axis('off')
    fig.canvas.draw_idle()
    i = 0
    while i < len(uncommitted) - 1:
        if uncommitted[i + 1] == depth:
            ax.add_artist(uncommitted[i])
        i += 2
    i = 0
    while i < len(committed) - 1:
        if committed[i] == ' ':
            i += 1
        else:
            if committed[i + 1] == depth:
                committed[i].set_color('orange')
                ax.add_artist(committed[i])
            i += 2

if os.path.exists(csv_file_path):
    with open(csv_file_path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if row['X'] == '\n':
                points.append(' ')
            else:
                points.append((float(row['X'])))
                points.append((float(row['Y'])))
                points.append((float(row['Z'])))
        csv_file.close()
        print(points)
        points_to_committed(points)
        update_circles()
else:
    with open(csv_file_path, mode='w', newline='') as csv_file:
                fieldnames = ['X', 'Y', 'Z']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()

plt.subplots_adjust(bottom=0.4)
image_plot = ax.imshow(slice, cmap='gray') # Display image slice in the stack
ax.axis('off')

# Creating the GUI buttons
ax_slider = plt.axes([0.25, 0.25, 0.65, 0.03], facecolor='lightgoldenrodyellow') # Add a slider for navigation
slider = Slider(ax_slider, 'Image', 0, len(stack), valinit=depth, valstep=1)

ax_clear_button = plt.axes([0.8, 0.025, 0.1, 0.04])
clear_button = Button(ax_clear_button, 'Clear Layer', color='lightgoldenrodyellow', hovercolor='0.975') # Add a button to clear current layer circles
clear_button.label.set_fontsize(8) # Set smaller font size for the button text

ax_commit_button = plt.axes([0.5, 0.025, 0.2, 0.04]) # Add a button to commit circles
commit_button = Button(ax_commit_button, 'Commit Microtubule', color = 'lightgoldenrodyellow', hovercolor = '0.975')
commit_button.label.set_fontsize(8)

ax_export_button = plt.axes([0.2, 0.025, 0.15, 0.04]) # add button to export data
export_button = Button(ax_export_button, 'Export Data', color = 'gold', hovercolor = '0.975')
export_button.label.set_fontsize(8)

ax_visualise_csv_button = plt.axes([0.2, 0.1, 0.15, 0.1]) # add button to export data
visualise_csv_button = Button(ax_visualise_csv_button, 'Visualise CSV', color = 'gold', hovercolor = '0.975')
visualise_csv_button.label.set_fontsize(8)
# STARTUP///////////////////////////////////////////////////////////////////////////

# FUNCTIONALITY/////////////////////////////////////////////////////////////////////

# Function to move slider with arrow keys
def on_key(event):
    global depth, stack
    if event.key == 'left' and int(slider.val) > 0:
        depth -= 1
        slider.set_val(depth)
    elif event.key == 'right' and int(slider.val) <= len(stack) - 1:
        depth += 1
        slider.set_val(depth)
            
# Function to update the displayed image based on slider value
def update(val):
    global slice, depth, stack
    depth = val
    slice = stack[depth]
    image_plot.set_data(slice)
    update_circles()
    fig.canvas.draw_idle()
    
# Function to handle mouse click event
def on_image_click(event):
    if event.inaxes == ax:
        x, y = int(event.xdata), int(event.ydata)
        add_circle(x, y)
        fig.canvas.draw_idle()
        
# Function to add a circle at the specified coordinates passed by on_image_click()
def add_circle(x, y):
    global depth
    circle = plt.Circle((x, y), 3, color='red', fill=False)
    uncommitted.append(circle)
    uncommitted.append(depth) # add circle and depth to uncommitted list
    ax.add_artist(circle)
    
# Function to clear circles on the current layer
def clear_layer(event):
    global depth, uncommitted
    i = 0 
    while i <= len(uncommitted) - 1:
        if uncommitted[i + 1] == depth:
            del uncommitted[i + 1]
            del uncommitted[i]
        else:
            i += 2
    fig.canvas.draw_idle()
    update_circles()

# Function to handle commit button click
def commit_circles(event):
    global committed, uncommitted
    i = 0
    while i <= len(uncommitted) - 1: # move uncommitted to committed, delete all members of uncommitted
        committed.append(uncommitted[i])
        del uncommitted[i]
        print(len(uncommitted))
    committed.append(' ') 
    update_circles()
    
def export_data(event):
    global committed
    i = 0
    j = 0
    data_export = []
    while i < len(committed) - 1:
        if committed[i] == ' ':
            data_export.append(' ') 
            i += 1
            j += 1
        else:
            x, y = committed[i].center
            z = committed[i + 1]
            data_export.append(x)
            data_export.append(y)
            data_export.append(z)
            print(data_export)
            i += 2
            j += 3
    data_export.append(' ')
    i = 0
    with open(csv_file_path, mode='w', newline='') as csv_file:
                fieldnames = ['X', 'Y', 'Z']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                while i < len(data_export) - 1:
                    if data_export[i] == ' ':
                        writer.writerow({'X': '\n', 'Y': '\n', 'Z': '\n'})
                        i += 1
                    else:
                        writer.writerow({'X': data_export[i], 'Y': data_export[i + 1], 'Z': data_export[i + 2]})
                        i += 3
                data_export.append(' ')

def play(event):
    try:
        subprocess.run(['python3', threeD_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
    except FileNotFoundError:
        print(f"Error: File not found at {threeD_path}")
    
# FUNCTIONALITY////////////////////////////////////////////////////////////////////////

# Attaching GUI buttons to functions and displaying plot
slider.on_changed(update) 
fig.canvas.mpl_connect('button_press_event', on_image_click) 

clear_button.on_clicked(clear_layer) 

commit_button.on_clicked(commit_circles) 

export_button.on_clicked(export_data)

visualise_csv_button.on_clicked(play)

fig.canvas.mpl_connect('key_press_event', on_key) 

plt.show()