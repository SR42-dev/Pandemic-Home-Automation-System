# Pandemic-Home-Automation-System
PESU I/O Robotics course project material

Source code word file (source_code.docx) -

	Arduino code - page 1
	Python dataset code - page 9
	Main python script - page 11

Pitch_slideshow - Our presentation slideshow 

Demo 1 - System test with successful login + demo of all features

Demo 2 - System test with failed login

main (Main project folder with all required files after testing. Do not delete anything from here) - 

	slave sketch - contains arduino code. 2 gestures used to traverse options and select, each detected by one ultrasonic sensor
	Sriram - <my name>, used it to store pictures of myself so dataset.py could learn my facial features and encode them
	dataset.py - encodes facial features into a file
 	face_enc - encoded file
	<all .mp3 files> - used for voices and music heard in the demo, called by main.py
	main.py - main python script that defines UI, communicates with arduino and calls necessary functions, uses face_enc to verify identity






