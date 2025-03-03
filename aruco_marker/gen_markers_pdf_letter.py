import os
import sys
dynamic_path = os.path.abspath(__file__+"/../")
# print(dynamic_path)
sys.path.append(dynamic_path)
from utility import gen_aruco_marker
import cv2
import numpy as np
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from typing import List, Tuple


def gen_marker_board_letter(aruco_dict:cv2.aruco_Dictionary, num_markers:int, positions:List[Tuple[float, float]],
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

    # Convert positions to pixels
    positions_px = [(int(x * dpi), int(y * dpi)) for x, y in positions]

    # Generate a list of markers
    markers = []

    for marker_id in range(num_markers):
        marker = gen_aruco_marker(aruco_dict, marker_id, marker_size_px)
        markers.append(marker)
        image_save_path = os.path.join(save_folder, f'marker_{marker_id}_letter.png')
        cv2.imwrite(image_save_path, marker)  # Save the markers as images (optional)

    # Create a new PDF
    pdf_file = os.path.join(save_folder, 'markers.pdf')
    c = canvas.Canvas(pdf_file, pagesize=letter)

    # Convert cm to points (1 cm = 28.3465 points)
    cm_to_pt = 28.3465

    # Convert cm to points (1 pt = 1/72 inch, 1 inch = 2.54 cm)
    inch_to_pt = 72/2.54

    # Page size in centimeters
    page_width_cm, page_height_cm = letter[0] / cm_to_pt, letter[1] / cm_to_pt

    # Convert page size to pixels
    page_width_px, page_height_px = int(page_width_cm * dpi), int(page_height_cm * dpi)

    # Ensure markers fit within the page
    assert max(x + marker_size_px for x, y in positions_px) <= page_width_px, "Markers exceed page width"
    assert max(y + marker_size_px for x, y in positions_px) <= page_height_px, "Markers exceed page height"

    # Add each marker to the PDF at its respective position
    count = 0
    for pos, marker in zip(positions_px, markers):
        x, y = pos
        x_pt = x /dpi * inch_to_pt
        y_pt = (page_height_px - (y + marker_size_px)) / dpi * inch_to_pt
        marker_img_path = os.path.join(save_folder, f'marker_{count}_letter.png')
        c.drawImage(marker_img_path, x_pt, y_pt, width=marker_size_px / dpi * inch_to_pt,
                    height=marker_size_px / dpi * inch_to_pt)
        count += 1

    # Save the PDF
    c.save()


if __name__ == "__main__":
    # Marker size in centimeters
    marker_size_cm = 1.5  # e.g., each marker is 5 cm x 5 cm

    # Resolution (DPI)
    dpi = 100  # pixels per centimeter

    # Define the dictionary to use for generating the markers
    # aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)
    aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_4X4_50)

    num_markers = 1

    # Relative positions in centimeters
    positions_cm = [
        (1, 1),
        (11, 11)
    ]

    save_folder = os.path.join(dynamic_path, 'gen_pdf_letter')

    if not os.path.exists(save_folder):
        os.mkdir(save_folder)
        print('Created folder', save_folder)

    gen_marker_board_letter(aruco_dict, num_markers, positions_cm, marker_size_cm, dpi, save_folder)

    print('Done')


