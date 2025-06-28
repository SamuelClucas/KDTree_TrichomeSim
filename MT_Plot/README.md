MT_Plot – Cortical Microtubule Coordinate Visualisation Tool
MT_Plot is a pair of simple scripts written during an internship at the Sainsbury Laboratory, University of Cambridge. The tool was developed in the final weeks of a placement investigating the spatial dynamics of microtubule arrays in simulated plant trichome cells. It was written to facilitate inspection of raw cortical microtubule coordinates exported from TrichomeSim.

Overview
TrichomeSim produces 3D geometries of epidermal cells, where microtubules are simulated on the cortical surface. During the project, visual inspection of microtubule data was required to qualitatively assess alignment, curvature, and surface constraints.

MT_Plot was developed as a utility to:

Load raw 3D coordinate files containing microtubule positions

Render these coordinates as 2D or 3D scatter plots

Perform simple preprocessing such as scaling, slicing, or filtering

This tool was intended for internal use and quick iteration, with minimal setup or dependencies.

File Contents
MT_Plot_2D.py:
A 2D scatter plot tool for flattened inspection of cortical microtubules across the x–z plane.
Data is expected to be in CSV format, with each row representing a 3D point.

MT_Plot_3D.py:
A 3D scatter renderer using matplotlib, with options for rotating and inspecting distributions in space.

academic_poster.pdf:
Poster presented at the Gatsby Plant Science Network Conference, Oxford (2023), describing this work in context.

Requirements
This project was written in Python 3. Minimal libraries are required:

bash
Copy
Edit
pip install numpy matplotlib
Data Format
Both scripts expect a text-based input file of 3D coordinates, one point per line:

python-repl
Copy
Edit
x1 y1 z1
x2 y2 z2
...
The delimiter can be whitespace or a comma; adjust parsing in the script if needed.

Update the filename variable in the script manually before running. These were originally tailored to local mesh exports from TrichomeSim.

Usage
2D plot:

bash
Copy
Edit
python MT_Plot_2D.py
3D plot:

bash
Copy
Edit
python MT_Plot_3D.py
These are standalone scripts. This project is provided for archival purposes.

Author
Samuel Clucas
Durham University (BSc, Biological Sciences, First Class)
Incoming MRes Student – Biomedical Data Science, Imperial College London

Funding provided by The Gatsby Charitable Foundation


