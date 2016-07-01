def shoot(cont):
    own = cont.owner
    col = cont.sensors["Collision"]
    col_1 = cont.sensors["Collision.001"]
    if col.positive and id(col.hitObject) != cont.owner["owner_ID"]:
        col.hitObject["normal"] = False
        col.hitObject["attacker_ID"] = cont.owner["owner_ID"]
    if col_1.positive:
        own.setLinearVelocity([-0.00000012,0,0], True)
        own.mass *= 80000
        own.applyForce([-2000000,0,0], True)
        own.endObject()

def hit(cont):
    col = cont.sensors["Collision"]
    if col.positive:
        if id(col.hitObject) != cont.owner["owner_ID"]:
            col.hitObject["normal"] = False
            col.hitObject["attacker_ID"] = cont.owner["owner_ID"]
