# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 09:51:39 2020

@author: DK
"""


import pickle
import numpy as np

import games.arkanoid.communication as comm
from games.arkanoid.communication import ( SceneInfo, GameInstruction, GameStatus, PlatformAction)

def ml_loop():    
    filename="F:/Documents/MachineLearning/EX/Arkanoid-master/knn.sav"
    # filename="F:/Documents/MachineLearning/MLGame-master/knn_test_2.sav"
    model=pickle.load(open(filename, 'rb'))
    comm.ml_ready()
    ball_postition_history=[]    
    while True:        
       
        scene_info = comm.get_scene_info()                
        ball_postition_history.append(scene_info.ball)
        
        if(len(ball_postition_history) > 1):
            vx=ball_postition_history[-1][0]-ball_postition_history[-2][0]
            vy=ball_postition_history[-1][1]-ball_postition_history[-2][1]
        
            temp=np.array([scene_info.ball[0],scene_info.ball[1],scene_info.platform[0],vx,vy])
            Result=temp[np.newaxis, :]        
       
        if scene_info.status == GameStatus.GAME_OVER:           
            print( "Lose" ,end='\n')            
            comm.ml_ready()
            continue
        elif scene_info.status == GameStatus.GAME_PASS:
            print( "Win" ,end='\n')            
            comm.ml_ready()
            continue
        
        if(len(ball_postition_history) > 1):
            Prediction=model.predict(Result)
        else:
            Prediction = 0        
        if Prediction<0:
            comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)            
        elif Prediction>0:
            comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
        else:
            comm.send_instruction(scene_info.frame, PlatformAction.NONE)
        
