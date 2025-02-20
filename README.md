# Infotainment System

![Raspberry Pi Icon](https://img.icons8.com/color/48/000000/raspberry-pi.png) ![Embedded Linux Icon](https://img.icons8.com/color/48/000000/linux.png) ![Yocto Project Icon](./images/yocto-project-logo.jpg)

## Project Overview
The **Infotainment System** is an Embedded Linux project developed as part of the **Embedded Linux Scholarship** by **AMIT** and **Orange Digital Center (ODC)**. This project showcases building a custom **Yocto-based Linux distribution** for the **Raspberry Pi 5** with various hardware peripherals.

## Hardware Components
- ![Raspberry Pi Icon](https://img.icons8.com/color/48/000000/raspberry-pi.png) **Raspberry Pi 5** with 8GB RAM
  
- ![LED Icon](https://img.icons8.com/color/48/000000/led-diode.png) **LED as Light Indicator**

- ![Relay Icon](https://img.icons8.com/fluency/48/000000/relay.png) **Relay-controlled Fan** (represented by a Yellow LED)

- ![Touchscreen Icon](https://img.icons8.com/color/48/000000/touchscreen-smartphone.png) **Touch Screen** (800x480 pixels, driver included with Raspbian OS)

## Project Features
- Custom Linux image built using **Yocto**
- Relay-based fan control using LEDs
- Light Indicator
- Traffic Sign Recognition using AI model Computer Vision YOLO V.8 (nano version)
- Interactive UI on a touch screen


## Building the Yocto Image
Follow these steps to build and deploy the custom Yocto image for the Raspberry Pi 5.

### Step 1: Install Yocto Build Environment
1. Install necessary packages for your development environment:
   ```bash
   sudo apt-get update && sudo apt-get install gawk wget git-core diffstat unzip texinfo gcc-multilib build-essential chrpath socat libsdl1.2-dev xterm
   ```
2. Download the Yocto Project source:
   ```bash
   git clone git://git.yoctoproject.org/poky
   cd poky
   ```

### Step 2: Configure the Build
1. Check out the latest branch compatible with Raspberry Pi 5:
   ```bash
   git checkout kirkstone
   ```
2. Initialize the environment:
   ```bash
   source oe-init-build-env
   ```

### Step 3: Layer Configuration
1. Add necessary layers for Raspberry Pi support:
   ```bash
   bitbake-layers add-layer meta-raspberrypi
   ```
2. Update the `conf/local.conf` file with the following:
   ```plaintext
   MACHINE = "raspberrypi5"
   ```

### Step 4: Build the Image
1. Run the Yocto build command:
   ```bash
   bitbake core-image-sato
   ```

### Step 5: Flash the Image
1. Use `dd` to write the image to an SD card:
   ```bash
   sudo dd if=core-image-sato-raspberrypi5.rpi-sdimg of=/dev/sdX bs=4M
   ```

2. Insert the SD card into the Raspberry Pi and power it on.

### Step 6: Upload Code to Raspberry Pi
1. Use `scp` to upload code to the Raspberry Pi:
   ```bash
   scp your_code.py pi@raspberrypi.local:/home/pi/
   ```

2. SSH into the Raspberry Pi to run the code:
   ```bash
   ssh pi@raspberrypi.local
   python3 /home/pi/your_code.py
   ```

## Repository Structure
```
📂 Infotainment-System
├── 📁 Yocto
│   ├── README.md
│   ├── build_instructions.md
├── 📁 Sourc code
│   ├── mainApp.py
│   ├── software_architecutre.md
├── 📁 Hardware
│   ├── schematics.pdf
│   ├── components_list.md
└── README.md
```

# 🛠️ Technologies & Tools  
<p align="left">
  <a href="https://www.w3schools.com/cpp/" target="_blank">
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/cplusplus/cplusplus-original.svg" alt="C++" width="40" height="40"/>
  </a>
  <a href="https://www.python.org" target="_blank">
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="Python" width="40" height="40"/>
  </a>
  <a href="https://git-scm.com/" target="_blank">
    <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="Git" width="40" height="40"/>
  </a>
  <a href="https://www.qt.io/" target="_blank">
    <img src="https://upload.wikimedia.org/wikipedia/commons/0/0b/Qt_logo_2016.svg" alt="QT" width="40" height="40"/>
  </a>
  <a href="https://www.tensorflow.org" target="_blank">
    <img src="https://www.vectorlogo.zone/logos/tensorflow/tensorflow-icon.svg" alt="TensorFlow" width="40" height="40"/>
  </a>
 <a href="https://www.linux.org/" target="_blank">
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/linux/linux-original.svg" alt="Linux" width="40" height="40"/>
  </a>
  <a href="https://opencv.org/" target="_blank">
    <img src="https://www.vectorlogo.zone/logos/opencv/opencv-icon.svg" alt="OpenCV" width="40" height="40"/>
  </a>
</p>

---

# 🌐 Connect with Us
**Mohammed Khalaf:**  
[![Github](https://img.shields.io/badge/-Github-000?style=flat&logo=Github&logoColor=white)](https://github.com/mohammedkh97)  [![Linkedin](https://img.shields.io/badge/-LinkedIn-blue?style=flat&logo=Linkedin&logoColor=white)](https://linkedin.com/in/mohammed-khalaf97)  [![Gmail](https://img.shields.io/badge/-Gmail-c14438?style=flat&logo=Gmail&logoColor=white)](mailto:Mohamedkhalaf20172020@gmail.com)  [![Facebook](https://img.shields.io/badge/-Facebook-1877F2?style=flat&logo=facebook&logoColor=white)](https://www.facebook.com//groups/1241072483656472)  [![WhatsApp](https://img.shields.io/badge/-WhatsApp-25D366?style=flat&logo=whatsapp&logoColor=white)](https://wa.me/+201022508443)  

**Hossam Abdel Hady:**  
[![Github](https://img.shields.io/badge/-Github-000?style=flat&logo=Github&logoColor=white)](https://github.com/hossam-yaser)  [![Linkedin](https://img.shields.io/badge/-LinkedIn-blue?style=flat&logo=Linkedin&logoColor=white)](https://linkedin.com/in/hossam-yasser-abdelhady)  [![Gmail](https://img.shields.io/badge/-Gmail-c14438?style=flat&logo=Gmail&logoColor=white)](mailto:hossamabdelhady000@gmail.com) [![Facebook](https://img.shields.io/badge/-Facebook-1877F2?style=flat&logo=facebook&logoColor=white)](https://www.facebook.com/Mr.Oscar.132)  [![WhatsApp](https://img.shields.io/badge/-WhatsApp-25D366?style=flat&logo=whatsapp&logoColor=white)](https://wa.me/+201112741722)  

**Saif-El-Dein Adel Fouad:**  
[![Github](https://img.shields.io/badge/-Github-000?style=flat&logo=Github&logoColor=white)](https://github.com/mohammedkh97)  [![Linkedin](https://img.shields.io/badge/-LinkedIn-blue?style=flat&logo=Linkedin&logoColor=white)](https://linkedin.com/in/mohammed-khalaf97)  [![Gmail](https://img.shields.io/badge/-Gmail-c14438?style=flat&logo=Gmail&logoColor=white)](mailto:Mohamedkhalaf20172020@gmail.com)  [![Facebook](https://img.shields.io/badge/-Facebook-1877F2?style=flat&logo=facebook&logoColor=white)](https://www.facebook.com//groups/1241072483656472)  [![WhatsApp](https://img.shields.io/badge/-WhatsApp-25D366?style=flat&logo=whatsapp&logoColor=white)](https://wa.me/+201002514819)  

**Mohammed Ahmed Salah:**  
[![Github](https://img.shields.io/badge/-Github-000?style=flat&logo=Github&logoColor=white)](https://github.com/mohammedkh97)  [![Linkedin](https://img.shields.io/badge/-LinkedIn-blue?style=flat&logo=Linkedin&logoColor=white)](https://linkedin.com/in/mohammed-khalaf97)  [![Gmail](https://img.shields.io/badge/-Gmail-c14438?style=flat&logo=Gmail&logoColor=white)](mailto:Mohamedkhalaf20172020@gmail.com)  [![Facebook](https://img.shields.io/badge/-Facebook-1877F2?style=flat&logo=facebook&logoColor=white)](https://www.facebook.com//groups/1241072483656472)  [![WhatsApp](https://img.shields.io/badge/-WhatsApp-25D366?style=flat&logo=whatsapp&logoColor=white)](https://wa.me/+201154558544)  

---


## Contact
For any questions or discussions, feel free to reach out to the team!

