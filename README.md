# Project Name : Emotion-recognition

Emotion recognition toolkit, forked and enchanced from https://github.com/omar178.

Features:

* It uses face tracking.
* It fork fast event on CPU (without GPU support).
* In my tests it detects "happinness" by smiling, "angry" or "sad" by shrinking nose,
and "surprised" by opening mouth (sometimes).
* Provided example sends OSC messages for using this emotions probabilities  into other applications.
* Very simple installation.


# Table of Content :
1.[Description](#p1)

2.[Installation](#p2)

3.[Usage](#p3)

4.[Dataset](#p4)



![](https://github.com/omar178/Emotion-recognition/blob/master/emotions/Happy.PNG)
![](https://github.com/omar178/Emotion-recognition/blob/master/emotions/angry.PNG)




<a id="p1"></a> 
# Description:

Our Human face is having a mixed emotions so we are to demonstrate the probabilities of these emotions that we have.

## What does Emotion Recognition mean?

Emotion recognition is a technique used in software that allows a program to "read" the emotions on a human face using advanced image processing. Companies have been experimenting with combining sophisticated algorithms with image processing techniques that have emerged in the past ten years to understand more about what an image or a video of a person's face tells us about how he/she is feeling and not just that but also showing the probabilities of mixed emotions a face could has.

<a id="p2"></a> 
# Installation:

Toolkit is tested in Windows 10, Python 3.6.3, 64-bit, but should work in 3.5–3.7 and pip >= 19.0 (because this versions as noted on Tensorflow site).


It uses OpenCV and Keras/TensorFlow.

To install it just call:

* **install_windows.bat** in Windows

* **pip install -r requirements.txt** in non-Windows

(See setup.py for the details)

<a id="p3"></a> 
# Usage:

The program will create a window to display the scene capture by webcamera and a window representing the probabilities of detected emotions.

> Demo

python real_time_video_osc.py

This example does the following:
* captures images from webcamera and draws it in a window, 
* detects face,
* if face is detected, computes probabilities of emotions and draws it in a separate window
* sends OSC messages for probabilities to use this data in your external applications (for control robots, etc.)

Press ESC to exit.

** Note: lighting conditions can be important for accurate detection, so please try to achieve no-shadows capturing
(for example, place some light source in the front of the face).


You can just use this with the provided pretrained model i have included in the path written in the code file, i have choosen this specificaly since it scores the best accuracy, feel free to choose any but in this case you have to run the later file train_emotion_classifier
> If you just want to run this demo, the following content can be skipped
- Train

- python train_emotion_classifier.py


<a id="p4"></a> 
# Dataset:

I have used [this](https://www.kaggle.com/c/3364/download-all) dataset

Download it and put the csv in fer2013/fer2013/

-fer2013 emotion classification test accuracy: 66%


# Credits
This work is inspired from [this](https://github.com/oarriaga/face_classification) great work and the resources of Adrian Rosebrock helped me alot!.

# Ongoing 
Draw emotions faces next to the detected face.

# Issues & Suggestions

If any issues and suggestions to me, you can create an [issue](https://github.com/omar178/Emotion-recognition/issues).

If you like this work please help me by giving me some stars.
