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
        filename = "F:\\Documents\\MachineLearning\\MLGame-master\\games\\pingpong\\ml\\my_tree_2P_new.sav"
        self.model_2P = pickle.load(open(filename,'rb'))
        self.cmd_2P =  "NONE"
        self.ball_location = [0,0]
    def update(self,scene_info):       

        self.side == "2P"
        
        if scene_info["status"] != "GAME_ALIVE":
            return "RESET"

        if not self.ball_served:
            self.ball_served = True
            return "SERVE_TO_LEFT"
    
    
    # 3. Start an endless loop
        

        if self.side == "2P":  

                
            while True:
                last_ball_location = self.ball_location                
                self.ball_location = scene_info["ball"]
            
                if scene_info["status"] == "GAME_1P_WIN" or \
                    scene_info["status"] == "GAME_2P_WIN":
                # Some updating or reseting code here
                
                    continue
                if(int(last_ball_location[1]) - int(self.ball_location[1]) > 0):
                    # go to up
                    
                    if(int(last_ball_location[0]) - int(self.ball_location[0]) > 0):
                           #go LU
                        LRUP = 1
                    else:
                        LRUP = 2
                            #go RU
                else:
                    #down
                    if(int(last_ball_location[0]) - int(self.ball_location[0]) > 0):
                           #go LD
                        LRUP = 3
                    else:
                        LRUP = 4
                            #go RD       
                
                inp_temp = [scene_info["ball"][0],scene_info["ball"][1],LRUP, \
                                 (200 - int(scene_info["ball"][0]))]
                move = str(self.model_2P.classify_test(inp_temp))
                
                print(move)
                try:
                    ans = move[1:3]
                    
                    ans = int(ans) *10
                except:
                    ans = move[1:2]
                    ans = int(ans) *10
                if(ans<50 and abs(scene_info["ball_speed"][1]) >= 21 ):
                
                    ans += 10
                
                if(scene_info["platform_2P"][0] +20 > ans):

                    self.cmd_2P = "MOVE_LEFT"
                    
                    return self.cmd_2P
                elif(scene_info["platform_2P"][0] +20 < ans):
                    self.cmd_2P = "MOVE_RIGHT"
                    
                    return self.cmd_2P
                else:
                    self.cmd_2P = "NONE"
                    
                    return self.cmd_2P
                    

    def reset(self):
        """
        Reset the status
        """
        self.ball_served = False
