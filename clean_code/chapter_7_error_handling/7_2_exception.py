import logging
from enum import Enum, auto

class Device:
    id: int
    pass


class DeviceStatus(Enum):
    DEVICE_SUSPENDED = auto()

class DeviceRecord(object):
    def get_status(self) -> DeviceStatus:
        pass


class DeviceShutDownError(Exception):
    pass


class DeviceHandle(Enum):
    INVALID = auto()


class DeviceController(object):
    """
    Notice how much cleaner it is. This isn’t just a matter of aesthetics. The code is
    better because two concerns that were tangled, the algorithm for device shutdown
    and error handling, are now separated. You can look at each of those concerns
    and understand them independently.
    """

    def get_handle(self, device_id: int) -> DeviceHandle:
        raise DeviceShutDownError("Invalid handle for: " + str(device_id))

    def send_shut_down(self):
        try:
            self.try_to_shut_down()
        except DeviceShutDownError as e:
            logging.exception(e)

    def try_to_shut_down(self, device: Device) -> None:
        handle: DeviceHandle = self.get_handle(device.id)
        record: DeviceRecord = self.retrieve_device_record(handle)

        self.pause_device(handle)
        self.clear_device_work_queue(handle)
        self.close_device(handle)

    def retrieve_device_record(self, handle) -> DeviceRecord:
        pass

    def pause_device(self, handle):
        pass

    def clear_device_work_queue(self, handle):
        pass

    def close_device(self, handle):
        pass

