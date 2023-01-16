Scalable computing over the internet. Most computing is done on
a single compute node. If the computation needs more than
a node or parallel processing, like many scientific computing problems,
we use parallel computers. Simply put, a parallel computer
is a very large number of single computing nodes with specialized
capabilities connected to other network. For example, the Gordon Supercomputer here
at The San Diego Supercomputer Center, has 1,024 compute nodes with 16 cores each
equalling 16,384 compute cores in total. This type of specialized
computer is pretty costly compared to its most recent cousin,
the commodity cluster. The term, commodity cluster,
is often heard in big data conversations. Have you ever wondered
what it exactly means? Commodity clusters are affordable
parallel computers with an average number of computing nodes. They are not as powerful as
traditional parallel computers and are often built out of
less specialized nodes. In fact,
the nodes in the commodity cluster are more generic in their
computing capabilities. The service-oriented computing community
over the internet have pushed for computing to be done on commodity
clusters as distributed computations. And in turn, reducing the cost
of computing over the Internet. In commodity clusters,
the computing nodes are clustered in racks connected to each other
via a fast network. There might be many of such
racks in extensible amounts. Computing in one or
more of these clusters across a local area network or the internet
is called distributed computing. Such architectures enable what
we call data-parallelism. In data-parallelism many jobs
that share nothing can work on different data sets or
parts of a data set. This type of parallelism sometimes
gets called as job level parallelism. But in this specialization,
we will refer to it as data-parallelism in the context of Big-data computing. Large volumes and varieties of big
data can be analyzed using this mode of parallelism, achieving scalability,
performance and cost reduction. As you can imagine, there are many
points of failure inside systems. A node, or
an entire rack can fail at any given time. The connectivity of a rack
to the network can stop or the connections between
individual nodes can break. It is not practical to restart everything
every time, if failure happens. The ability to recover from such
failures is called Fault-tolerance. For Fault-tolerance of such systems,
two neat solutions emerged. Namely, Redundant data storage and restart of failed
individual parallel jobs. We will explain these two solutions next. As a summary the commodity
clusters are a cost effective way of achieving data parallel scalability for
big data applications. These type of systems have a higher
potential for partial failures. It is this type of distributed
computing that pushed for a change towards cost
effective reliable and Fault-tolerant systems for
management and analysis of big data.