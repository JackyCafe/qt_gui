import abc

from image import Image


class Camera(abc.ABC):

    @abc.abstractmethod
    def open(self) -> None:
        pass

    @abc.abstractmethod
    def get_image(self) -> Image:
        pass

    @abc.abstractmethod
    def close(self) -> None:
        pass