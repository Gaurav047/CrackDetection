# -*- coding: utf-8 -*-
"""crackDetection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/111kgMt3SqEDRXg7P_neKFXjlDBxuk-Ln
"""

!wget https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DL0321EN/data/images/concrete_crack_images_for_classification.zip -P /resources/data

!unzip -q  /resources/data/concrete_crack_images_for_classification.zip -d  /resources/data

"""### Imports and Auxilliary Functions"""

from PIL import Image
from matplotlib.pyplot import imshow
import pandas
import matplotlib.pylab as plt
import os
import glob

"""### We will use the following function to plot in the lab"""

def show_data(data_sample, shape = (28, 28)):
    plt.imshow(data_sample[0].numpy().reshape(shape), cmap='gray')
    plt.title('y = ' + data_sample[1])

"""# **Examine** **Files**"""

directory="/resources/data"
negative='Negative'
negative_file_path=os.path.join(directory,negative)
negative_file_path

"""### Checking the negative data"""

os.listdir(negative_file_path)[0:3]

"""##### We need the full path of the image so we join them as above. Here are a few samples  three samples:"""

[os.path.join(negative_file_path,file) for file in  os.listdir(negative_file_path)][0:3]

"""In some cases, we may have files of a different type, so we have to ensure it's of type <b>jpg</b>. We have to check the extension using the method <code> endswith()</code>. The method  <code>endswith()</code> returns True if the string ends with the specified suffix, otherwise, it will return False. Let's do a quick example:"""

print("test.jpg".endswith(".jpg"))
print("test.mpg".endswith(".jpg"))

"""We now have all the tools to create a list with the path to each image file.  We use a List Comprehensions  to make the code more compact. We assign it to the variable <code>negative_files<code> , sort it in and display the first three elements:"""

negative_files=[os.path.join(negative_file_path,file) for file in  os.listdir(negative_file_path) if file.endswith(".jpg")]
negative_files.sort()
negative_files[0:3]

"""### Repeat the above steps with positive"""

positive="Positive"
positive_file_path=os.path.join(directory,positive)
positive_file_path

"""Check Positive Data"""

os.listdir(positive_file_path)[0:3]

[os.path.join(positive_file_path,file) for file in  os.listdir(positive_file_path)][0:3]

"""We now have all the tools to create a list with the path to each image file. We use a List Comprehensions to make the code more compact. We assign it to the variable positive_files , sort it in and display the first three elements:"""

positive_files=[os.path.join(positive_file_path,file) for file in  os.listdir(positive_file_path) if file.endswith(".jpg")]
positive_files.sort()
positive_files[0:3]

"""<h2 id="Display">Display and Analyze Image With No Cracks</h2>

We can open an image by using the <code>Image</code> Module in the  <b>PIL</b> library, using the function open. We only require the image path; the input is the path of the image. For example we can load the first image as follows:
"""

image1 = Image.open(negative_files[0])
# you can view the image directly 
#image

"""Let's plot the image"""

plt.imshow(image1)
plt.title("1st Image With No Cracks")
plt.show()

"""Let's plot the second image"""

image2 = Image.open(negative_files[1])
plt.imshow(image2)
plt.title("2nd Image With No Cracks")
plt.show()