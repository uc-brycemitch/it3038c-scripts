INSTALLING PILLOW:
First, I made sure that python had an environment variable path on my machine (does not work otherwise). 
Then, I went into the command prompt and typed in the following commands (pip is already installed with new python versions):
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow

My projects allows the user to add text to a photo using the Pillow Plugin. I built this off of the previous plugin lab we used. Rather than adding filters, I focused on the text aspect.
I used the Pillow tutorial located here to build my code: https://www.tutorialspoint.com/python_pillow/python_pillow_quick_guide.htm

To use the code, you must download the code and the "puppy.jpg" photo. 
In some cases, the code can't find the path to the photo. I was able to fix this by opening up the puppy photo before running the code (it is an issue with windows and app data)

The terminal will prompt the user to enter in what text they want, and then will open the photo with the text added. 
