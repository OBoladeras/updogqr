import os
import sys
import qrcode
import netifaces
import threading


class UpdogQR:
    def __init__(self):
        self.img_pid = None
        self.img_path = "qr.png"

        self.link = f"http://{self.get_ip_address()}:9090"

    def generate_qr_code(self):
        print("Generating QR code...\n")

        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(self.link)
        qr.make(fit=True)
        qr_img = qr.make_image(fill="black", back_color="white")

        try:
            qr_img.show()
        except:
            try:
                qr_img.save(self.img_path)
            except:
                try:
                    self.img_path = "/tmp/qr.png"
                    qr_img.save(self.img_path)
                except:
                    print("Error generating the image")

            self.img_pid = os.system(f"open {self.img_path}")

    def get_ip_address(self):
        interfaces = netifaces.interfaces()

        for iface in interfaces:
            addresses = netifaces.ifaddresses(iface)
            if netifaces.AF_INET in addresses:
                for addr in addresses[netifaces.AF_INET]:
                    ip = addr['addr']
                    if not ip.startswith('127.') and not ip.startswith('169.254.'):
                        return ip

        return None

    def start(self):
        threading.Thread(target=self.generate_qr_code).start()

        try:
            dir = os.path.dirname(sys.executable)

            os.system(f"{dir}/updog")
        except KeyboardInterrupt:
            exit(0)
        finally:
            if os.path.exists(self.img_path):
                os.system(f"rm {self.img_path}")

            if self.img_pid is not None:
                os.system(f"kill {self.img_pid}")


def main():
    UpdogQR().start()


if __name__ == "__main__":
    main()
