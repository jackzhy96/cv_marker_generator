import cv2
import numpy as np




def gen_aruco_marker(aruco_dict:cv2.aruco_Dictionary, marker_id: int, marker_size: int, white_background:bool=False)->np.ndarray:
    '''
    draw the aruco marker with given information
    :param aruco_dict: the dictionary to use for generating the markers
    :param marker_id: the aruco marker id
    :param marker_size: the aruco marker size in pixel
    :return: the generated aruco marker
    '''
    # initialize the marker
    marker = np.zeros((marker_size,marker_size), dtype=np.uint8)
    # generate the marker
    marker = cv2.aruco.drawMarker(aruco_dict, marker_id, marker_size)
    if white_background:
        marker = ((marker - 255)*(-1)).astype(np.uint8)
    return marker

if __name__ == "__main__":
    test = 1

    # Define the dictionary to use for generating the markers
    aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)

    # Generate the first marker
    marker1_id = 1
    marker1_size = 200
    marker1 = gen_aruco_marker(aruco_dict, marker1_id, marker1_size, white_background=True)
    # cv2.imwrite('test.png', marker1)