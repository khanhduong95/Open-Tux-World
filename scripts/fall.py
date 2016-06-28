from bge import logic
from mathutils import Vector

def gravity(cont):
    own = cont.owner
    v = own["v_z"]
    if v >= 0:
        v = 0
    if v >= -100:
        v -= 0.5
    own.applyForce([0,0,50*v], False)
    own["v_z"] = v

def main(cont):
    own = cont.owner
    own.enableRigidBody()
    v = Vector((own["v_x"],own["v_y"],own["v_z"]))
    dv = Vector(own.worldLinearVelocity) - v
    v += dv
    max_dv = max(dv.x,dv.y,dv.z)
    min_dv = min(dv.x,dv.y,dv.z)
    if max_dv > 40:
        if max_dv > 60:
            own["health"] -= max_dv * 0.1
        else:
            own["health"] -= max_dv * 0.05
        print(own)
        print(own["health"])

    elif min_dv < -40:
        if min_dv < -60:
            own["health"] -= -min_dv * 0.1
        else:
            own["health"] -= -min_dv * 0.05
        print(own)
        print(own["health"])

    own["v_x"] = v.x
    own["v_y"] = v.y
    own["v_z"] = v.z

    if own["health"] <= 0:
        own["death"] = True
        own.state = logic.KX_STATE4
    elif max_dv < 1 and min_dv > -1 and (cont.sensors["Collision.001"].positive or not own["FALL"]):
        own.disableRigidBody()
        own.worldOrientation[2] = [0.0,0.0,1.0]
        own.state = logic.KX_STATE2
