import sys
sys.path.append("../../Libraries/Python")
import jpeg

# Create a jpeg worker
jpegWorker = jpeg.JPEG("image1.jpeg")

# Get the message and write to image
message = input("Message:")
jpegWorker.encode(message)

# Read the message
print(jpegWorker.decode())

# Strip the image of messages
jpegWorker.strip()