#Project by SASANK
#Libraries
import os
import cv2
import hashlib


# Convert text to binary.
def text_to_binary(text):
    binary = ''.join(format(ord(char), '08b') for char in text)
    return binary

# Convert binary to text.
def binary_to_text(binary):
    text = ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))
    return text

# To Encrypt or decrypt the text using SHA-256 & XOR with the given key.
def xor_encrypt_decrypt(text, key):
    key = hashlib.sha256(key.encode()).digest()  # Using SHA-256 to generate a key
    encrypted = ''.join(chr(ord(char) ^ key[i % len(key)]) for i, char in enumerate(text))
    return encrypted


# To Check if the text can fit in the image.
def can_hide_text(image_path, text):
    # Read the image
    image = cv2.imread(image_path)
    # Calculates the number of bits available
    total_bits = image.shape[0] * image.shape[1] * 3
    print("\nTotal no. of bits can be hide in the Image : "+ str(total_bits))
    # Calculate the length of the binary text including the delimiter
    binary_text_length = len(text_to_binary(text)) + 16
    print("No. of bits of the secret message : "+ str(binary_text_length))
    return binary_text_length <= total_bits


# Hide text inside an image with authentication.
def hide_text_in_image(image_path, text, passcode, output_path):

    if not can_hide_text(image_path, text):
        print("The text is too long to hide in this image.Try with another image .")
        return
    
    # Encrypt the text with the passcode
    encrypted_text = xor_encrypt_decrypt(text, passcode)
    # Convert the encrypted text to binary
    binary_text = text_to_binary(encrypted_text) + '1111111111111110'  # Add a delimiter at the end
    binary_index = 0

    # Read the image
    image = cv2.imread(image_path)

    for row in image:
        for pixel in row:
            for channel in range(3):  # Loop through the RGB channels
                if binary_index < len(binary_text):
                    # Replace the LSB of the pixel with the next binary digit of the text
                    pixel[channel] = int(format(pixel[channel], '08b')[:-1] + binary_text[binary_index], 2)
                    binary_index += 1

    # Saves the modified image
    cv2.imwrite(output_path, image)
    print("Text is successfully hidden in image.")

    # Opens the modified image
    os.startfile(output_path)

# Extract hidden text from an image with authentication.
def extract_text_from_image(image_path, passcode):
    # Read the image
    image = cv2.imread(image_path)
    binary_text = ""
    
    for row in image:
        for pixel in row:
            for channel in range(3):  # Loop through the RGB channels
                # Extract the LSB of the pixel and add it to the binary text
                binary_text += format(pixel[channel], '08b')[-1]

    # Split the binary text by the delimiter and convert to text
    binary_text = binary_text.split('1111111111111110')[0]
    encrypted_text = binary_to_text(binary_text)
    
    # Decrypt the text with the passcode
    decrypted_text = xor_encrypt_decrypt(encrypted_text, passcode)
    return decrypted_text



# Main ... Goes Here

print("Greetings Mr.User .")
i=2
while(i>1):
    print("\n --MENU-- ")
    print("1.Hide text in Image .")
    print("2.Extraxt the text from Image .")
    print("3.Exit .")
    n=int(input("Enter your Choice : "))

    if(n==1):
        input_image_path = input("Enter the input path of the Image: ")
        output_image_path = input("Enter the output path of the Image (To save): ")
        text_to_hide = input("Enter your secret message to hide : ")
        passcode = input("Enter your Security Passcode : ")

        # To Hide the text in the image
        hide_text_in_image(input_image_path, text_to_hide, passcode, output_image_path)
        k=int(input("Enter 0 , to decrypt the message : "))
        if(k==0):
            entered_passcode = input("Enter the passcode: ")
            # To Extract the text from the image
            extracted_text = extract_text_from_image(output_image_path, entered_passcode)
            print("Extracted Text:", extracted_text)

    elif(n==2):
        output_image_path = input("Enter the output path of the Image : \n")
        entered_passcode = input("Enter the passcode: ")
        # To Extract the text from the image
        extracted_text = extract_text_from_image(output_image_path, entered_passcode)
        print("Extracted Text:", extracted_text)
    else:
        print("Thank You!")
        exit()



# THE END <3
