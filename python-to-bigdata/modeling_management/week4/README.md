# working with data models

## data models vs. data formats

> slides [here](slides/01_DataModelvsDataFormat.pdf)

- **format**: serialized representation of the data
  - foe example, csv files (csv does not mean relational)

## working with streaming data

### data stream

> slides [here](slides/02_WhatIsADataStream.pdf)

velocity of data coming in varying rates is a challenge; for some applications (streaming data processing applications) this presents the need to process data as it is generated (as it **streams**).

**streaming data processing applications**: constant stream of data flowing from a source (like a sensory machine or social media)

examples:
- making data-drive marketing decisions in real time from use of data
- monitor of industrial/farming machinery for detection of potential system failures
- any sensor network/internet of things environment controlled by another entity
- filghtstats, that processes flight events and turns it into intelligence and information

**data streaming**
- stream: a possibily unbounded **sequence of data** records (may or not be related or correlated with each other)
- generally timestamped or geo-tagged
- synchronized sequence of events
- can stream from many **sources** (instruments, internet of things, computer programs, websites, social media)
- streaming data sometimes get referred to as event data as each data item is treated as an individual event in a synchronized sequence
- streams pose very difficult **challenges** for conventional data management architectures, which are built primarily on the concept of persistence, static data collections
- streaming data management systems cannot be separated from **real-time processing of data**

**streaming data systems**
- they process data in motion
- computations done in near-real time
- subscribe non-interactivvely to sources (don't send back info or response)
- big data streaming systems examples:
  - amazon kinesis
  - apache storm
  - flink
  - spark streaming
  - samza 

**dynamic steering**
- dinamically changing the next steps or direction of app through continuous computational process using streaming
- part of streaming data management and processing
- examples
  - self-driven car
  - all streaming data applications
  - online gaming

### why is streaming data different?

> slides [here](slides/03_WhyIsStreamingDataDifferent.pdf)

streaming data must be handled differently than static data

**data-at-rest**: mostly static data collected from one or data sources; the analysis happens after data is collected 
- analysis is called **batch** or static processing
- in data processing algorithms the **size** determines time and space
- in batch processing the analytical steps have access to often all data, can take more time

**data-in-motion**: mode in which data gets analyzed at the same time it is being generated
- analysis is called **stream processing**
- data processing algorithms have **unbounded size**, but **finite** time and space; algorithms that require iteration are not possible since stream never ends
- management and processing:
  - compute one data element or small window of data element at a time
  - these computations can update metrics, monitor and plot statistics on the streaming data. Or apply analysis techniques to the streaming data to learn about the dynamics of the system as a time series
  - relatively fast
  - subscription to data source but with no interaction or feedback
  - can't be processed all at the same time

**hybrid architecture**
- lambda architecture for processing streaming and back jobs at the same time
- in these systems, streaming wheel over the real-time data is managed and kept until those data elements are pushed to a batch system and become available to access and process as batch data
- a stream **storage layer** is used to enable fast trees of streams and ensure data ordering and consistency
- and a **processing layer** for data is used to retrieve data from the storage layer to analyze it and most probably little bit to a batch data stream and notify the streaming storage that the data set does no longer need to be in streaming storage


- two main **challenges** that need to be overcome to avoid data loss, and enable real time analytical tasks
  1. streaming data **changes** over time
     - changes can be
       - periodic
       - sporadic
       -  dropping or missing data
       - no data when network or hardware problems

### understanding data lakes

> slides [here](slides/04_UnderstandingDataLakes.pdf)

what are data lakes?
- created in response of storage and processing challenges
  - need to ingest data into fast and scalable storage system, flexible enough
  - traditional warehouse don't fit big data challenges for streaming and batch applications
- data lakes enable batch processing of streaming data
- a data lake is a parth of a big data infrastructure that many streams can flow into and get stored for processing in their original form
- we can think of it as 
  - a massive storage depository 
  - with huge processing power 
  - and ability to handle a very large number of concurrence, data management and analytical tasks

how do they work? **schema-on-read**
1. data gets loaded from its source
2. data is stored in its native format until needed
3. at which time app can freely read dara and add structure to it
- ensures all data is used for a potentially unknown use at a later time

**schema-on-write**
- in traditional warehouses, data is loaded into warehouse after transforming (transform and structure before load)
- data is not loaded unless there is a use for it

#### data lake vs data warehouse

## hand-on: handling data streams

### Exploring Streaming Sensor Data

1. open terminal window
2. look at streaming weather station measurements
3. look at key for measurements
4. plot streaming measurements

> see complete instructions [here](hands-on/01_Exploring_Streaming_Sensor_Data.pdf)

### Exploring Streaming Twitter Data (Optional)

1. open terminal window
2. look at streaming tweets containing specific words
3. plot frequency of streaming tweets

- [instructions](hands-on/02_InstructionsforSettingUp_TwitterApp.pdf) to create twitter app
- [instructions](hands-on/03_Exploring_Streaming_Twitter_Data_(Optional).pdf) for exploring
  
