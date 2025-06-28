import vtk
import numpy as np
import csv
from skimage import io
from vtk.util.numpy_support import vtk_to_numpy
from vtkmodules.vtkCommonCore import vtkCommand
import os
import sys


image_stack = io.imread('/Users/samclucas/Documents/stacks_for_mt_spline_builder/base_1C_prbabilities.tif')
image_stack = (image_stack).astype(np.uint8)
csv_file_path = '/Users/samclucas/Desktop/base_points.csv'

points = []

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
else:
    print(".CSV doesn't exist - create with MT Plot 2D first")           

# Create a VTK volume
vtk_volume = vtk.vtkImageData()
vtk_volume.SetDimensions(image_stack.shape[2], image_stack.shape[1], image_stack.shape[0])
vtk_volume.SetSpacing(1, 1, 1)  # Adjust as needed

print(image_stack.dtype)
# Convert numpy array to VTK array
vtk_array = vtk.vtkUnsignedCharArray()
vtk_array.SetNumberOfComponents(1)
vtk_array.SetArray(image_stack.ravel(), np.prod(image_stack.shape), False)
vtk_volume.GetPointData().SetScalars(vtk_array)

# Create a renderer
renderer = vtk.vtkRenderer()

# Create a volume property
volume_property = vtk.vtkVolumeProperty()

# Create an alpha transfer function for transparency
alpha_function = vtk.vtkPiecewiseFunction()
alpha_function.AddPoint(0, 0.0)  # Background is fully transparent
alpha_function.AddPoint(255, 1.0)  # Foreground is fully opaque
volume_property.SetScalarOpacity(alpha_function)

# Create a volume mapper
volume_mapper = vtk.vtkGPUVolumeRayCastMapper()
volume_mapper.SetInputData(vtk_volume)

# Create a volume actor
volume_actor = vtk.vtkVolume()
volume_actor.SetMapper(volume_mapper)
volume_actor.SetProperty(volume_property)

# Add the volume actor to the renderer
renderer.AddVolume(volume_actor)

# Create a render window
render_window = vtk.vtkRenderWindow()
render_window.AddRenderer(renderer)

# Create a render window interactor
render_window_interactor = vtk.vtkRenderWindowInteractor()
render_window_interactor.SetRenderWindow(render_window)

# Set up interactor style
interactor_style = vtk.vtkInteractorStyleTrackballCamera()
render_window_interactor.SetInteractorStyle(interactor_style)

i = 0
MT_count = 0
point_count = 0
if len(points) != 0:
    MT_count += 1
    point_count += 1
while i < len(points) - 1:
    if points[i] == ' ':
        i += 1
        MT_count += 1
    else:
        point_count +=1
        i += 1
print("Microtubules:", " ", MT_count)
print("Points rendered:", " ", point_count/3)

def realise_Sphere(x, y, z, previous_sphere_actor = None):
    global sphere_source, sphere_mapper, sphere_actor, line_source, line_mapper, line_actor
    # Create a sphere source
    sphere_source = vtk.vtkSphereSource()
    sphere_source.SetCenter(x, y, z)
    sphere_source.SetRadius(3)  
    sphere_source.SetPhiResolution(20)
    sphere_source.SetThetaResolution(20)

    # Create a mapper for the sphere
    sphere_mapper = vtk.vtkPolyDataMapper()
    sphere_mapper.SetInputConnection(sphere_source.GetOutputPort())

    # Create an actor for the sphere
    sphere_actor = vtk.vtkActor()
    sphere_actor.SetMapper(sphere_mapper)
    sphere_actor.GetProperty().SetColor(0.0, 1.0, 0.0)  # Set sphere color
    
    renderer.AddActor(sphere_actor)
    
    if previous_sphere_actor != None:
        prev_x, prev_y, prev_z = previous_sphere_actor.GetCenter()
        # Create a line source to connect spheres
        line_source = vtk.vtkLineSource()
        

        # Create a mapper for line geometries
        line_mapper = vtk.vtkPolyDataMapper()
        line_mapper.SetInputConnection(line_source.GetOutputPort())

        # Create a line geometry actor
        line_actor = vtk.vtkActor()
        line_actor.SetMapper(line_mapper)
        line_actor.GetProperty().SetColor(0.0, 1.0, 0.0)  # Set line color
        
        line_source.SetPoint1(prev_x, prev_y, prev_z)
        line_source.SetPoint2(x, y, z)
        
        renderer.AddActor(line_actor)
    return sphere_actor

i = 0

while i < len(points) - 1:
    if points[i] == ' ':
        previous_sphere_actor = None
        i += 1
    elif i == 0:
        previous_sphere_actor = realise_Sphere(points[i], points[i + 1], points[i + 2])
        i += 3
    else:
        previous_sphere_actor = realise_Sphere(points[i], points[i + 1], points[i + 2], previous_sphere_actor)
        i += 3

def keyboard_callback(obj, event):
    global render_window
    key = render_window_interactor.GetKeySym()
    if key == "Escape":
        print("Closing")
        render_window.Finalize()
        del render_window
        os._exit(0)

render_window_interactor.AddObserver(vtkCommand.KeyPressEvent, keyboard_callback)

render_window.Render()
render_window_interactor.Start()


