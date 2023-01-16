What is a Distributed File System? Most of us have file
cabinets in our offices or homes that help us store
our printed documents. Everyone has their own
method of organizing files, including the way we bin similar
documents into one file, or the way we sort them in alphabetical or
date order. When computers first came out,
the information and programs were stored in punch cards. These punch cards were
stored in file cabinets, just like the physical
file cabinets today. This is where the name,
file system, comes from. The need to store information in
files comes from a larger need to store information in the long-term. This way the information lives
after the computer program, or what we call process,
that produced it terminates. If we don't have files, our access to
such information would not be possible once a program using or producing it. Even during the process, we might need
to store large amounts of information that we cannot store within the program
components or computer memory. In addition, once the data is in a file, multiple processes can access
the same information if needed. For all these reasons, we store
information in files on a hard disk. There are many of these files, and they get managed by your operating system,
like Windows or Linux. How the operating system manages
files is called a file system. How this information is stored
on disk drives has high impact on the efficiency and speed of access to
data, especially in the big data case. While the files have exact addresses for
their locations in the drive, referring to the data units of sequence of these
blocks, that's called the flat structure, or hierarchy construction of index
records, that's called the database. They also have human readable symbolic
names, generally followed by an extension. Extensions tell what kind of file it is,
in general. Programs and
users can access files with their names. The contents of a file can be numeric,
alphabetic, alphanumeric, or binary executables. Most computer users work
on personal laptops or desktop computers with
a single hard drive. In this model, the user is limited
to the capacity of their hard drive. The capacity of different devices vary. For example, while your phone or tablet might have a storage capacity
in the order of gigabytes, your laptop computer might have a terabyte of
storage, but what if you have more data? Some of you probably had
issues in the past with running out of space on your hard drive. A way to solve this is to have
an external hard drive and store your files there or,
you can buy a bigger disk. Both options are a bit of a hassle, to
copy the data to a new disk, aren't they? They might not even be
an option sometimes. Now imagine, you having two computers and storing some of your data in one and
the rest of your data in another. How you organize and partition your data
between these computers is up to you. You might want to store your
work data in one computer and your personal data in another. Distributing data on multiple
computers might be an option, but it raises new issues. In this situation, you need to know
where to find the files you need, depending on what you’re doing. You can find it manageable,
if it’s just your data. But now imagine having
thousands of computers to store your data with big volumes and
variety. Wouldn't it be good to have a system
that can handle the data access and do this for you? This is a case that can be handled
by a distributive file system. Now, let's assume that there
are racks of these computers, often even distributed across the local or wide area network, because such file
systems, distributed file systems. Data sets, or parts of a data set, can be replicated across the nodes
of a distributed file system. Since data is already on these nodes,
then analysis of parts of the data is needed in a data parallel fashion,
computation can be moved to these nodes. Additionally, distributed file
systems replicate the data between the racks, and also computers
distributed across geographical regions. Data replication makes
the system more fault tolerant. That means, if some nodes or
a rack goes down, there are other parts of the system,
the same data can be found and analyzed. Data replication also helps with scaling
the access to this data by many users. Often, if the data is popular, many
reader processes will want access to it. In a highly parallelized replication, each reader can get their own node
to access to and analyze data. This increases overall system performance. Note that a problem with having
such a distributive replication is, that it is hard to make
changes to data over time. However, in most big data systems,
the data is written once and the updates to data is maintained
as additional data sets over time. As a summary, a file system is
responsible from the organization of the long term information
storage in a computer. When many storage computers
are connected through the network, we call it a distributed file system. Distributed file systems provide data
scalability, fault tolerance, and high concurrency through partitioning and
replication of data on many nodes.