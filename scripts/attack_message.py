def main(cont):
    col = cont.sensors["Collision"]
    if col.positive:
        col.hitObject["normal"] = False
        col.hitObject["attacker_ID"] = cont.owner["owner_ID"]
