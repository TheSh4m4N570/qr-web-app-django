
# Qr Web App

I had the idea to start this project, when we received an e-mail at work asking us to create QR code from a list of urls. I then decided to first play with some python modules to see how things are done. I first created a simple class that reads a json file containing urls and then loop through them to generate qrcode with the help of 
qr-code and pillow package. I then integrated django to make a web app. Project is still ongoing I'll be adding alot of features.





## TODO
* Add image type choice in the form ('png', 'eps', 'jpeg')
* Add custom and predefined image size
* Add custom colors
* Add the possibilty to upload a logo
* Create a user profile where he can keep track of the QrCodes created
