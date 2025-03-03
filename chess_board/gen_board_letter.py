import os
import sys
dynamic_path = os.path.abspath(__file__+"/../")
# print(dynamic_path)
sys.path.append(dynamic_path)
from utility import create_chessboard, cm_to_points
import cv2
import numpy as np
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from typing import List, Tuple


def gen_chess_boards_letter(save_folder:str, chessboard_params:List[Tuple[int, int, float]], dpi:int, gap_cm:float,
                            margins_cm:Tuple[float, float, float, float], output_pdf:str)->None:
    """
    Save multiple chessboards to a single PDF file using ReportLab with specified gaps and margins.

    Parameters:
    chessboard_params (list): List of tuples containing (rows, cols, square_size_cm) for each chessboard.
    dpi (int): Dots per inch for resolution.
    gap_cm (float): Gap between chessboards in centimeters.
    margins_cm (tuple): Margins (top, bottom, left, right) in centimeters.
    output_pdf (str): Output PDF filename.
    """
    c = canvas.Canvas(output_pdf, pagesize=letter)
    page_width, page_height = letter

    gap_points = cm_to_points(gap_cm)  # Convert gap from cm to points
    top_margin, bottom_margin, left_margin, right_margin = [cm_to_points(m) for m in margins_cm]

    current_y = page_height - top_margin  # Start below the top margin

    for idx, (rows, cols, square_size_cm) in enumerate(chessboard_params):
        # Create the chessboard pattern
        chessboard_image = create_chessboard(rows, cols, square_size_cm, dpi)

        # Save the chessboard image as PNG using OpenCV
        image_save_path = os.path.join(save_folder, f'chess_board_letter_{(idx + 1)}.png')
        cv2.imwrite(image_save_path, chessboard_image)

        # Calculate the chessboard size in points
        board_width_points = (cols * square_size_cm) / 2.54 * 72  # Convert cm to points
        board_height_points = (rows * square_size_cm) / 2.54 * 72  # Convert cm to points

        # Calculate the position to center the image horizontally and maintain margins
        x = left_margin + (page_width - left_margin - right_margin - board_width_points) / 2
        current_y -= (board_height_points + gap_points)  # Move down by the height of the board and gap

        # If chessboard does not fit on the current page, start a new page
        if current_y < bottom_margin:
            c.showPage()
            current_y = page_height - top_margin - board_height_points - gap_points

        y = current_y

        # Draw the image on the PDF
        c.drawImage(image_save_path, x, y, width=board_width_points, height=board_height_points)

    # Save the PDF
    c.save()
    print(f"PDF created successfully: {output_pdf}")


if __name__ == "__main__":
    save_folder = os.path.join(dynamic_path, 'gen_pdf_letter')

    if not os.path.exists(save_folder):
        os.mkdir(save_folder)
        print('Created folder', save_folder)

    output_pdf = os.path.join(save_folder, 'chess_board_letter.pdf')

    # Resolution (DPI)
    dpi = 300  # pixels per centimeter

    # List of chessboard configurations (rows, cols, square size in cm)
    chessboard_params = [
        (11, 10, 0.5),  # First chessboard
        (11, 10, 0.6),  # Second chessboard
        # (12, 10, 1.0),  # Third chessboard
        # Add more configurations as needed
    ]

    dpi = 300  # Resolution in dots per inch
    gap_cm = 3.0  # Gap between chessboards in centimeters
    margins_cm = (2.0, 2.0, 2.0, 2.0)  # Top, bottom, left, right margins in centimeters

    # Generate and save chessboards to a single PDF
    gen_chess_boards_letter(save_folder, chessboard_params, dpi, gap_cm, margins_cm, output_pdf)

    print('Done')
