from ctypes import POINTER, cast
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


def _get_volume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_,
        CLSCTX_ALL,
        None
    )
    return cast(interface, POINTER(IAudioEndpointVolume))


def volume_up():
    volume = _get_volume()
    current = volume.GetMasterVolumeLevelScalar()
    volume.SetMasterVolumeLevelScalar(min(current + 0.1, 1.0), None)
    return "Volume increased."


def volume_down():
    volume = _get_volume()
    current = volume.GetMasterVolumeLevelScalar()
    volume.SetMasterVolumeLevelScalar(max(current - 0.1, 0.0), None)
    return "Volume decreased."


def mute():
    volume = _get_volume()
    volume.SetMute(1, None)
    return "Muted."


def unmute():
    volume = _get_volume()
    volume.SetMute(0, None)
    return "Unmuted."


def set_volume(level):
    volume = _get_volume()
    volume.SetMasterVolumeLevelScalar(level / 100, None)
    return f"Volume set to {level}%."