from bge import logic
from mathutils import Vector

def main(cont):
    own = cont.owner
    v = Vector((own["v_x"],own["v_y"],own["v_z"]))
    dv = Vector(own.worldLinearVelocity) - v
    v += dv

    if dv.x > 50 or dv.x < -50 or dv.y > 50 or dv.y < -50 or dv.z > 50 or dv.z < -50:
        own["health"] -= 1
        print(own)
        print(own["health"])

    own["v_x"] = v.x
    own["v_y"] = v.y
    own["v_z"] = v.z

    if own["health"] <= 0:
        own.state = logic.KX_STATE3
