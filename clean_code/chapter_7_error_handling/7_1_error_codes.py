import logging
from enum import Enum, auto


class Device:
    id: int
    pass


class DeviceHandle(Enum):
    INVALID = auto()


class DeviceStatus(Enum):
    DEVICE_SUSPENDED = auto()


class DeviceRecord(object):
    def get_status(self) -> DeviceStatus:
        pass


class DeviceController(object):
    """
    The problem with these approaches is that they clutter the caller.
    The caller must check for errors immediately after the call.
    Unfortunately, it’s easy to forget. For this reason it is better to
     throw an exception when you encounter an error. The calling code is cleaner.
     Its logic is not obscured by error handling.    
    """


    record: DeviceRecord

    def get_handle(self, device_id: int) -> DeviceHandle:
        pass

    def send_shut_down(self, device: Device) -> None:
        handle: DeviceHandle = self.get_handle(device.id)

        # Check the state of the device
        if handle != DeviceHandle.INVALID:
            # Save the device status to the record field 
            self.retrieve_device_record(handle)
            # If not suspended, shut down
            if self.record.get_status() != DeviceStatus.DEVICE_SUSPENDED:
                self.pause_device(handle)
                self.clear_device_work_queue(handle)
                self.close_device(handle)
            else:
                logging.log("Device suspended. Unable to shut down")
        else:
            logging.log("Invalid handle for: " + str(device))

    def retrieve_device_record(self, handle):
        pass

    def shut_down(self, handle):
        pass

    def pause_device(self, handle):
        pass

    def clear_device_work_queue(self, handle):
        pass

    def close_device(self, handle):
        pass
