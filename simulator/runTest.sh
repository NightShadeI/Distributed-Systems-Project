#!/bin/bash
# to kill multiple runaway processes, use 'pkill runaway_process_name'
# For the Java implementation, use the following format: ./tests1.sh your_client.class [-n]

algorithm=$1
trap "kill 0" EXIT

echo "running their implementation..."
sleep 1
../ds-sim/ds-server -c configs/daconfig.xml -v all > theirs.txt&
sleep 1
../ds-sim/ds-client -a $algorithm

echo "running our implementation..."
sleep 2
./ds-server -c configs/daconfig.xml -v all > ours.txt&
sleep 1
python3 ../src/client.py -a $algorithm
sleep 1

echo "testing done!"
