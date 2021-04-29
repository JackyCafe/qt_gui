import cv2

from camera_model.machine import Camera
from image import Image


class RotatedCamera(Camera):
    _camera: Camera
    _rotate_method: int

    def __init__(self, camera: Camera, rotate_method: int):
        self._camera = camera
        self._rotate_method = rotate_method

    def open(self) -> None:
        self._camera.open()

    def get_image(self) -> Image:
        image = self._camera.get_image()
        return cv2.rotate(image, self._rotate_method)

    def close(self) -> None:
        self._camera.close()