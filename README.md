# Distributed-Systems-Project
## Resource Efficient Job Scheduler for a Distributed Environment
This is where we will be working on a *job scheduler* to distribute tasks among a set of working servers. 

There are 2 steps to running the simulator: starting the server, and then running the client.

### Starting the Server
Ensure you are in the /simulator directory, and run the following command in a terminal window:
`./ds-server -c {{config-file}} -v all`, where {{config-file}} is replaced by the path to your config file (examples of which can be found in /simulator/configs).

Example usage: `./ds-server -c configs/ds-config1.xml -v all`

### Running the Client
Once you have started the server, you now need to run your client. Ensure you are in the /src directory, and, in a separate terminal window, run the following command:
`python3 client.py`

If successful, your resource-efficient job scheduler should now run!


### Comparing Baseline Algorithms
Within the /simulator directory you can compare baseline algorithms (first-fit, best-fit, worst-fit) implemented by MQ Uni's simulator: `ds-client` and our baseline implementations within our client simulator: `/src/client.py`

Simply run the bash script `run-comparison-test.sh {{algorithm}}` where {{algorithm}} is replaced by your choice of algorithm: ff, bf, wf.

Example usage:
`./run-comparison-test.sh bf` -> This runs the different baseline algorithm implementations of `bf` = best-fit in `simulator/ds-client` and `src/client.py`, compares the output for any differences.
