# EMR - Elastic Map Reduce

## Architecture

- hadoop common
  - core of Hadoop framework
  - jar files to run Hadoop
- hadoop distrubuted file system **HDFS**
  - fault tolerant
  - data replication, store large files as blocks replicated
  - high throughput
- hadoop yarn
  - Yet Another Resouce Negotiator
- hadoop MapReduce
  - process large datasets
  - map: splits data into smaller chunks
  - reduce: reduce chunks into output file

### Yarn

- Resource Manager, runs on master node
- Node Manager, runs on slave nodes
- Application Master, managers containers on slave nodes
- Containers, actual working code

### MapReduce

- phases
  - Input
    Read in data
  - Split
    Create key, value pairs of data
  - Map
    Runs map function on key, value pairs
  - Shuffle
    Move keys to correct reducers
  - Reduce
    Run reduce function on key, value pairs
  - Result
    Save reduce output to file
