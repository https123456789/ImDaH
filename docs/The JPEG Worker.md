# JPEG Worker

The JPEG Worker can be found in the *Libraries/Python/jpeg.py* file.

## Basic Usage

```
import sys
# Add the library folder to pypath.
sys.path.append("../../Libraries/Python/")
# Impot library
import jpeg

# Create worker and add filename
jpegWorker = jpeg.JPEG("image1.jpeg")

# Write message
message = input("Message:")
jpegWorker.encode(message)

# Read the message
print("You wrote:")
print(jpegWorker.decode())

# Strip all messages from file
jpegWorker.strip()
print("Messages were stripped, file now reads:")
print(jpegWorker.decode())
```

This script uses all three of the core functions of the jpeg library: encode, decode, strip.

## The encode Function

The encode function is called with `jpegWorker.encode(message)` where jpegWorker is a `jpeg.JPEG` object, and `message` is a string. The function returns no value.

### Note:

The function only appends messages to a file.

## The decode Function

The decode function is called with `jpegWorker.decode()` where jpegWorker is a `jpeg.JPEG` object. The function returns all of the messages stored in the image.

## The strip Function

The strip function is called with `jpegWorker.strip()` where jpegWorker is a `jpeg.JPEG` object. The function has no return value.