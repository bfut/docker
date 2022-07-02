#!/bin/sh

# 1) -v mounts current working directory to container
# 2) -w sets working directory
# -a) execute bash script (must run chmod +x locally!)
# -b) run python script (mind conda environment)
INPUTDIR=$PWD
LOCALDIR=~/../"demo"

mkdir $INPUTDIR/.out

# Copy contents to container
cp -R $PWD $LOCALDIR
cd $LOCALDIR
echo $PWD

# Create example FMU
cd /pythonfmu/examples
conda run -n conda-fmi pythonfmu build -f ./demoslave.py --no-external-tool
ls -lg

# Run test
cd $LOCALDIR
conda run -n conda-fmi pytest --disable-warnings --ignore=/pythonfmu/pythonfmu/tests -vvs
#conda run -n conda-fmi pytest --ignore=/pythonfmu/pythonfmu/tests -vvs
ls -lg
cat logfile

cp $LOCALDIR/logfile $INPUTDIR/.out/logfile

cd $INPUTDIR
ls -lg
cd .out
ls -lg
