## Chapter 2 - Communication Layer
In Chapter 2 of the Kafka Building Blocks course, we explored the following components:

- Kafka / Redpanda records
- Producers
- Consumers
- Consumer Groups

We created a basic producer (see [here][basic-producer]), a producer that provides a record key and event timestamp (see [here][key-producer]), and a simple consumer that can be instantiated multiple times to create a consumer group (see [here][simple-consumer]).

[basic-producer]: /02-communication-layer/producer-examples/basic.py
[key-producer]: /02-communication-layer/producer-examples/basic.py
[simple-consumer]: /02-communication-layer/consumer-examples/consumer.py

The commands we executed are shown below:

```sh
# start the Redpanda cluster
docker-compose up -d

# set an alias for the `rpk` executable
alias rpk="docker exec -ti redpanda-1 rpk"

# inspect the cluster
rpk cluster info

# create and activate a Python virtual environment
python3 -m venv
source bin/activate

# install the kafka-python dependency
pip install kafka-python-ng

# create the purchases topic
rpk topic create purchases -p 4

# run a basic producer (see producer-examples/basic.py)
python -m producer-examples.basic

# run a producer that groups related records by key, and uses event-time semantics
python -m producer-examples.with_key_and_timestamp

# run one or more consumers
# tab 1
python -m consumer-examples.consumer.py

# tab 2
python -m consumer-examples.consumer.py

# inspect the consumer groups
rpk group list

# get detailed information about the group
rpk group describe my-group
```

Please see the course for more information.
