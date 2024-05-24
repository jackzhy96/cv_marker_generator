# cv_marker_generator
A generator for CV markers

## Aruco Marker Generator
The folder `aruco_marker` has all scripts to generate the marker board images / PDFs.

The file names are self-explained.

Let's take [gen_marker_pdf_letter.py](aruco_marker/gen_markers_pdf_letter.py) as an example. 
This script is to generate a printable pdf for letter size paper.

### How to Run

In your terminal, run following commands:

```bash
cd ~/cv_marker_generator/aruco_marker/
python gen_markers_pdf_letter.py
```

It will generate a folder called `gen_pdf_letter` in the folder `aruco_marker`. The folder includes a printable PDF file 
and separate images for all the markers in the PDF file with PNG format.

### Parameters to Modify

Let's take [gen_marker_pdf_letter.py](aruco_marker/gen_markers_pdf_letter.py) as an example, the other files share 
the same name space.

1. Marker Size: change `marker_size_cm` at line [#77](https://github.com/JackHaoyingZhou/cv_marker_generator/blob/main/aruco_marker/gen_markers_pdf_letter.py#L77)
2. Marker Style: change `aruco_dict` at line [#83](https://github.com/JackHaoyingZhou/cv_marker_generator/blob/main/aruco_marker/gen_markers_pdf_letter.py#L83)
3. Number of Markers: change `number_markers` at line [#85](https://github.com/JackHaoyingZhou/cv_marker_generator/blob/main/aruco_marker/gen_markers_pdf_letter.py#L85), the unit is cm
4. Relative positions among markers: change `positions_cm` at line [#88](https://github.com/JackHaoyingZhou/cv_marker_generator/blob/main/aruco_marker/gen_markers_pdf_letter.py#L88), the unit is cm

## Other Marker Generator

To be continued ...