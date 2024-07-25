# Hide-text-in-image-Steganography
##NOTE: To decrypt the Modified_secret.png .  -> PASSCODE : passcode

What is Steganography ?
Steganography is the practice of concealing a secret message within another non-secret medium, such as an image, audio file, or text document. Unlike cryptography, which makes data unreadable to unauthorized users, steganography hides the existence of the data itself. This technique can be used for secure communication, where the hidden message remains invisible to unintended recipients while being easily retrievable by those who know the method to uncover it.
-> Here in this projectwe will see "Hiding text inside an image using Least Significant Bit (LSBs) Technique of Steganography .

-> You can see an Example attached in the repository .


#### Requirements

- Python 3.x
- OpenCV library (`cv2`)
- hashlib library (included with Python)

#### Installation

Before running the script, ensure you have the required libraries installed. You can install OpenCV using pip:

```sh
pip install opencv-python
```

#### User Manual (How to use )

1. **Run the Script**

   Execute the script in your Python environment. You will see the following greeting and menu options:

   ```
   Greetings Mr. User.
   *MENU*
   1. Hide text in Image
   2. Extract the text from Image
   3. Exit
   ```

2. **Hide Text in Image**

   - Select option `1` to hide text in an image.
   - You will be prompted to enter the input image path, output image path, the secret message to hide, and a security passcode.

   ```sh
   Enter the input path of the Image:
   Enter the output path of the Image (To save):
   Enter your secret message to hide:
   Enter your Security Passcode:
   ```

   - The script will then encrypt the message using the provided passcode, hide the encrypted message in the image, and save the modified image to the specified output path.
   - You will be prompted to enter `0` to decrypt and verify the hidden message.

   ```sh
   Enter 0, to decrypt the message:
   Enter the passcode:
   Extracted Text: [Your Secret Message]
   ```

3. **Extract Text from Image**

   - Select option `2` to extract hidden text from an image.
   - You will be prompted to enter the output image path and the passcode used to hide the text.

   ```sh
   Enter the output path of the Image:
   Enter the passcode:
   Extracted Text: [Your Secret Message]
   ```

4. **Exit**

   - Select option `3` to exit the program.

   ```sh
   Thank You!
   ```

#### Functions

- **text_to_binary(text)**: Converts text to binary representation.
- **binary_to_text(binary)**: Converts binary data to text.
- **xor_encrypt_decrypt(text, key)**: Encrypts or decrypts text using XOR with a key hashed by SHA-256.
- **can_hide_text(image_path, text)**: Checks if the text can be hidden in the image.
- **hide_text_in_image(image_path, text, passcode, output_path)**: Hides the text in the image and saves it.
- **extract_text_from_image(image_path, passcode)**: Extracts the hidden text from the image using the passcode.

#### Example

1. **Hiding Text**

   ```
   Enter your Choice: 1
   Enter the input path of the Image: D:\MSS\Internship project\sunrise2.0.jpg
   Enter the output path of the Image (To save): D:\MSS\Internship project\enc_sunrise2.0.jpg
   Enter your secret message to hide: Hello World
   Enter your Security Passcode: mypasscode
   Enter 0, to decrypt the message: 0
   Enter the passcode: mypasscode
   Extracted Text: Hello World
   ```

2. **Extracting Text**

   ```
   Enter your Choice: 2
   Enter the output path of the Image: D:\MSS\Internship project\enc_sunrise2.0.jpg
   Enter the passcode: mypasscode
   Extracted Text: Hello World
   ```

## Notes

- Ensure the image has enough capacity to store the message. The script will notify you if the message is too long to fit in the image.
- The security passcode is critical for both encryption and decryption. Use a passcode that you can remember but is hard for others to guess.

