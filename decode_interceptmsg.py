import string
from base64 import b64encode, b64decode

# Function to decode step2
def decodeStep2(s):
    return b64decode(s).decode('utf-8')

# Function to decode using Julius cipher
def decodeStep1(plaintext, shift=-4):
    loweralpha = string.ascii_lowercase
    shifted_string = loweralpha[shift:] + loweralpha[:shift]
    converted = str.maketrans(loweralpha, shifted_string)
    return plaintext.translate(converted)

# List of decoding steps
secret_decoding = ['decodeStep3', 'decodeStep2', 'decodeStep1']

# Read intercepted message from a file
with open('intercepted.txt', 'r') as file:
    interceptedMessage = file.read().strip()  # Read and remove any extra whitespace/newlines

# Loop through decoding steps
while True:
    try:
        counter = int(interceptedMessage[0]) - 1  # Get the step to decode
    except ValueError:
        # If it's not a number, the decoding process is finished
        print("Decoded message:", interceptedMessage)
        break

    # Remove the first character (the step indicator)
    interceptedMessage = interceptedMessage[1:]

    # Perform decoding based on the current step
    if secret_decoding[counter] == 'decodeStep3':
        interceptedMessage = interceptedMessage.translate(
            str.maketrans(
                "mlkjihgfedcbaMLKJIHGFEDCBAzyxwvutsrqponZYXWVUTSRQPON",
                "zyxwvutsrqponZYXWVUTSRQPONmlkjihgfedcbaMLKJIHGFEDCBA"
            )
        )
    elif secret_decoding[counter] == 'decodeStep2':
        interceptedMessage = decodeStep2(interceptedMessage)
    elif secret_decoding[counter] == 'decodeStep1':
        interceptedMessage = decodeStep1(interceptedMessage)
