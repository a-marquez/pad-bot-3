import webview
from ppadb.client import Client as AdbClient
# from uiautomator import Device
import uiautomator2 as u2

test_serials = ['299b2eedfb1c7ece', '3e6a404e']

class Api:
  def __init__(self):
    self.cancel_heavy_stuff_flag = False
    self.client = AdbClient(host="127.0.0.1", port=5037)
    self.devices = self.client.devices()

  def get_device_serials(self):
    self.devices = self.client.devices()
    return [*map(lambda device: device.serial, self.devices)]

  def toggle_device_screen(self, serial):
    response = self.client.device(serial).shell('input keyevent KEYCODE_POWER').strip()
    print(response)

  def multi_point_swipe(self, serial):
    # d = Device(serial)
    # d.click(500, 500)
    # d.long_click(300, 300)
    # d.screen.off()

    d = u2.connect(serial)
    return d.swipe_points([(200, 400), (500, 1000), (800, 1000)], .01)

if __name__ == '__main__':
  api = Api()
  # webview.create_window('Hey', 'http://127.0.0.1:5173/debug', js_api=api)
  # webview.start(debug=True)
  print(api.multi_point_swipe(test_serials[1]))

