import attr


@attr.s
class UART:
    path = attr.ib()
    rate = attr.ib(default=115200)
    timeout = attr.ib(default=0.1)
    buf_size = attr.ib(default=10)
    _device = attr.ib(init=False)

    def __enter__(self, *args):
        self._device = Serial(self.path, self.rate, timeout=self.timeout)
        return self

    def __exit__(self, *args):
        if self._device is not None:
            self._device.close()
            self._device = None

    def send_data(self, data):
        data = data[:self.buf_size]
        data = bytearray(data)
        data.extend(bytearray(self.buf_size - len(data)))
        self._device.write(data)

    def send(self, cmd, params):
        self.send_data([cmd] + params)

    def read(self, length):
        return self._device.read(length)
