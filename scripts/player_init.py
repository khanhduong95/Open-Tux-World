from bge import logic

def main(cont):
    own = cont.owner
    own['ID'] = id(own)#ID
    own['stamina'] = own['max_stamina']
    own["weapon"] = 2
    own["snow"] = 20
    own["ice"] = 20
    scene = logic.getCurrentScene()
    scene.active_camera = own.children["camera_track"].children["camera_track2"].children["cam_dir2"].children["cam_dir"].children["cam_holder"].children["Camera"]
    own.state = logic.KX_STATE2
