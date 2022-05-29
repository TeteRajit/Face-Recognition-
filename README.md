# Face-Recognition
## Overview
You must have seen a facial recognition login system in apps or websites. Here, I have built a very easy-to-adapt login system from scratch that you can integrate into any app or system for login aspects.This is a web based facial log in website which uses Facial recognition for user authentication.It uses flask server for running the Convolutional Neural Network. It helps in 1-to-1 face verificationfor checking of the person who is logging in, is really that person or not for authentication of that person and security purposes, it also comes with liveness detection mechanism to check whether the person detected on the camera is a REAL person or FAKE(eg. image, video, etc. of that person) and after logging in i have provided the user with a simple webpage of Voting Management System through which the user can enter his/her details and vote for his/her respective political party.

### Sample Screenshots
<img width="684" alt="image" src="https://user-images.githubusercontent.com/93934156/170876189-fc41450e-0a87-4bcd-913b-5b0064fac621.png">
<img width="684" alt="image" src="https://user-images.githubusercontent.com/93934156/170876367-89f265a1-b287-4ba8-8889-733163af4f57.png">

## Requirements
cmake==3.21.1

numpy==1.21.4

dlib==19.22.99

imutils==0.5.4

opencv-contrib-python==4.5.3.56

tensorflow==2.5.0

scikit-learn==0.24.2

face-recognition==1.3.0

Flask==2.0.1

Flask-SQLAlchemy==2.5.1

SQLAlchemy==1.4.22



## Full Workflow
1.	Create a folder for a sinlge person and name after the person's name in face_recognition/dataset .
2.	Collect the images showing full face (1 face per 1 image per 1 person). Since we are using 1 shot learning technique, collect only up to 10 images for each person would be enough.
3.	Run `encode_faces`.
4.	Now you should get encoded faces file ending with .pickle in the path that you specified.
5.	Run `recognize_faces.py` .
6.	Collect video of yourself/others in many light condition (the easiest way to do this is to film yourself/others walking around your/others home) and save to face_liveness_dection/videos folder. The length of the video depends on you. You can name the video as per your liking.
7.	Use those recorded videos and play it on your phone. Then, hold your phone and face the phone screen (running those recorded videos) to the webcam and record your PC/laptop screen or you can just record your video from some other device and use that video. By doing this, you are creating the dataset of someone spoofing the person in the video / pretending to be the person in the video. Try to make sure this new spoofing video has the same length (or nearly) as the original one because we need to avoid unbalanced dataset. 
8.	Run `collect_dataset.py` . Make sure you save the output into the right folder (should be in `dataset` folder and in the right label folder `fake` or `real`). 
9.	Run `train_model.py` . Now, we should have .model, label encoder file ending with .pickle, and image in the output folder you specify. On running the code, you should see liveness.model, label_encoder.pickle, and plot.png in this exact folder (like in this repo).
10.	Run liveness_app.py . If the model always misclassify, go back and see whether you save output images (real/fake) in the right folder. If you are sure that you save everything in the right place, collect more data or better quality data. This is the common iterative process of training model.
11.	Run `face_recognition_liveness_app.py` . The window should show up for a while with bounding box having your name on top and whether real or fake with probability. If your code work properly, this window will be closed automatically after the model can detect you and you are real for 10 consequence frames. By specifying this 10 consequence frames, it can make sure that the person on the screen is really that person who is logging in and real, not just by accident that the model misclassifies for some frames. It also allows some room for model to misclassify. You can adjust this number in line 176 'sequence_count' variable in the code, if you want it to be longer or shorter. And right after the window closes, we should see your name and label (real) on the command line/terminal.
12.	In `app.py`, in the main folder of this project, go down to line 56 and so on. Uncomment those lines and change the parameters in Users object to your username, password, and name. If you want more column go to line 13 and add more in there. IMPORTANT NOTE: The name you save here in name column in this database MUST MATCH the name that you train your face recognition model in steps above (put in simple, must match the folder name inside face_recognition/dataset) unless the login mechanism is not going to work.
13.	Run `app.py` and go to the port that it's displaying on your command line/terminal. Test everything there, the login mechanism, face recognition, and face liveness detection. It must work fine by now. 
14.	After logging in and face verification you will be directed to a voting window where you have to enter your details and you can easily vote for your respective political party.
15.	Congratulations! You've done everything :D


## Login Credentials
Username=rajit_tete

Password=123456789

### Sample Outputs
![image](https://user-images.githubusercontent.com/93934156/170876405-44f3d51e-70aa-41f2-b195-a64f11441754.png)
![image](https://user-images.githubusercontent.com/93934156/170876412-218f8b2d-4a48-4666-bcea-ca2c8f358008.png)


## Drawback
This project is not an end-to-end solution because it doesn't work in a client-server manner (no use of WebRTC) which means that end users need to have python and all libraries installed (absolutely not practical in a real-world solution). The project meant to work as a starting point or to provide the idea of how all components work together.

## Reference
https://youtu.be/PmZ29Vta7Vc

https://www.youtube.com/watch?v=sz25xxF_AVE&t=17

https://www.youtube.com/watch?v=D5xqcGk6LEc
