# big data modeling (part 2)

## different kinds of data models (part 2)

### vector space model

> slides [here](slides/01_VectorSpaceModel.pdf)

data model that has been succesfully used to retrieve data from large collections of **text** and **images**.

text:
- thought of as unstructured data (because it doesn't have attributes and collections)
- it is a sequence of string punctuated by line and parent of breaks
- to find it, we need:
  - the text data itself
  - and a different structure that is computed from the text data; to create it a **vector model** is used

#### introduction
- input: a query document, output: documents that are similar to it 
- similarity is computed and used to search documents
- search engines use some form of vector models and similarity search to locate text data
- the same principle can be used for finding similar images

#### document vector

example steps
1. we have three different documents
2. create **term frequency matrix (TF)**
   - rows are documents
   - columns are words in the documents
   - each cell contain the number of ocurrences of each word on esach document 
3. create **inverse document frequency (IDF)** vector for each term
   - the document frequency of a term is the count of that term in the whole collection divided by the number of documents $DF = \frac{x}{n}$
   - n: number of documents (3)
   - x: ocurrences of word ("new" appears twice in collection, x = 2)
   - IDF is calculated by $ \log_2 (\frac{n}{x}) $, which, for "new" would be $ \log_2 (\frac{3}{2}) = 0.584 $
      - why $\log$ to the base $2$? there is no deep scientific reason for it, it is more of a convention in many areas of computer science; $\log_2 x$ is the same number as $\log_{10} x$ times $\log_2 10$ (which is a constant, so the relative score of IDF does not change regardless of the base used)
    - why IDF? there are common words (such as "is", "the", "a") that it's prevalence has a negative impact on its informativeness, so it lowers the number of frequencies: it **penalizes** words that are too commonplace in the collection
      - IDF is a penalty factor
4. multiply IDF and TF numbers to get a column-wise multiplication, the **tf-idf matrix** 
   - for each document we have a vector represented as a row
   - each row represents te relative importance of each term in the vocabulary
   - vocabulary: the collection of all words that appear in this collection
   - last column after each document vector is the **length** of the document vector (square root of the sum of squares, as the formula in slides)
 
#### searching in vector space

for the example, the document contains "new new york"

1. write query (like in google) to perform a search in the vector space
2. maximum frequency of terms
3. create query vector taking document vector of query and multiply each term by number of ocurrences divided by the maximum term frequency (2, in the example of slides), the output has two non-zero terms (for "new" and "york")
4. compute lenght of query vector
5. compute **similarity function** between query vector and each document (measuring how far the query vector is from each document) 

#### similarity function

- there are many similarity functions defined and used for different things
- popular similarity function: **cosine function**
  - measures the cosine function of the angle between these two vectors
  - (formula in slides)
  - if vectors are identical, the angle between them is zero, and cosine evaluates to one
  - as the angle increases, the value of cosine decreases to make them more dissimilar
  - to compute it, multiply corresponding elements of two vectors and then sum these products; this sum is then divided by the product of the document length and the query length 

in the result of the distance function it is noticeable that the document 1 is much more similar to the query than the other two

#### query term weighting

- similarity scoring and document ranking process works effectively but the method is cotton dry
- to accomplish having more control over the ranking of terms, put different weight on each query term
  - each query term has its own weight, the total weigth is the sum of all the weights
  - query vector and its lenght is computed as before
  - each term in the query vector is further multiplied by these relative weights
  - in result, each term has different rates and this changes the ranking of the documents

#### image search

- similarity search is often used for **images** using a vector space model
- one can compute features from images, one common feature is a **scatter histogram**
  - histogram of red, green and blue channels
  - is the count of pixels having a certain density value
  - think of histograms as a vector
  - table shown in slides es a feature vector where numbers for each row have been normalized with the size of the image to the row sum equal to one
- Similar vectors can be computed of the image texture, shapes of objects and any other properties. Thus making a **vector space model significant for unstructured data**.

### graph data model

> slides [here](slides/02_GraphDataModel.pdf)

- data + connectivity
  - graphs bear two kind of info: 
    1. properties and attributes of entities and relationships
    2. connectivity structure of the network

- graphs representation, **property graph model**: 
  - vertex or node table: gives ids to nodes and lists their properties
  - edge table has two parts: the properties of the edge and teh direction of the arrow in the arrow; there is a tuple for each edge

> Now representing connectivity information gives graph data a new kind of computing ability that's different from other data models we have seen so far. Even without looking at the properties of the nodes and edges, one can get very interesting information just by analyzing or querying this connectivity structure.

#### paths

- a very important class of operations in graph data that involves edge following based on some sort of conditions
- "optimal path" operations (optimization for path operations):
  - find the **shortest path** between two nodes (from source location to a target location)
  - find **optimal round-trip** path that must include some specific nodes (determine the order in which the nodes must be visited), eg: trip planner
  - find "best compromise" paths (**pareto-optimality**) between two nodes (best path given two or more optimization criteria that cannot be satisfied simultaneously)

#### neighborhoods

- the **neighborhood** of a node N in a graph is a set of edges directly connected to it
- a **K neighborhood** of N is a collection of edges between nodes that are, at most, K steps away from N.
- **community**: subgraph of a graph that has many more edges *within* the subgraph comepared to edges to nodes outside the subgraph (a higher density of edges within the community and a lower density across two different communities)
  - operations:
    - dense subgraph finding
    - optimization of clusteredness
- **anomalous** neighbourhoods are different from all others 
  - near star: the nodes connected to central are not connected between them
  - near clique: each node is connected to all other neighborhood nodes
  - heavy vicinity: some edges have an unusually heavy weight compared to the others
    - predominant edge: just **one** edge is predominantly high rate compared to all other

#### connectivity operations

- **connectedness** is fundamental property of a graph
  - every node is reachable from each node in the undirected version of the graph (though some path)
- **connected components**: a graph is not conneccted but there are subgraphs wich are connected

### other data models

> slides [here](slides/03_OtherDataModels.pdf)

#### array as a data model

- columns and rows
- indexed structure in `array[row][column]`, using indices to get value of data item
- number of dimensions -> number of indices
- k dimensional array can be represented as a relation (a table) with k + 1 columns
  - the number of tuples in this representation will be the product of size of first dimension times size of second and so forth
- arrays of vectors: the cells of an array have vectors as values (see slides for visual representation)
  - one can create combinations of array operations, vector operations and composite operations; operations for arrays of vectors:
    - `dim(A)` — number of dimensions of A
    - size of dimension
    - value of element at cell (i,j)
    - value of kth element at cell (i,j)
    - vector-length of the vector at cell (i,j)
    - vector distance between the values of two cells given distance functions\
    - (see slides for operation definitions )

## hands on

### Exploring Vector Data Models with Lucene

see instructions [here](hands-on/01-Exploring_Vector_Data_Models_with_Lucene.pdf)

### Exploring Graph Data Models with Gephi

summary of steps:
1. import data into gephi
2. examine properties of graph
3. perform statistical operations
4. run different layout algorithms

find complete hands-on [here](hands-on/02-Exploring_Graph_Data_Models_with_Gephi.pdf)