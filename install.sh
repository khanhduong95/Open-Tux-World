BASEDIR=$(dirname $0)
BLENDER_EXE=${1:-blender}
${BLENDER_EXE} -b ${BASEDIR}/terrain_src.blend -P ${BASEDIR}/build_terrain.py &
${BLENDER_EXE} -b ${BASEDIR}/items_src.blend -P ${BASEDIR}/build_item.py
${BLENDER_EXE} -b ${BASEDIR}/penguin_src.blend -P ${BASEDIR}/build_penguin.py
