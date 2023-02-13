# Cat Face Detection and Cut

This code is designed to detect the cat face in an image and cut it out. The code is written in Python and uses the opencv library to detect the cat face. The detection is performed using the haarcascade classifier, and the cut is done based on the coordinates of the detected face.

## Dependencies

- os
- cv2
- math

## Usage

1. Run the code by calling the `load()` function.
2. Input the breed of the cat, and the code will automatically detect the cat face and cut it out in the original images under the specified directory.
3. The cut cat face will be saved in the specified location.

## Main Functions

### `detect(filename)`

This function is used to detect the cat face in an image. It uses the haarcascade classifier to perform the detection and returns the coordinates of the cat face.

### `cut(filename)`

This function is used to cut the cat face from the original image based on the coordinates returned by the `detect()` function.

### `load()`

This function is used to load the original images, and it will call the `cut()` function to detect and cut the cat face. The cut cat face will be saved in the specified location.

## Note

- The code is designed to work with a specific set of directories, so make sure to update the directory paths in the code before using it.
- The code may not work well on images with small cat faces, and the detection may return incorrect results.

