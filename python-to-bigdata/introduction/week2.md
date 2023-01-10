# characteristics of bigdata and dimensions of scalability

## characteristics of big data

big data is a blanket term that is used to refer to any collection of data so large and complex that it exceeds the processing capability of conventional data management systems and techniques.

**characteristics**:
1. [volume](#volume): vast amounts of data that is generated every second, mInutes, hour, and day in our digitized world.
2. [variety](#variety): refers to the ever increasing different forms that data can come in such as text, images, voice, and geospatial data.
3. [velocity](#velocity):  refers to the speed at which data is being generated and the pace at which data moves from one point to the next.
   
volume, variety, and velocity are the **three main** dimensions that characterize big data

4. [veracity](#veracity): refers to the biases, noise, and abnormality in data. Or, better yet, It refers to the often unmeasurable uncertainties and truthfulness and trustworthiness of data
5. [valence](#valence): refers to the connectedness of big data in the form of graphs, just like atoms.

### volume

volume `=` size: volume is the big data dimension that relates to the sheer size of big data. is the dimension related to its size and its exponential growth.

data at an **astronomical** scale: **exponential** growth in data volume and storage.

relevance of volume? businesses and organizations are collecting and leveraging large volumes of data to improve their end products, whether it is safety, reliability, healthcare, or governance

**challenges** related to the massive volumes of bigdata:
1. storage: as the size of the data increases so does the amount of storage space required to store that data efficiently.
2. data acquisition: we need to be able to retrieve that large amount of data fast enough, and move it to processing units in a timely fashion to get results when we need them. this brings additional challenges, such as:
    - networking
    - bandwidth
    - cost of storing data
    - in-house vs cloud storage
3. retrieval
4. cost
5. scalability
6. performance

> as the volume increases performance and cost start becoming a challenge:
> `+` volume
> `-` performance
> `+` cost

> powers of ten video [here](https://www.youtube.com/watch?v=0fKBhvDjuy0)

### variety

variety `=` complexity (additional complexity that results from more kinds of data that we need to store, process, and combine)

today, a much wider variety of data are collected, stored, and analyzed to solve real world problems. 
1. image data, 
2. text data, 
3. network data, 
4. geographic maps, 
5. computer generated simulations
6. etc

**heterogeneity** of data can be characterized along several dimensions; axes of data variety:
1. structural variety - formats and models: difference in the representation of the data (EKG signal vs newspaper article vs satellite image vs tweet)
2. media variety - medium in which data get delivered (audio of speech vs transcript of speech: same information, different media)
3. semantic variety - how to interpret and operate on data (qualitative vs quantitatiive); another kind comes from  different assumptions of conditions on the data
4. availability variations - real-time? intermitent?

#### example: email

email and email collections demonstrate significant internal variation in structure, media, semantics, and availability:
1. **well-structured** (table-like part): sender, receiver, date, etc
2. **text**: body of the email
3. **multi-media**: attachments
4. **network**: who-sends-to-whom
5. **semantics**: a current email cannot reference a past email
6. **availability**: real-time?


### velocity

velocity `=` speed: velocity refers to the increasing speed at which big data is created and the increasing speed at which the data needs to be stored and analyzed.

processing of data in real-time to match its production rate as it gets generated is a particular **goal** of big data analytics.

#### real time processing vs batch processing

being able to catch up with the velocity of big data and analyzing it as it gets generated can even impact the quality of **human life** (sensors and smart devices monitoring the human body can detect abnormalities in real time and trigger immediate action, potentially saving lives.)

real-time processing is quite different from its remote relative, batch processing.

batch processing was the norm until a couple of years ago. Large amounts of data would be fed into large machines and processed for days at a time.

1. collect data
2. clean data
3. feed in chunks
4. wait
5. act

organizations which make decisions on latest data are more likely to hit the target. for this reason it's important to **match the speed of processing with the speed of information generation**, and get real time decision making power

batch processing is incomplete while real-time processing is fast.

> fortunately, with the event of cheap sensors technology, mobile phones, and social media, we can obtain the latest information at a much rapid rate and in real time in comparison with the past.

streaming data gives information on what's going on right now. streaming data has velocity, meaning it gets generated at **various rates**. and analysis of such data in real time gives agility and adaptability to maximize benefits you want to extract.

### veracity

veracity of Big Data refers to the **quality** of the data. it sometimes gets referred to as *validity* or *volatility* referring to the lifetime of the data.

- it is important for making big data operational.
- data is of no value if it's not accurate, the results of big data analysis are only as good as the data being analyzed.
- there are many ways to define data quality, in big data, it can be defined as a function of a couple of different variables:
  1. accuracy of data
  2. reliability of the data source
  3. context within analysis
  4. how meaningful the data is with respect to the program that analyzes it
- data provenance: transformations that big data go through up until the moment it is used for an estimate
- the growing torrents of big data pushes for fast solutions to utilize it in analytical solutions

### valence

valence `=` connectedness: more connected data have higher valences.

- **data connectivity**: two data items are connected when they are related to each other
  - data items are often **directly** connected to one another
    - city - its country
    - facebook users that are friends
    - employee - his work place
  - data could also be **indirectly** connected:
    - two scientists - they are both physicists
- **valence**: fraction of data items that are connected out of total number of possible connections
  - data connectivity increases over time, makes the data connections denser (which makes many regular, analytic critiques very inefficient)

#### challenges

- more complex data exploration algorithms
- modeling and prediction of valence changes
- group event detection
- emergent behaviour analysis

### sixth v: value

dimensions of big data and their challenging dimension:
1. volume &rarr; size
2. variety &rarr; complexity
3. velocity &rarr; speed
4. veracity &rarr; quality
5. valence &rarr; connectedness

at the heart of the big data challenge is turning all of the other dimensions into truly useful business **value** (bring value to the problem at hand). generate value out of big data.

> ["small" deifinition of big data](definition.md)

# data science: getting value out of big data

## defining the question

## the process of data analysis