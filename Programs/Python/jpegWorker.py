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