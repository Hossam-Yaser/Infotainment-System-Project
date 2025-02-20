# Infotainment System

![Raspberry Pi Icon](https://img.icons8.com/color/48/000000/raspberry-pi.png) ![Embedded Linux Icon](https://img.icons8.com/color/48/000000/linux.png) ![Yocto Project Icon](./images/Yocto-Project.png)

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

## 🚀 Running the Application over Raspbian OS  
Follow these steps to run the application on **Raspbian OS** for Raspberry Pi 5:  

1. **Set up the application dependencies:**  
   - Install the following packages and modules:
     - `python3`
     - `qt5`
     - `cv2`
     - `sys`
     - `os`
     - YOLO version 8 (nano)
     - `ultralytics`
     - `requests`  
   
   You can install the required Python packages using `pip`:
   **Install `pip`:**  
   - Update the package list and install `pip` for Python 3:
   ```bash
   sudo apt update
   sudo apt install python3-pip
   ```
   ```bash
   pip install opencv-python-headless ultralytics requests
   ```

### 💡 Hint: We also ran the application using our **customized Yocto image**. You can find the detailed steps in the [Yocto Directory](#repository-structure).  

## Repository Structure
```
📂 Infotainment-System
├── 📁 Yocto
│   ├── README.md
│   ├── 📁 image.zip
├── 📁 Source code
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

