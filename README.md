# Disaster Relief Inventory Counter

Where ever disaster strikes, be it in a third world country or even right here in the United States, resources that come in from relief groups are often scarce. This puts an even stronger emphasis on proper logistics and inventorty tracking, especially with disaster-relief items of importance (such as medicine or food supplies). In events like these, you often will find yourself in a low-bandwith environment, which brings with it a number of organizational issues.

Using a well-trained machine vision model on our Raspberry Pi 3, our aim is to provide a low-power, portable tool that allows for real-time inventory tracking in disaster struck areas. We imagine it set up in pop-up hospitals or shelters, where the low-power camera can be placed in inventory and the user can have real-time inventory tracking instantly, but there are many other potential applications for easy inventory tracking in low bandwith environments. Whether it's for fraud prevention, or to have a live feed of when there are changes in your stock, the tool utilizes visual recognition to make sure these scarce resources are being distributed properly and not getting lost among the many other things going on.

## Example Input:
![Screenshot](readimg1.jpg)

## Example Output:
![Screenshot](readimg2.jpg)

## Training Instructions

For best results, your foundation / relief group should collect 50+ unique images of your inventory/storage and label them accordingly. This framework uses the IBM Watson Visual Recognition portal to streamline the training process. As with everything in machine vision: the more data, the better.

On the hardware side, the Raspberry Pi setup is a relatively quick and low power consuming image processing center for where ever you set up your storage.
