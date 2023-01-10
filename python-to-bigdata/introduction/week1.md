# introduction to big data

## why big data?

#### what launched the big data era?

our phones and the apps installed in them are a big source of big data which all the time, every day, contributes to our core.

**cloud computing**: computing anywhere and anytime (on-demand computing). this ability + torrent of data = opportunity to perform data analysis to tell us things about the world and ourselves

#### applications: what makes big data valuable

big data &rarr; better models &rarr; higher precision (&rarr; smart and personalized business)

big data has eneabled **personalized marketing**:
- big data &rarr; personalized marketing data &rarr; happy costumers
- consumers generate data through social media
- areas and techniques:
  1. recommendation engines: predict best match products (amazon, netflix)
  2. sentiment analysis: analysis of feelings with reviews using natural language processing, referred to as opinion mining
  3. mobile advertising
  4. consumer growth to guide product growth: using consumer behaviour as a whole
  5. biomedical applications and personalized medicine
  6. bid ata-driven cities

#### examples

###### saving lives with bidata

we cannot control fire storms, bit can predict their behaviour: use bigdata to monitor, predict and manage a firestorm: **wildfire analytics**:
1. prediction
2. response

why can bigdata help? streams in data torrent:
1. people: devices they carry
2. sensors and satellites, things that measure environmental factors
3. organizations: area maps, service updates and databases

&rarr; **integration of diverse data**: see new things develop predictive analysis

diverse data sources:
1. machine data: temperature, humidity, air pressure including image data streaming
2. organizational data: institutions that enerate info, they provide valuable data that is curated and verified
3. people on social medias: hardest data sources to streamline but can be very valuable once integrated

things you can do with such data:
1. monitoring
2. visualization
3. fire modeling: analysis and modeling to predict

###### using bigdata to help patients

precision medicine: area of medicine targeted toward an individual person (analyze genetics, environment, daily activities) to detect or predict a health problem early, help prevent disease and provide right drug at right dose in case of illness

key components of changes:
- reduced cost of data generation and analysis
- increased availability of cheap large data storage
- increased digitization of previously paper records
- **we need one more**: combine various types of data produced by different groups in a meaningful way

putting data together, integration of:
1. people: most interesting
   - mobile health apps that record data from sensors and generated from people 
   - **human sensors**: information recorded by humans and not necessarily by sensors (like minutes of mindfulness a day)
   - the impact of novel people-generated data: accuracy and quality of data patients provide by memory during doctor appointments is very low (not exactly patients fault, they may be unsure or forgotten); **today** people are self reporting reactions and experiences through social media, blogs, online support groups, sources of data that wasn't available before
2. sensors: generated info was used only in real time and then discarded, now it is being gathered to be stored and analyzed
   - fitness devices: their goal is to improve wellness by having you monitor your daily status; the data they generate can be very useful medical information, but this data alone wouldn't drive the dream of precision medicine
   - integration of fitness devices + electronic health records + genomic profile (remains an open question) 
3. organizations: carry experimental and computed data to interpret
   - scientific data and knowledge bases: assemble human knowledge in a machine processable form

integration &rarr; personalization &rarr; precision

###### A Sentiment Analysis Success Story: Meltwater helping Danone

Meltwater helped Danone to monitor the opinions through social media for one of their marketing campaigns. They were able to measure what was impactful and what was not, through such monitoring.

> 90% of the information ever generated was generated in the last two years; other facts [here](http://www.slideshare.net/BernardMarr/big-data-25-facts/2-Every_2_dayswe_create_as)

## big data: where does it come from?

combining types of data &rarr; big data value
1. wisdom
2. knowledge
3. information
4. data

data enabled decisions and actions:

### machine-generated data

- largest source
- smart devices
  - they connect to other devices and networks
  - collect and analyze data autonomously
  - provide environmental context
- **the internet of things**: everything connected and generating data
- machines collect data 24/7 via their built-in sensors, at personal and industrial scales

increasing number of machines that sense `x` 
data collected by each device `=`
machines &rarr; biggest source

#### advantages

- in-situ: bring computation to data
- real-time notifications enable real-time actions
- design differently
- culture shift to real-time operations
- icreased use of scalable computing
- SCADA

machine generated data can uniquely enable real-time actions in many systems and processes, but a culture shift is needed for its computing and real-time action.

### big data generated by people (the unstructured challenge)

- people generate massive amounts of data through daily activities in social media, photo and video sharing, blogs, messages, emails, documents
- this data is
  - text-heavy
  - unstructured: data that does not conform to a predefined data model
- brings challenges

> eighty to ninety percent of entire data is unstructured 

- **velocity**: volume and fast generation of data

tools `+` data `+` skilled people `=` value

#### how is it being used?

- tools are designed to manage unstructure information and analyze it, majority of them are based on `Hadoop`, an open source big data framework
  - `Hadoop` is designed to support the processing of large data sets in a distributed computing environment
- `Storm` and `Spark`: two other open source frameworks that handle real time data generated at a fast rate
- ETL (extract, transform and load) process doesn't fit unstructured data; businesses use a hybrid approach
  1. smaller structured data remains in relational databases
  2. large unstructured datasets get stored y NoSQL databases in the cloud
- NoSQL Data technologies are based on non-relational concepts and provide data storage options

As we saw big data must pass through a series of steps before it generates value. Namely data access, storage, cleaning, and analysis.

One approach to solve this problem is to run each stage as a different layer.

And use tools available to fit the problem at hand, and scale analytical solutions to big data.

unstructured people generated data &rarr; emerging big data tools and approaches &rarr; better decisions, increased productivity, profits and societal impact

As a **summary**, although there are challenges in working with unstructured people generated data at a scale and speed that applications demand. There are also emerging technologies and solutions that are being used by many applications to generate value from the rich source of information.

### organization-generated data (structured but often siloed)

- closest to what most businesses currently have
- how organizations produce data: depends on each organization business model
- almost every event can be potentially stored, for example:
  - commercial transactions
  - banking/stock records
  - credit cards
  - government open data
  - e-commerce
  - medical records
  - etc
- organizations store info for current and future use, as well as past analysis
- highly structured data (including spreadsheets): structure defined by a model
- relational databases are highly adopted by many organizations
- **querying the data**: commonly used languages (like SQL) to extract data of interest from tables
- challenge to integrated structured data: **data silos** within an organization, no one system has access to all data, each dataset is compartmentalized; if they are left untouched, there is a risk to having **outdated, unsynchronized and even invisible** data sets.

Organizations are realizing the detrimental outcomes of this rigid structure. And changing policies and infrastructure to enable integrated processing of all data to the entire organization's benefit. Cloud-based solutions are seen as agile and low capital intensive solutions in this area. As a summary, while highly structured organizational data is very useful and trustworthy, and thus a valuable source of information, organizations must pay special attention to breaking up the silos of information to make full use of its potential.

#### benefits come from commbining with other data types

- examples
  - UPS: route optimizations
  - Walmart: find patterns 
- early adopters of big data analytics have gained a significant lead over the rest of the corporate world

As a summary, organizations are gaining significant benefit from integrating big data practices into their culture and breaking their silos. Some major benefits to organizations are operational efficiency, improved marketing outcomes, higher profits, and improved customer satisfaction.

### the key: integrating diverse data

real value comes from integrating different types of data; **data integration** means bringing together data from diverse sources and turning them into coherent and more useful information. **turning complex data into something useful.**
1. discovering, accessing, monitoring
2. modeling, transforming

why do we need it? data integration &rarr; 
1. richer data
2. increase data collaboration
   - reduce data complexity
   - increase data availability
   - unify your data system
  
Overall by integrating diverse data streams you add value to your big data and improve your business even before you start analyzing it.

> extra resources:
> - [McKinsey report](http://www.mckinsey.com/business-functions/business-technology/our-insights/big-data-the-next-frontier-for-innovation)
> - [The WIFIRE Project](https://www.youtube.com/watch?v=0ohwGggaXZM)