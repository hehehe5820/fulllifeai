try:
    import bluetooth
except ImportError:
    bluetooth = None

try:
    import wifi
except ImportError:
    wifi = None


def bluetooth_scan():
    if bluetooth is None:
        return ["蓝牙模块未安装或当前系统不支持"]
    try:
        devices = bluetooth.discover_devices(lookup_names=True)
        return devices
    except Exception as e:
        return [f"扫描失败:{str(e)}"]


def wifi_get_info():
    if wifi is None:
        return "wifi模块不支持当前系统"
    try:
        return str(wifi.radio.ipv4_address)
    except Exception as e:
        return f"获取WiFi信息失败:{e}"


def send_bluetooth_msg(mac, message):
    if bluetooth is None:
        return "蓝牙库未安装，无法发送消息"
    sock = None
    try:
        sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        sock.connect((mac, 1))
        sock.send(message)
        return "蓝牙消息发送完成"
    except Exception as e:
        return f"蓝牙发送失败：{str(e)}"
    finally:
        if sock is not None:
            sock.close()
