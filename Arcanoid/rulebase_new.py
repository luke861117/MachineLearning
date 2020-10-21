# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 17:14:41 2020

@author: DK
"""



class MLPlay:
    def __init__(self):
        """
        Constructor
        """
        self.ball_served = False

    def update(self, scene_info):
        """
        Generate the command according to the received `scene_info`.
        """
        
        platform_center = scene_info["platform"][0]+20
        ball_center = scene_info["ball"][0]+2.5
        ball_Y = scene_info["ball"][1]
        BIG_Y = 325#球會彈兩次的界線
        # Make the caller to invoke `reset()` for the next round.
        if (scene_info["status"] == "GAME_OVER" or
            scene_info["status"] == "GAME_PASS"):
            return "RESET"
        if not self.ball_served:
            self.ball_served = True
        if ball_Y<= BIG_Y:
            if ball_center > 100:
                if platform_center < 20	:
                    command = "MOVE_RIGHT"
                    return command
                    
                elif platform_center > 20	:
                    command = "MOVE_LEFT"
                    return command
                    
            elif ball_center < 100: 
                if platform_center < 180	:
                    command = "MOVE_RIGHT"
                    return command
                    
                elif platform_center > 180	:
                    command = "MOVE_LEFT"
                    return command
                   
        elif ball_Y>= BIG_Y:
            if platform_center < ball_center:
                command = "MOVE_RIGHT"
                return command
                
            elif platform_center > ball_center:
                command = "MOVE_LEFT"
                return command
                

        if not self.ball_served:
            self.ball_served = True
        

    def reset(self):
        """
        Reset the status
        """
        self.ball_served = False
