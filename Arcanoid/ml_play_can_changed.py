import games.arkanoid.communication as comm
from games.arkanoid.communication import ( \
    SceneInfo, GameInstruction, GameStatus, PlatformAction
)
def ml_loop():   
    comm.ml_ready()   
    while True:        
        scene_info = comm.get_scene_info()
        platform_center = scene_info.platform[0]+20
        ball_center = scene_info.ball[0]+2.5
        ball_Y = scene_info.ball[1]
        BIG_Y = 300#球會彈兩次的界線
        if scene_info.status == GameStatus.GAME_OVER or \
            scene_info.status == GameStatus.GAME_PASS:
            comm.ml_ready()
            continue
        
        if ball_Y<= BIG_Y:
            if ball_center > 100:
                if platform_center < 20	:
                    comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
                elif platform_center > 20	:
                    comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
            elif ball_center < 100: 
                if platform_center < 180	:
                    comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
                elif platform_center > 180	:
                    comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
        elif ball_Y>= BIG_Y:
            if platform_center < ball_center:
                comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
            elif platform_center > ball_center:
                comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
