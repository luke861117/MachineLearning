"""
The template of the script for the machine learning process in game pingpong
"""
import math
import pickle
import numpy as np

class MLPlay:
    def __init__(self, side):        
        self.ball_served = False
        self.side = side
        filename1 = "F:\\Documents\\MachineLearning\\MLGame-master\\games\\pingpong\\ml\\my_tree_1P_new.sav"
        self.model = pickle.load(open(filename1,'rb'))
        self.cmd_1P =  "NONE"         
        self.ball_location = [0,0]      
    def update(self,scene_info): 
        self.side == "1P"
        # ball_location = [0,0]
        if scene_info["status"] != "GAME_ALIVE":
            return "RESET"

        if not self.ball_served:
            self.ball_served = True
            return "SERVE_TO_LEFT"
    
    
    # 3. Start an endless loop
        if self.side == "1P":
            while True:
                last_ball_location = self.ball_location
            
                self.ball_location = scene_info["ball"]                
                if scene_info["status"] == "GAME_1P_WIN" or \
                    scene_info["status"] == "GAME_2P_WIN":
                # Some updating or reseting code here
                    
                    continue
                if(int(last_ball_location[1]) - int(self.ball_location[1]) < 0):
                    # go to down
                    if(int(last_ball_location[0]) - int(self.ball_location[0]) < 0):
                           #go RD
                        LRUP = 2
                    else:
                        LRUP = 1
                            #go LD
                else:
                    #upping
                    if(int(last_ball_location[0]) - int(self.ball_location[0]) < 0):
                           #go RU
                        LRUP = 4
                    else:
                        LRUP = 3
                            #go LU
                
                
                inp_temp = [scene_info["ball"][0],scene_info["ball"][1],LRUP, \
                                 (200 - int(scene_info["ball"][0]))]

                move = str(self.model.classify_test(inp_temp))
                
                try:
                    ans = move[1:3]
                    ans = int(ans) *10
                except:
                    ans = move[1:2]
                    ans = int(ans) *10
                
                if(scene_info["platform_1P"][0] +20 > ans):
                    self.cmd_1P = "MOVE_LEFT"
                    return self.cmd_1P
                elif(scene_info["platform_1P"][0] +20 < ans):
                    self.cmd_1P = "MOVE_RIGHT"
                    return self.cmd_1P
                else:
                    self.cmd_1P = "NONE"
                    return self.cmd_1P
        
    def reset(self):
        """
        Reset the status
        """
        self.ball_served = False
