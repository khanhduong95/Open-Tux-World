BASEDIR=$(dirname $0)
WORLDDIR=${BASEDIR}/${1}
TMPDIR=${WORLDDIR}/tmp
for file in ${WORLDDIR}/*_src.blend
do
    ${2:-blender} -b "$file" -P ${BASEDIR}/separate_terrain_files.py &
done
wait
for file in ${TMPDIR}/*.blend
do
    ${2:-blender} -b "$file" -P ${BASEDIR}/cut_terrain.py &
done
wait
rm -rf ${TMPDIR}
