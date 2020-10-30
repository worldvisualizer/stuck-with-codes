#!/usr/bin/env bash

ind=0
pids=()
for firstind in $(seq 5); do
    (
	echo "first job, sleeping $firstind"
        sleep $firstind
    ) &
    pids[${ind}]=$!
    echo ${pids[$ind]}
    ind+=1
done

for secondind in $(seq 5); do
    (
	echo "second job, sleeping $secondind"
        sleep $secondind
    ) &
    pids[${ind}]=$!
    echo ${pids[$ind]}
    ind+=1
done

for pid in ${pids[*]}; do
    echo "waiting for the pid: $pid"
    wait $pid
done


