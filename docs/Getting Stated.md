# Getting Started

To get started, download the libraries from [downloads](<Downloads>) or download the zipped repository.

| Languages |
|-----------|
|[Python](<#Python>)|

## Python

### Hello World!

To follow tradition, our first script will be called HelloWorld.py. As always, the completed script can be found in the *Programs/Python* folder.

This is the image that we are going to use:
*Programs/Python/image1.jpeg*

![image1.jpeg](<https://github.com/https123456789/ImDaH/blob/main/Programs/Python/image1.jpeg>)

First, let's import the jpeg library.

```
import sys
sys.path.append("../../Libraries/Python/")
import jpeg
```

Now, we need to create a jpeg worker.

```
jpegWorker = jpeg.JPEG("image1.jpeg")
```

The JPEG object must be initialized with a filename which can be change at a later date by accessing `jpegWorker.filename`.

Next, we need to collect the message that the user wants to write to the file.

```
message = input("Message")
```

Oh, and we also want to write to the image.

```
jpegWorker.encode(message)
```

The message has now been written to the image in a way that image viewing/editing programs won't display it.

![image1.jpeg](<https://github.com/https123456789/ImDaH/blob/main/Programs/Python/image1.jpeg>)

To read the message, we need to call the decode function.

```
print(jpegWorker.decode())
```

The decode function will return the message which we then print. Finally, we can remove the message from the image with a call to the strip function.

```
jpegWorker.strip()
```

Our image is now exactly as it was at the start of the program.

![image1.jpeg](<https://github.com/https123456789/ImDaH/blob/main/Programs/Python/image1.jpeg>)

The completed program should look like this:
```
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
```

The output to the terminal should be:
```
$ python HelloWorld.py
Message:Hello World!
Hello World!
$ 
```

For more information about the jpeg worker, please see [The JPEG Worker](<The JPEG Worker>).