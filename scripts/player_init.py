from bge import logic

def main(cont):
    own = cont.owner
    try:
        ID = logic.globalDict['ID'] = logic.globalDict['ID'] + 1

    except:
        ID = logic.globalDict['ID'] = 0

    own['ID'] = ID
    own['stamina'] = own['max_stamina']

    scene = logic.getCurrentScene()
    scene.active_camera = own.children["camera_track"].children["camera_track2"].children["cam_dir2"].children["cam_dir"].children["cam_holder"].children["Camera"]
    own.state = logic.KX_STATE2