class BLECore:
    def __init__(self):
        print("BLE communication core initialized.")

    def connect_device(self, device_id):
        print(f"Connecting to BLE device: {device_id}")
        return True

if __name__ == "__main__":
    ble = BLECore()
    ble.connect_device("my_ble_device")
