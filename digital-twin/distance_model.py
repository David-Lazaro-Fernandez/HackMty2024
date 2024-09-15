# I have the x and y pixels of the bounding box, which is equivalent to a person, i know the height of the person in meters
# also i positioned my camera at a height og 3.14 meters with an angle of inclination facing down of 30 degrees
# i want to calculate the distance between the camera and the person in meters

xmin, ymin, xmax, ymax = 926.4, 212.1, 1009.6, 430.0


height = ymax - ymin
width = xmax - xmin

import math

def calculate_person_height(y_known, height_known_person, y_other, camera_params):
    """
    Calculate the height of a person based on the known height of another person.

    Parameters:
    y_known (int): The y-coordinate (in pixels) of the bottom of the bounding box of the known person.
    height_known_person (float): The height of the known person in meters.
    y_other (int): The y-coordinate (in pixels) of the bottom of the bounding box of the other person.
    camera_params (dict): A dictionary containing camera parameters:
        - focal_length (float): The focal length of the camera in pixels.
        - sensor_height (float): The height of the camera sensor in meters.

    Returns:
    float: The estimated height of the other person in meters.
    """
    focal_length = camera_params['focal_length']
    sensor_height = camera_params['sensor_height']

    # Calculate the proportional height difference in pixels
    height_ratio = y_other / y_known

    # Use the known height of the person to calculate the height of the other person
    estimated_height = height_known_person * height_ratio
    
    return estimated_height

# Example usage
y_known_person = 1000  # Bottom of bounding box for the known person in pixels
height_known_person = 1.75  # Known height of the person in meters
y_other_person = 800  # Bottom of bounding box for the other person in pixels

camera_params = {
    'focal_length': 1620,  # in pixels
    'sensor_height': 0.0024  # in meters (sensor height)
}

estimated_height_other_person = calculate_person_height(y_known_person, height_known_person, y_other_person, camera_params)
print(f"Estimated height of the other person: {estimated_height_other_person:.2f} meters")

# Calculate the distance between the camera and the person
def calculate_distance_to_person(y_person, height_person, camera_height, camera_angle):
    """
    Calculate the distance between the camera and a person based on their height and position in the frame.

    Parameters:
    y_person (int): The y-coordinate (in pixels) of the bottom of the bounding box of the person.
    height_person (float): The height of the person in meters.
    camera_height (float): The height of the camera above the ground in meters.
    camera_angle (float): The angle of inclination of the camera in degrees.

    Returns:
    float: The estimated distance between the camera and the person in meters.
    """
    # Convert the camera angle to radians
    camera_angle_rad = math.radians(camera_angle)

    # Calculate the vertical distance from the camera to the person
    vertical_distance = camera_height / math.tan(camera_angle_rad)

    # Calculate the proportional height difference in pixels
    height_ratio = y_person / camera_height

    # Use the known height of the person to calculate the distance to the person
    estimated_distance = vertical_distance / height_ratio

    return estimated_distance