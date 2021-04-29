from fancy import config as cfg


class PylonCameraConfig(cfg.BaseConfig):
    exposure_time: int = cfg.Option(default=100, type=int)
    shutter_mode: str = cfg.Option(default="GlobalResetRelease", type=str)
    width: int = cfg.Option(required=True, type=int)
    height: int = cfg.Option(required=True, type=int)
    delay: float = cfg.Option(required=True, type=float)