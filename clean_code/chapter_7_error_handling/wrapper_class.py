import logging as log


class GMXError(Exception):
    pass


class DeviceResponseException(Exception):
    pass


class ATM1212UnlockedException(Exception):
    pass


class ACMEPort:
    def __init__(self, port_number: int):
        self.port_number = port_number

    pass

    def open(self):
        pass

    def close(self):
        pass



def reportPortError(e: Exception):
    log.exception(f"Report {e}")


"""
That statement contains a lot of duplication, and we shouldn’t be surprised. 
In most exception handling situations, the work that we do is relatively 
standard regardless of the actual cause. We have to record an error and make sure that 
we can proceed.
"""

try:
    port = ACMEPort(12)
    port.open()
except DeviceResponseException as e:
    reportPortError(e)
    log.exception("Device response exception", e)
except ATM1212UnlockedException as e:
    reportPortError(e)
    log.exception("Unlock exception", e)
except GMXError as e:
    reportPortError(e)
    log.exception("Device response exception", e)
finally:
    port.close()

"""
In this case, because we know that the work that we are doing is roughly the same 
regardless of the exception, we can simplify our code considerably by wrapping 
the API that we are calling and making sure that it returns a common exception type:
"""

class PortDeviceFailure(Exception):
    pass


class LocalPort(ACMEPort):
    def __init__(self, port_number: int):
        super().__init__(port_number)

    def open(self):
        try:
            super().open()
        except DeviceResponseException as e:
            raise PortDeviceFailure("Device response exception") from e
        except ATM1212UnlockedException as e:
            raise PortDeviceFailure("Device response exception") from e
        except GMXError as e:
            raise PortDeviceFailure("Device response exception") from e

    def close(self):
        pass


"""
Better yet, we can use a decorator to wrap the API calls:
"""
try:
    port = LocalPort(12)
    port.open()
except PortDeviceFailure as e:
    reportPortError(e)
    log.exception("Device response exception", e)
finally:
    port.close()
