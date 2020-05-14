#!/bin/bash
# to kill multiple runaway processes, use 'pkill runaway_process_name'
# For the Java implementation, use the following format: ./tests1.sh your_client.class [-n]

algorithm=$1
trap "kill 0" EXIT

echo "Running their implementation..."
sleep 1
../ds-sim/ds-server -c configs/daconfig.xml -v all > theirs.txt&
sleep 1
../ds-sim/ds-client -a $algorithm

echo "  "
echo "Running our implementation..."
echo "# client.py 15-May-2020, 2020 Authored by: Avi.R, Cooper.T, Tom.T
# Client started with '../src/client.py -a wf'"
sleep 2
./ds-server -c configs/daconfig.xml -v all > ours.txt&
sleep 1
python3 ../src/client.py -a $algorithm
sleep 1

echo "  "
echo "Testing Complete!"

TEST_OUTPUT=$false
OUT=$(diff ours.txt theirs.txt)

sleep 1
echo "  "
echo "Checking Difference..."
TEST_OUTPUT=$(diff <(echo "$OUT") EXPECTED_DIFF.txt)

sleep 1
if [$TEST_OUTPUT != $false]
then 
	echo "Yay! :D THERE IS NO DIFFERENCE!"
else
	echo "Oh No! D: THERE IS A DIFFERENCE!"
fi

