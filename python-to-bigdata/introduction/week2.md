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

### getting value out of big data

**data science**: basis for empirical research where data is used to induce information for *observations*. turns data into *insights* or even *actions*.
- big data &harr; insight &harr; action
- **observations**: data (big data) related to a business or scientific case
- **insights**: the data products of data science. extracted from data through exploratory data analysis and modeling: 
  - big data `+` analysis and question &rarr; insight
- it is not static, involves a process where models are constantly improved
- using data science and analysis of the past and current information, data science generates **actions**: it is a generation of *actionable information* for the future
  -  historical data `+` near real-time data `=` **prediction**
- happens at the intersection of:
  1. computer science
     - advanced computing
     - data engineering
     - domain expertise
     - data visualization
     - machine learning
  2. mathematics
    - statistics
      - statistical modeling
    - scientific method
    - relational algebra
    - problem solving
    - (and other sets of expertise that require **deeper knowledge** and skills)
  3. business expertise
     - business pasion
  - (a lot of skills to have for a single person)

> (image of list of skills from slides)

  - in reality, data scientists are teams of people who act like one

data scientists:
- are passionate about the story and the meaning behind data
- understand the problem they are trying to solve
- aim to find the right analytical methods to solve this problem
- have an interest in engineering solutions to solve problems
- have curiosity about each others work
- have communication skills to interact with the team and present their ideas and result to others

As a summary, a data science team often comes together to analyze situations, business or scientific cases, which none of the individuals can solve on their own. There are lots of moving parts to the solution. But in the end, all these parts should come together to provide actionable insight based on big data.

Being able to use evidence-based insight in business decisions is more important now than ever. Data scientists have a combination of technical, business and soft skills to make this happen.

### building a big data strategy

**strategy**: plan of action or policy designed to achieve a major or overall aim
1. aim
2. policy
3. plan
4. action 

**big data strategy**

when building one, we look at:
- what we have
- what high level goals we want to achieve
- what we need to do to get there
- what are the policies around data from the beggining to the end

steps to build one:
  
1. starts with big **objectives** (goals): identify which data is useful and why by focusing on what data to collect
   - these are questions to turn big data into advantage for your business
   - once defined, look at what you have and analyze the gaps and actions to get there
   - focus on short and long term objectives
   - each company needs to evaluate how data science or big data analytics would add value to their business objectives
2. create a culture to embrace that analytics can help your business: provide organizational **buy-in**
   - a big data strategy must have: 
     - commitment
     - sponsorship
     - community
   - goals should be developed with all stakeholders
3. build data science **team**; a diverse team is necessary to be effective: diverse expertise and diverse as a team
   - with:
     - data scientists
     - application developers
     - information technologists
     - business owners
   - *one for all*: mentality that everyone works together as partners with common goals
4. build in-house **expertise**: constant training of team members on:
   - big data tools and analytics
   - bussiness practices and objectives
5. open a mini **idea lab**: small data science team whose main job is do data experiments and test new ideas with a research level role
   - come up with ideas
   - deploy analytics
   - include customers in experiments
   - deploy full scale in case idea works
6. **share data**: data across the organization is easily accesed and integrated
   - remove barriers to data access
   - no data silos
   - data sharing mindset
7. defining big data **policies**
   - privacy and lifetime
   - curation and quality
   - interoperability and regulation
   - questions you should think of addressing around policy:
     - What are the privacy concerns?
     - Who should have access to, or control data?
     - What is the lifetime of data, which is sometimes defined as volatility, anatomy of big data?
     - How does data get curated and cleaned up?
     - What ensures data quality in the long term?
     - How do different parts of your organization communicate or interoperate using this data?
     - Are there any legal and regulatory standards in place?
8. cultivate **analytics-driven culture**: analytics `+` business `=` opportunities and growth
   - analytics is an integral part of doing business
   - willing to use analytics in driving business decisions
9. **adapt** strategy to your use cases: make business dynamic in face of change 

#### summary

1. integrate analytics
2. communicate goals
3. build teams
4. share data
5. adopt for new situations

### five P's of data science

> see [notes](ps.md) for 5 P's from WorDS Center

#### how does big data science happen?: five components of data science

data science: a multi-disciplinary craft that combines [people](#people) teaming up around application-specific [purpose](#purpose) that can be achieved through a [process](#process), big data computing [platforms](#platforms), and [programmability](#programmability).

![alt text](imgs/p-of-data-science.jpg "components of data science")

> all of these should lead to products where the focus really is on the questions or purpose that are defined by your big data strategy ideas.

![alt text](imgs/purpose.png "purpose")

> a typical conversation around the process starts with: *let's not dive into the techniques yet; what is the problem at large? how do we see ourselves solving it?*
>
> this leads to **challenges** I can then use to define **problems**

##### people

refers to a data science team or the projects stakeholders; they're expert in data and analytics, business, computing, science, or big data management.

##### purpose

refers to the challenge or set of challenges defined by your big data strategy.

##### process

people with *purpose* will define a process to collaborate and communicate around. it is conceptual in the beginning and defines the set of steps an how everyone can contribute to it

steps (see links for next section notes):

1. big data engineering
   1. [acquire](#acquiring-data)
   2. [prepare](#pre-processing-data)
2. (big data analytics (computational big data science)
   1. [analyze](#analyzing-data)
   2. [report](#communicating-results)
   3. [act](#turning-insights-into-action)

iterating process:
   
![](imgs/process.png "process")

> this process should support experimental work and dynamic scalability on the big data and computing platforms

##### platforms

computing platforms to scale different steps. scalability should be in the mind of all team members and get communicated as an expectation.

##### programmability

scalable process should be programmable through utilization of reusable and reproducible programming interfaces to libraries, like systems middleware, analytical tools, visualization environments, and end user reporting environments.

##### sixth p: data product

data science can be defined as a craft of using the five P's identified in this lecture, leading to a sixth P, the data product

### asking the right questions

formulate the question:

1. the first step is to **define the problem** that needs to be addressed, or the opportunity that needs to be ascertained.

> *A problem well defined is a problem half solved.* - Charles F. Kettering

2. **assess the situation** to get an overview of the situation: exercise caution analyzing risks, costs, benefits, contingencies, regulations, resources and requirements of the situation.
3. **define goals** and objectives based on answers
   - define success criteria

(transcript of video [here](questions.md))

## the process of data analysis

### steps in the data science process

1. [acquiring data](#acquiring-data): it includes anything that makes us retrieve data including; finding, accessing, acquiring, and moving data. It includes identification of and authenticated access to all related data. And transportation of data from sources to distributed files systems. It includes way to subset and match the data to regions or times of interest. As we sometimes refer to it as geo-spacial query.
2. [exploring data](#exploring-data)
3. [pre-processing data](#pre-processing-data)
4. [analyzing data](#analyzing-data)
5. [communicating results](#communicating-results)
6. [turning insights into action](#turning-insights-into-action)

#### acquiring data
#### exploring data
#### pre-processing data
#### analyzing data
#### communicating results
#### turning insights into action

# useful links
- https://support.typora.io/Draw-Diagrams-With-Markdown/