from crowd_sim.envs.utils.agent import Agent
from crowd_sim.envs.utils.state import JointState
import math
from crowd_sim.envs.policy.policy import Policy
from crowd_sim.envs.utils.action import ActionRot, ActionXY
from crowd_sim.envs.utils.state import ObservableState, FullState
import numpy as np
import math
import os
import sys
import time
import tty, termios
import torch
import torch.nn as nn
import itertools
import logging

class Robot(Agent):
    def __init__(self, config, section):
        super().__init__(config, section)
        self.turn = 0
        self.speed = 0

    def act(self, ob):
        if self.policy is None:
            raise AttributeError('Policy attribute has to be set!')
        state = JointState(self.get_full_state(), ob)
        action = self.policy.predict(state)
        return action
    
    def act_api(self):
        thread_stop = False 
        walk_vel_ = 0.25   
        yaw_rate_ = math.pi / 6

        max_tv = walk_vel_  
        max_rv = yaw_rate_  
        print('Welcome to use our API for your own demonstrations.' )
        print('Please, set the speed and direction for robot.')                
        while not thread_stop: 
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try :
                tty.setraw( fd )
                ch = sys.stdin.read(1)
            finally :
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
                            
            if ch == 'w':  
                max_tv = walk_vel_  
                self.speed += 1  
                
                time.sleep(0.1)
                keyboard_speed = self.speed * max_tv 
                keyboard_angle = self.turn * max_rv
                api_action = {}
                api_action[0] = keyboard_speed * math.cos(keyboard_angle)
                api_action[1] = keyboard_speed * math.sin(keyboard_angle)
                            #env.render('video', args.video_file)
                            #action = ActionXY(*self.sim.getAgentVelocity(0))
                action = ActionXY(api_action[0],api_action[1])
                print(action)

            elif ch == 's':  
                max_tv = walk_vel_  
                self.speed -= 1

                time.sleep(0.1)
                keyboard_speed = self.speed * max_tv 
                keyboard_angle = self.turn * max_rv
                api_action = {}
                api_action[0] = keyboard_speed * math.cos(keyboard_angle)
                api_action[1] = keyboard_speed * math.sin(keyboard_angle)
                            #env.render('video', args.video_file)
                            #action = ActionXY(*self.sim.getAgentVelocity(0))
                action = ActionXY(api_action[0],api_action[1])
                print(action)   
            elif ch == 'a':  
                max_rv = yaw_rate_  
                self.turn += 1

                time.sleep(0.1)
                keyboard_speed = self.speed * max_tv 
                keyboard_angle = self.turn * max_rv
                api_action = {}
                api_action[0] = keyboard_speed * math.cos(keyboard_angle)
                api_action[1] = keyboard_speed * math.sin(keyboard_angle)
                            #env.render('video', args.video_file)
                            #action = ActionXY(*self.sim.getAgentVelocity(0))
                action = ActionXY(api_action[0],api_action[1])
                print(action)  
            elif ch == 'd':  
                max_rv = yaw_rate_  
                self.turn -= 1

                time.sleep(0.1)
                keyboard_speed = self.speed * max_tv 
                keyboard_angle = self.turn * max_rv
                api_action = {}
                api_action[0] = keyboard_speed * math.cos(keyboard_angle)
                api_action[1] = keyboard_speed * math.sin(keyboard_angle)
                            #env.render('video', args.video_file)
                            #action = ActionXY(*self.sim.getAgentVelocity(0))
                action = ActionXY(api_action[0],api_action[1])
                print(action)
            elif ch == 'q':  
                self.turn = 0
                self.speed = 0
                time.sleep(0.1)
                keyboard_speed = self.speed * max_tv 
                keyboard_angle = self.turn * max_rv
                api_action = {}
                api_action[0] = keyboard_speed * math.cos(keyboard_angle)
                api_action[1] = keyboard_speed * math.sin(keyboard_angle)
                            #env.render('video', args.video_file)
                            #action = ActionXY(*self.sim.getAgentVelocity(0))
                action = ActionXY(api_action[0],api_action[1])
                print(action)
            
            elif ch == 'e':
                thread_stop = True
                
                keyboard_speed = self.speed * max_tv 
                keyboard_angle = self.turn * max_rv
                api_action = {}
                api_action[0] = keyboard_speed * math.cos(keyboard_angle)
                api_action[1] = keyboard_speed * math.sin(keyboard_angle)
                            #env.render('video', args.video_file)
                            #action = ActionXY(*self.sim.getAgentVelocity(0))
                action = ActionXY(api_action[0],api_action[1])
                print(action)
                
                return action 
            
            # time.sleep(0.1)
            keyboard_speed = self.speed * max_tv 
            keyboard_angle = self.turn * max_rv
            api_action = {}
            api_action[0] = keyboard_speed * math.cos(keyboard_angle)
            api_action[1] = keyboard_speed * math.sin(keyboard_angle)
                            #env.render('video', args.video_file)
                            #action = ActionXY(*self.sim.getAgentVelocity(0))
            action = ActionXY(api_action[0],api_action[1])

    '''def act_ui(self):
        thread_stop = False 
        walk_vel_ = 0.25   
        yaw_rate_ = math.pi / 6

        max_tv = walk_vel_  
        max_rv = yaw_rate_  
        turn = 0
        speed = 0 
        print('Welcome to use our UI for your own expectation.' )
        print('Please, watch two different trajectories and enter your points.')     
        print('(1,0); (0.5,0.5); or (0,1)')             
        while not thread_stop: 
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try :
                tty.setraw( fd )
                ch = sys.stdin.read(1)
            finally :
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
                            
            if ch == '1':  
                print('(1,0)')
            if ch=='0':
                print('(0,1)')
            else:
                return 0 
            
            time.sleep(0.1)
            keyboard_speed = speed * max_tv 
            keyboard_angle = turn * max_rv
            api_action = {}
            api_action[0] = keyboard_speed * math.cos(keyboard_angle)
            api_action[1] = keyboard_speed * math.sin(keyboard_angle)
                            #env.render('video', args.video_file)
                            #action = ActionXY(*self.sim.getAgentVelocity(0))
            action = ActionXY(api_action[0],api_action[1])'''