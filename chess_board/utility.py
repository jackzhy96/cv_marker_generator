import cv2
import numpy as np


def cm_to_pixels(cm, dpi):
    """
    Convert centimeters to pixels based on the DPI.

    Parameters:
    cm (float): Size in centimeters.
    dpi (int): Dots per inch.

    Returns:
    int: Size in pixels.
    """
    inches = cm / 2.54  # Convert centimeters to inches
    pixels = int(inches * dpi)
    return pixels


def cm_to_points(cm):
    """
    Convert centimeters to points for PDF rendering.

    Parameters:
    cm (float): Size in centimeters.

    Returns:
    float: Size in points.
    """
    inches = cm / 2.54  # Convert centimeters to inches
    points = inches * 72  # Convert inches to points
    return points


def create_chessboard(rows, cols, square_size_cm, dpi):
    """
    Create a chessboard image with given number of rows and columns, and square size in cm.

    Parameters:
    rows (int): Number of rows in the chessboard.
    cols (int): Number of columns in the chessboard.
    square_size_cm (float): Size of each square in centimeters.
    dpi (int): Dots per inch for resolution.

    Returns:
    np.ndarray: An image of the chessboard pattern.
    """
    # Convert square size from cm to pixels
    square_size_px = cm_to_pixels(square_size_cm, dpi)

    # Calculate the total dimensions of the chessboard
    img_height = rows * square_size_px
    img_width = cols * square_size_px

    # Create a blank image
    chessboard = np.zeros((img_height, img_width), dtype=np.uint8)

    # Fill the chessboard with squares
    for i in range(rows):
        for j in range(cols):
            if (i + j) % 2 == 0:
                cv2.rectangle(
                    chessboard,
                    (j * square_size_px, i * square_size_px),
                    ((j + 1) * square_size_px, (i + 1) * square_size_px),
                    (255, 255, 255),
                    thickness=cv2.FILLED,
                )
    return chessboard



if __name__ == "__main__":
    test = 1