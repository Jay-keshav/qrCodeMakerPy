# QR Code Generator
This Python script allows you to quickly and easily generate QR codes from any URL and save them as image files. You can also preview the generated QR code image directly after saving.

## Features
- Converts any URL into a QR code.
- Saves the QR code as an image with a user-defined name.
- Displays the generated QR code image.

## How to Use
Ensure your PC has the `qrcode` and `Pillow` libraries installed. Then, you can run this script on your PC. After running, simply enter the URL and a name for the QR code when prompted, and you're done!

## Libraries Used
- **qrcode**: This library is used to generate QR codes from the provided input.
- **Pillow (PIL)**: This library is used to handle the image file, including saving and displaying the generated QR code.

## Example
Here is an example interaction with the script:

```text
Enter the url u want to convert in qr code: https://example.com
Enter a name for that qr code image: example_qr
```

The script will generate a QR code for `https://example.com`, save it as `example_qr.png`, and display the QR code image.

## Code Explanation
- **URL Input**: The script takes a URL as input from the user.
- **Name Input**: The user provides a name for the QR code image file.
- **QR Code Generation**: The `qrcode.make()` function generates a QR code from the provided URL.
- **Saving the Image**: The QR code is saved as an image file in PNG format using the `Pillow` library.
- **Displaying the Image**: The `Pillow` library is used to open and display the image.

## Notes
- Ensure the name you provide for the QR code image does not conflict with existing files in the directory.
- The script uses a default scale for the QR code image, which can be adjusted in the `save()` method if needed.

## Acknowledgments
- [qrcode Library Documentation](https://pypi.org/project/qrcode/)
- [Pillow Library Documentation](https://pillow.readthedocs.io/)
