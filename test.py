import rospy
import baxter_interface
from baxter_interface import Gripper, Limb, Head
import time

rospy.init_node('test')

left = Limb('left')
right = Limb('right')
leftg = Gripper('left')
head = Head()

def dab():
	right.move_to_neutral()
	left.move_to_neutral()

	dableft = {'left_w0': -0.10316020798529407, 'left_w1': 0.0790000105760988, 'left_w2': -0.0011504855909140602, 
	'left_e0': -0.006519418348513008, 'left_e1': -0.039883500485020755, 
	'left_s0': 0.29682528245582757, 'left_s1': -0.6181942575178218}

	dabright = {'right_s0': 0.6810874698211237, 'right_s1': -0.4935583185021319, 
	'right_w0': -0.008820389530341128, 'right_w1': 0.3321068405771921, 'right_w2': 0.0038349519697135344, 
	'right_e0': 1.749121593386343, 'right_e1': 1.6333060439009943}


	left.move_to_joint_positions(dableft, timeout = 2)
	head.set_pan(-0.8, speed=.5)
	right.move_to_joint_positions(dabright, timeout = 6)
	head.command_nod()
	time.sleep(1)

	right.move_to_neutral()
	left.move_to_neutral()

def pickUp3Point2():
	above3point2 = {'left_w0': 0.0, 'left_w1': 1.3157720208087136, 'left_w2': -0.002684466378799474, 
					'left_e0': 0, 'left_e1': 0.7850146682003605, 
					'left_s0': -0.73, 'left_s1': -0.6293156182299909}
	down3point2 = { 'left_w0': 0.13077186216723152, 'left_w1': 1.1, 'left_w2': 0.0015339807878854137, 
					'left_e0': -0.16605342028859604, 'left_e1': 0.7,
					'left_s0': -0.62, 'left_s1': -0.28}	
	Gripper.calibrate(leftg)
	leftg.open()
	time.sleep(1)

	left.move_to_joint_positions(above3point2, timeout = 4)
	left.move_to_joint_positions(down3point2, timeout = 4)

	leftg.open()
	leftg.close()
	time.sleep(1)
	left.move_to_joint_positions(above3point2)
	leftg.open()

head.set_pan(0, speed=100)
pickUp3Point2()
dab()
