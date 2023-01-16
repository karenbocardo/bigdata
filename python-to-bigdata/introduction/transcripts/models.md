Programming Models for Big Data. We have seen that scalable computing
over the internet to achieve data-parallel scalability for big data
applications is now a possibility. Thanks to commodity clusters. Cost-effective commodity clusters
together with advances in distributed file systems to move computation to data, provide a potential to conduct
scalable big data analytics. The next thing we will
talk about is how to take advantage of these
infrastructure advances. What are the right programming models? A programming model is an abstraction or
existing machinery or infrastructure. It is a set of abstract
runtime libraries and programming languages that
form a model of computation. This abstraction level can be low-level
as in machine language in computers. Or very high as in high-level programming
languages, for example, Java. So we can say,
if the enabling infrastructure for big data analysis is distributed
file systems as we mentioned, then the programming model for
big data should enable the programmability of the operations within
distributed file systems. What we mean by this being able to
write computer programs that work efficiently on top of distributed
file systems using big data and making it easy to cope with
all the potential issues. Based on everything we discussed so far, let's describe the requirements for
big data programming models. First of all, such a programming model for
big data should support common big data operations like
splitting large volumes of data. This means for partitioning and
placement of data in and out of computer memory along with a model
to synchronize the datasets later on. The access to data should
be achieved in a fast way. It should allow fast distribution to nodes
within a rack and these are potentially, the data nodes we moved
the computation to. This means scheduling of
many parallel tasks at once. It should also enable
reliability of the computing and full tolerance from failures. This means it should enable
programmable replications and recovery of files when needed. It should be easily scalable to
the distributed notes where the data gets produced. It should also enable adding new resources
to take advantage of distributive computers and scale to more or
faster data without losing performance. This is called scaling out if needed. Since there are a variety
of different types of data, such as documents, graphs,
tables, key values, etc. A programming model should enable
operations over a particular set of these types. Not every type of data may be
supported by a particular model, but the models should be optimized for
at least one type. Is it getting a little complicated? It doesn't have to have to be. In fact, we apply similar models in
our daily lives for everyday tasks. Let's look at the scenario where you
might unknowingly apply this model. Imagine a peaceful Saturday afternoon. You receive a phone call from a friend and
she says, she they will be at your
house in an hour for dinner. It seems like you completely forgot that
you had invited your friends for dinner. So you say, you are looking forward
to it and head to the kitchen. As a quick solution, you decide to
cook pasta with some tomato sauce. You need to take advantage
of parallelization, so that the dinner is ready by the time your
guest arrive, that's within an hour. You call your spouse and your teenage
kids to action in the kitchen. Now, you need to give them directions to
start dicing the ingredients for you. But in the heat of the moment, you end up
mixing the onions, tomatoes and peppers. Instead of sorting them first, you give everyone a randomly mixed
batch of different types of vegetables. They are required to use their computer
powers to chop the vegetables. They need to ensure not mix
different types of veggies. When everyone is done chopping, you want
to group the veggies by their types. You ask each helper to collect items
of the same type, put them in a large bowl and label this large bowl with
the sum of individual bowl weights like tomatoes in one bowl, peppers in
another and the onions in the third bowl. In the end, you have nice large bowls with the total
weight of each vegetable labeled on it. Your helpers are soon done with their work
while you're focused on coordinating their actions and other dinner tasks in the
kitchen, you can start cooking your pasta. What you have just seen is an excellent
example of big data modeling in action. Only it is really the data
processed by human processors. This scenario can be modeled by a common
programming model for big data. Namely MapReduce. MapReduce is a big data programming
model that supports all the requirements of big
data modeling we mentioned. It can model processing large data, split complications into
different parallel tasks and make efficient use of large commodity
clusters and distributed file systems. In addition, it abstracts out
the details of parallelzation, full tolerance, data distribution,
monitoring and load balancing. As a programming model, it has been implemented in a few
different big data frameworks. Next week,
we will see more details on MapReduce and how its Hadoop implementation works. To summarize, programming models for big data are abstractions over
distributed file systems. The desired programming models for
big data should handle large volumes and varieties of data. Support full tolerance and
provide scale out functionality. MapReduce is one of these models, implemented in a variety of
frameworks including Hadoop. We will summarize the inner workings
of the Hadoop implementation next week.