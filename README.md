# Updog QR 🗃️

## Description
It is a QR code generator that will generate a QR code for the user to scan and be directed to the Updog website.\
It can be usefull to move files from a computer to a phone or tablet. 📱\
This project is a extension of the Updog project.🐕‍🦺  


## Installation
The installation of this project is very simple, it can be installed the same in Windows and Linux, but the steps are different because of security reasons.

To install this project, follow these steps:


<div style="display: flex; gap: 5%; justify-content: center;">
<div>

### Windows 🪟
1. Clone the repository
    ```bash
    git clone https://github.com/OBoladeras/updogqr.git
    ```

2. Install the module
    ```bash
    pip install ./updogqr
    ```

</div>
<div>

### Linux 🐧
Note: In linux you may need to install the following packages:
```bash
sudo apt update
sudo apt install python3-dev python3-venv build-essential
```

<br>

1. Clone the repository
    ```bash
    git clone https://github.com/OBoladeras/updogqr.git
    cd updogqr
    ```

2. Create a virtual environment
    ```bash
    python -m venv .venv
    ```

3. Install the requirements
    ```bash
    .venv/bin/pip install .
    ```

4. Create an alias and activate it
    ```bash
    echo -e "\nalias updogqr='$(pwd)/.venv/bin/updogqr'" >> ~/.bashrc
    source ~/.bashrc
    ```

</div>
</div>


## Usage
To use this project, you just need to run the following command the folder where you want to send or receive files:

```bash
updogqr
```

This will generate a QR code that you can scan with your phone or tablet to be directed to the Updog website.🐕‍🦺


## Contributing
Contributions are welcome! Please follow these guidelines:
1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.


## License
This project is licensed under the [MIT License](LICENSE).
