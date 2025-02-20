## Building the Yocto Image
Follow these steps to build and deploy the custom Yocto image for the Raspberry Pi 5.

### Step 1: Install Yocto Build Environment
1. Install necessary packages for your development environment:
   ```bash
   sudo apt-get update && sudo apt-get install gawk wget git-core diffstat unzip texinfo gcc-multilib build-essential chrpath socat libsdl1.2-dev xterm
   ```
2. Download the Yocto Project source (Clone Poky):
   ```bash
   git clone -b kirkstone git://git.yoctoproject.org/poky
   cd poky
   ```

### Step 2: Configure the Build
1. Initialize the environment:
    source the oe-init-build-env environment setup script to define Yocto Project’s build environment on your build host
   ```bash
   source oe-init-build-env
   ```

### Step 3: Layer Configuration
1. Download raspberry pi 5 BSP (board support package):
    ```bash
    git clone git://git.yoctoproject.org/meta-raspberrypi.git
    ```
2. Add necessary layer for Raspberry Pi support (Board Support Package (BSP)):
   ```bash
   bitbake-layers add-layer meta-raspberrypi
   ```
3. Update the `conf/local.conf` file with the following:
   ```plaintext
    edit in local.conf :
        change the machine variable to:
        MACHINE ??= "raspberrypi5" 
        Add these two variables depending on your threads : 
            BB_NUMBER_THREADS = "6" 
            BB_PARALLEL_MAKE = "-j 6"
        The number 6 equals the number of the threads you have minus 1 or 2 to be able to deal with the system while building process
   ```
4. clone open embedded layer :
    ```bash
    git clone -b kirkstone git://git.openembedded.org/meta-openembedded
    ```
5. clone qt5 layer :
    ```bash
    git clone -b kirkstone https://github.com/meta-qt5/meta-qt5
    ```
6. Add all the Layers to your image :
    ```bash
    bitbake-layers add-layer  ../meta-openembedded/meta-*  ../meta-qt5
    ```

### Step 4: Build the Image
1. Run the Yocto build command:
   ```bash
   bitbake core-image-base
   ```

### After the build process the image will be created in this directory poky/build/tmp/deploy/images/raspberrypi5 ###

### Step 5 Create ISO Image
1. to create an iso image use this command after sourcing the oe-init-build-env :
    ```bash
    wic create  sdimage-raspberrypi -e core-image-base
    ```
### Step 6: Flash the Image

1. to flash this image to the sd card use this command :
    ```bash
    sudo dd if=sdimage-raspberrypi-202502162204-mmcblk0.direct of=/dev/sdb1 status=progress 
    ```  
    ### note : don't forget to change sdb1 with your sd card block 
    to get it use this command :
    ```bash
    lsblk
    ```

2. Insert the SD card into the Raspberry Pi and power it on and now You are ready to run your image over raspberry pi 5.
