import os
import sys
dynamic_path = os.path.abspath(__file__+"/../")
# print(dynamic_path)
sys.path.append(dynamic_path)
from utility import gen_aruco_marker
import cv2
import numpy as np
from typing import List, Tuple

def gen_marker_board(markers: List[np.ndarray], positions: List[Tuple[float, float]], marker_size: float, dpi: int)-> np.ndarray:
    '''
    generate the marker board image with aruco markers
    :param markers: a list of markers generated
    :param positions: relative positions in centimeters
    :param marker_size: the size of the markers in centimeters
    :param dpi: pixels per centimeter
    :return:
    '''
    # Convert positions to pixels
    positions_px = [(int(x * dpi), int(y * dpi)) for x, y in positions]

    # Marker size in pixels
    marker_size_px = int(marker_size * dpi)

    # Calculate the size of the combined image
    max_x = max(pos[0] for pos in positions_px) + marker_size_px
    max_y = max(pos[1] for pos in positions_px) + marker_size_px

    # # Create a blank black image to hold all markers
    # combined_image = np.zeros((max_y, max_x), dtype=np.uint8)

    # Create a blank white image to hold all markers
    combined_image = (np.ones((max_y, max_x)) * 255).astype(np.uint8)

    # Place each marker at its respective position
    for pos, marker in zip(positions_px, markers):
        x, y = pos
        combined_image[y:y + marker_size_px, x:x + marker_size_px] = marker

    return combined_image


if __name__ == "__main__":
    # Marker size in centimeters
    marker_size_cm = 2  # e.g., each marker is 5 cm x 5 cm

    # Resolution (DPI)
    dpi = 100  # pixels per centimeter

    # Marker size in pixels
    marker_size_px = marker_size_cm * dpi

    # Define the dictionary to use for generating the markers
    aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)

    # Generate a list of markers
    num_markers = 5
    markers = []

    for marker_id in range(num_markers):
        marker = gen_aruco_marker(aruco_dict, marker_id, marker_size_px)
        markers.append(marker)

    # Save the markers as images (optional)
    # for i, marker in enumerate(markers):
    #     cv2.imwrite(f'marker_{i}.png', marker)

    # Relative positions in centimeters
    positions_cm = [
        (0, 0),
        (10, 0),
        (0, 10),
        (10, 10),
        (5, 5)
    ]

    combined_image = gen_marker_board(markers, positions_cm, marker_size_cm, dpi)

    # Save the combined image
    # cv2.imwrite('combined_markers.png', combined_image)

    # Display the combined image (optional)
    cv2.imshow('Combined Markers', combined_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
