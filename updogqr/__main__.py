import os
import qrcode
import socket
import threading


def generate_qr_code(link):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(link)
    qr.make(fit=True)
    qr_img = qr.make_image(fill="black", back_color="white")
    qr_img.show()


def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address


def main():
    ip = get_ip_address()
    threading.Thread(target=generate_qr_code,
                     args=(f"http://{ip}:9090",)).start()
    try:
        os.system("updog")
    except KeyboardInterrupt:
        exit(0)


if __name__ == "__main__":
    main()
