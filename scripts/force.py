from bge import logic
import math
from mathutils import Vector

def main(cont):
    own = cont.owner
    v = Vector((own["v_x"],own["v_y"],own["v_z"]))
    dv = Vector(own.worldLinearVelocity) - v
    v += dv
    max_dv = max(dv.x,dv.y,dv.z)
    min_dv = min(dv.x,dv.y,dv.z)
    if max_dv > 30:
        own["health"] -= max_dv*0.05
        print(own)
        print(own["health"])
        own.state = logic.KX_STATE3

    elif min_dv <-30:
        own["health"] -= -min_dv*0.05
        print(own)
        print(own["health"])
        own.state = logic.KX_STATE3

    own["v_x"] = v.x
    own["v_y"] = v.y
    own["v_z"] = v.z

    if own["health"] <= 0:
        own["death"] = True
        own.state = logic.KX_STATE4
