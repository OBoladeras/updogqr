import os
import sys
import qrcode
import netifaces
import threading


def generate_qr_code(link):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(link)
    qr.make(fit=True)
    qr_img = qr.make_image(fill="black", back_color="white")
    try:
        qr_img.show()
    except:
        qr_img.save("qr.png")
        os.system("open qr.png")


def get_ip_address():
    interfaces = netifaces.interfaces()

    for iface in interfaces:
        addresses = netifaces.ifaddresses(iface)
        if netifaces.AF_INET in addresses:
            for addr in addresses[netifaces.AF_INET]:
                ip = addr['addr']
                if not ip.startswith('127.') and not ip.startswith('169.254.'):
                    return ip

    return None


def main():
    ip = get_ip_address()
    threading.Thread(target=generate_qr_code,
                     args=(f"http://{ip}:9090",)).start()

    try:
        python_executable = sys.executable
        dir = os.path.dirname(python_executable)

        os.system(f"{dir}/updog")
    except KeyboardInterrupt:
        exit(0)
    finally:
        if os.path.exists("qr.png"):
            os.system("rm qr.png")


if __name__ == "__main__":
    main()
