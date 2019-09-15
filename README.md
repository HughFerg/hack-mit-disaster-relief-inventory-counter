# Disaster Relief Inventory Counter

Where ever disaster strikes, whether in a third world country or even right here in the United States, resources that come in from relief groups are often scarce, which puts an even stronger emphasis on proper logistics and inventorty tracking. In events like these, you often will find yourself in a low-bandwith environment, which brings with it a number of organizational issues.

Using a well-trained machine vision model on our Raspberry Pi 3, our aim is to provide a low-power, portable tool that allows for inventory tracking in disaster struck areas. Whether it's for fraud prevention, or to have a live feed of when there are changes in your stock, the tool utilizes visual recognition to make sure these scarce resources are being distributed properly and not getting lost among the many other things going on.

## Example Input:
![Screenshot](readimg1.jpg)

## Example Output:
![Screenshot](readimg2.jpg)

## Training Instructions

For best results, your foundation / relief group should collect 50+ unique images of your inventory/storage and label them accordingly. This framework uses the IBM Watson Visual Recognition portal to streamline the training process. As with everything in machine vision: the more data, the better.

On the hardware side, the Raspberry Pi setup is a relatively quick and low power consuming image processing center for where ever you set up your storage.
