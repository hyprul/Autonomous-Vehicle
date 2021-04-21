# Heading level 1 Autonomous Vehicle Behavioral Cloning with Uadcity Simulator

I've decided to use the Udacity Self Driving Car Simulator to simulate the training of an autonomous car and enable autonomous driving. The Udacity Simulator is linked below.

https://github.com/udacity/self-driving-car-sim
(Using the V1 Stable Version)

In summary, I used the simulator to generate training data for the model by driving the car through the training track; dataset is collected by me and available publicly at my GitHub.

https://github.com/hyprul/track_data

The dataset and images are preprocessed, augmented, and trained to generate a model for the simulator to use.

The specific processing and algorithms code are posted on Google Colaboratory. THIS IS THE MAIN BULK OF THE CODE.

https://colab.research.google.com/drive/1r54CQORXMXpnqPjVOcR5OMARYLS0n65U#scrollTo=h7PDtL1kU1sI


The dataset is then inputted to the NVIDIA convolutional neural network to learn the behavior from the manual driving. The main learning variable is the steering angle of the car at any given instance. The model will learn to adjust the steering angle based on the given situation. After training the model, I will evaluate its performance by running the simulator autonomously on both the same and a different track. The car will be able to perform well and drive on its own depending on the robustness of the generated model.

After running all the cells and training the model(takes around 2 hours), and outputs 'model.h5' file. Then Flask and Socket.io to generate webserver gateway, actualize telemetry, and send commands to the simulator in real time.

Applicable to real life driving, cars are typically driven around and trained on real roads by manual drivers, then the data is used to train and clone the behavior. 


#H1 Libraries and Frameworks Used
Anaconda
Keras/Tensorflow
Flask, Socket.io
OpenCV


#H1 How to Compile and Run Program
First make sure the Udacity Simulator is installed.
The main files in use for this program are the "drive.py" and "model.h5" files. The algorithms to generate the 'model.h5' file is posted on Google Colaboratory as noted above. 

In terminal, please create and activate Anaconda environment and install the following:
*auto can be any name that you choose*

	conda create --name auto
	conda activate auto
	conda install -c anaconda flask
	conda install -c conda-forge python-socketio
	conda install -c conda-forge eventlet

	conda install -c conda-forge tensorflow
	conda install -c conda-forge keras
	conda install -c anaconda pillow
	conda install -c anaconda numpy
	conda install -c conda-forge opencv

*in case of continuous socket 404 error, downgrade python-engineio using the following command*
	conda install -c conda-forge python-engineio=2.2.0

To setup the telemetry server, in terminal
	python driver.py

Then open up the simulator(recommended resolution 800x600, fastest graphics quality), Autononous Mode with the selected track!






# Autonomous-Vehicle
