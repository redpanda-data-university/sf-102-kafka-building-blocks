## Chapter 1 - Storage Layer
In Chapter 1 of the Kafka Building Blocks course, we explored the following components:

- Clusters
- Brokers
- Topics
- Partitions

The commands we executed are shown below:

```sh
# start the Redpanda cluster
docker-compose up -d

# set an alias for the `rpk` executable
alias rpk="docker exec -ti redpanda-1 rpk"

# inspect the cluster
rpk cluster info

# create a regular topic
rpk topic create sales \
    --partitions 12 \
    --topic-config cleanup.policy=delete \
    --topic-config retention.ms=1209600000 \
    --replicas 1

# create a compacted topic
rpk topic create users \
    --partitions 4 \
    --topic-config cleanup.policy=compact \
    --replicas 1

# list the topics
rpk topic list

# describe a topic
rpk topic describe sales

# add partitions to a topic
rpk topic add-partitions sales --num 2

# alter the configuration of a topic
rpk topic alter-config sales --set retention.ms=604800000

# delete a topic
rpk topic delete sales users
```

The course also demonstrates how to use Redpanda Console to inspect clusters, brokers, topics, and partitions. Please see the course for more information.
