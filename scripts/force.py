import bge, time
from mathutils import Vector

def main(cont):

    own = cont.owner

    t = own["time"]
    v = Vector((own["v_x"],own["v_y"],own["v_z"]))
    m = own.mass

    dt = time.time() - t
    t += dt

    dv = Vector(own.worldLinearVelocity) - v
    v += dv

    f = m * dv / dt
#    print(f)
    
    if f > 1:
        own["health"] -= 1
        print(own)
        print(own["health"])
        
    own["time"] = t
    own["v_x"] = v.x
    own["v_y"] = v.y
    own["v_z"] = v.z
