import os
import sys
dynamic_path = os.path.abspath(__file__+"/../")
# print(dynamic_path)
sys.path.append(dynamic_path)
from utility import gen_aruco_marker
import cv2
import numpy as np
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from typing import List, Tuple


def gen_marker_board_a4(aruco_dict:cv2.aruco_Dictionary, num_markers:int, positions:List[Tuple[float, float]],
                        marker_size:float, dpi:int, save_folder:str)->None:
    '''
    generate a PDF file including multiple Aruco markers in A4 size
    :param aruco_dict: the defined aruco dictionary from cv2
    :param num_markers: number of markers to generate
    :param positions: relative positions of the markers in cm
    :param marker_size: marker size in cm
    :param dpi: pixels per cm
    :return: generate a pdf file and series of images of markers
    '''
    # Marker size in pixels
    marker_size_px = int(marker_size * dpi)

    # Generate a list of markers
    markers = []

    for marker_id in range(num_markers):
        marker = gen_aruco_marker(aruco_dict, marker_id, marker_size_px)
        markers.append(marker)
        image_save_path = os.path.join(save_folder, f'marker_{marker_id}_A4.png')
        cv2.imwrite(image_save_path, marker)  # Save the markers as images (optional)

    # Create a new PDF
    pdf_file = os.path.join(save_folder, 'markers.pdf')
    c = canvas.Canvas(pdf_file, pagesize=A4)

    # Convert cm to points (1 cm = 28.3465 points)
    cm_to_pt = 28.3465

    # Add each marker to the PDF at its respective position
    for marker_id, (x_cm, y_cm) in enumerate(positions):
        x_pt = x_cm * cm_to_pt
        y_pt = A4[1] - (y_cm + marker_size_cm) * cm_to_pt  # Convert y-coordinate and adjust for PDF origin at bottom-left
        marker_img_path = os.path.join(save_folder, f'marker_{marker_id}_A4.png')
        c.drawImage(marker_img_path, x_pt, y_pt, width=marker_size_cm * cm_to_pt, height=marker_size_cm * cm_to_pt)

    # Save the PDF
    c.save()


if __name__ == "__main__":
    # Marker size in centimeters
    marker_size_cm = 3  # e.g., each marker is 5 cm x 5 cm

    # Resolution (DPI)
    dpi = 100  # pixels per centimeter

    # Define the dictionary to use for generating the markers
    aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)

    num_markers = 2

    # Relative positions in centimeters
    positions_cm = [
        (1, 1),
        (11, 11)
    ]

    save_folder = os.path.join(dynamic_path, 'gen_pdf_a4')

    if not os.path.exists(save_folder):
        os.mkdir(save_folder)
        print('Created folder', save_folder)

    gen_marker_board_a4(aruco_dict, num_markers, positions_cm, marker_size_cm, dpi, save_folder)

    print('Done')

