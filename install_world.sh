BASEDIR=$(dirname $0)
WORLDDIR=${BASEDIR}/worlds/${1}
BUILDDIR=${WORLDDIR}/build
for file in ${WORLDDIR}/*_src.blend
do
    ${2:-blender} -b "$file" -P ${BASEDIR}/separate_terrain_files.py &
done
wait
counter=0
for file in ${BUILDDIR}/*.blend
do
    counter=$(expr $counter + 1)
    if [ $(expr $counter % 8) -eq 0 ]
    then
	wait
    else
	${2:-blender} -b "$file" -P ${BASEDIR}/cut_terrain.py &	
    fi
done
wait
