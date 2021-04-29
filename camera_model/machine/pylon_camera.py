from time import sleep
from pypylon import pylon
import exception
from image import Image
from . import Camera
from ..configs.pylon_camera_config import PylonCameraConfig
import threading


class PylonCamera(Camera):
    _camera: pylon.InstantCamera
    _converter: pylon.ImageFormatConverter
    _config: PylonCameraConfig
    _image_lock: threading.Lock

    def __init__(self, config: PylonCameraConfig):
        self._camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
        self._config = config
        self._image_lock = threading.Lock()
        self.converter = pylon.ImageFormatConverter()
        self.converter.OutputPixelFormat = pylon.PixelType_BGR8packed
        self.converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned

    def open(self) -> None:
        self._camera.Open()
        self._camera.AcquisitionControl.GetFeatures()[3].SetValue(self._config.shutter_mode)
        self._camera.ExposureTime = self._config.exposure_time
        self._camera.Width = self._config.width
        self._camera.Height = self._config.height
        self._camera.BalanceWhiteAuto = 'Once'
        sleep(self._config.delay)
        self._camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)


    def get_image(self) -> Image:
        with self._image_lock:
            if not self._camera.IsGrabbing():
                raise exception.CameraNotOpenedError()

            grab_result = self._camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
            assert isinstance(grab_result, pylon.GrabResult)

            if not grab_result.GrabSucceeded():
                grab_result.Release()
                raise exception.CameraGetFailedError(
                    f"code: {grab_result.GetErrorCode()}, desc: {grab_result.GetErrorDescription()}"
                )

            img = self.converter.Convert(grab_result).GetArray()
            grab_result.Release()
            return img

    def close(self) -> None:
        self._camera.Close()

