BASEDIR=$(dirname $0)
WORLDDIR=${BASEDIR}/worlds/${1}
BUILDDIR=${WORLDDIR}/build
for file in ${WORLDDIR}/*_src.blend
do
    ${2:-blender} -b "$file" -P ${BASEDIR}/separate_terrain_files.py &
done
wait
for file in ${BUILDDIR}/*.blend
do
    ${2:-blender} -b "$file" -P ${BASEDIR}/cut_terrain.py &
done
wait
