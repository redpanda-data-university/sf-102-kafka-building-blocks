# Redpanda University
[Redpanda University][rpu] is a series of courses that will teach you the basics of event streaming, and will help you gain hands-on experience with a new data streaming platform called [Redpanda][rp].

## Streaming Fundamentals: Kafka Building Blocks
This repository contains code examples for the Kafka Building Blocks course from [Redpanda University][rpu]. The following chapters are included:

- [Chapter 1: Storage Layer][01-storage-layer]
- [Chapter 2: Communication Layer][02-communication-layer]
- Chapter 3: The Road Ahead (no tutorials)

[rp]: https://redpanda.com/
[rpu]: https://university.redpanda.com/

[01-storage-layer]: /01-storage-layer
[02-communication-layer]: /02-communication-layer

## Getting Started
To start a Redpanda cluster and the Redpanda Console (a UI for visualizing and managing clusters), run the following commands:

```sh
docker-compose up -d
```

Once the clusters are running, Redpanda Console will be available at: http://localhost:8080.

To interact with Redpanda from the commandline, set the following alias so that any invocation of `rpk` uses the pre-installed version in your local Redpanda cluster:

```sh
alias rpk="docker exec -ti redpanda-1 rpk"
```

From here, you can use `rpk` to interact with the Redpanda cluster:

```sh
rpk cluster info
```

Each chapter will contain a set of steps for you to execute. Please see in the [individual chapters](#streaming-fundamentals-kafka-building-blocks) for more information.

