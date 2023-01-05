# Additional Common Python Topics

**Description**

In this section you will learn package management in Python, how to debug and profile python code. Also, you will learn how to work with different data formats such as json, xml and yaml.

**Duration**

40h

**Why do we need to use a package manager?**

**Package Managers** are used to automate the process of **installing**, **upgrading**, **configuring**, and **removing** programs.

**Learning path**

1. Get familiar with **package manager**:
- [https://en.wikipedia.org/wiki/Package_manager](https://www.google.com/url?q=https://en.wikipedia.org/wiki/Package_manager&sa=D&source=editors&ust=1671237776608622&usg=AOvVaw2ljai5iz-NhrTzrGUhBbvM)
- [https://devopedia.org/package-manager](https://www.google.com/url?q=https://devopedia.org/package-manager&sa=D&source=editors&ust=1671237776609054&usg=AOvVaw0zQSqP0QF1tQ3_NhYwuEI0)

Key concepts which you need to know after reading:

- What is **package manager**
- What is the **package**
- Why is the package manager **required** in the first place
- Basic **functions** of a package manager
2. Learn about pip: [https://realpython.com/what-is-pip/](https://www.google.com/url?q=https://realpython.com/what-is-pip/&sa=D&source=editors&ust=1671237776610390&usg=AOvVaw1led0Wp4VbE1cc74xCTILp)

Key concepts which you need to know after reading:

- What is **pip**
- How to **install/uninstall/upgrade** packages
- **Finding** packages published to the [Python Package Index](https://www.google.com/url?q=https://pypi.org/&sa=D&source=editors&ust=1671237776611198&usg=AOvVaw3etKX_RF7fSealQFJemmYD) ([PyPI](https://www.google.com/url?q=https://pypi.org/&sa=D&source=editors&ust=1671237776611381&usg=AOvVaw3pM9FyYIGu5Ot44lQCmA7z))
- How to **generate/update** dependencies in file
- The problem with **hardcoding** the versions of your packages and their dependencies
- Difference between **development** and **production** dependencies
- Which **alternatives** exist
3. Learn about **PyPI**: [https://realpython.com/pypi-publish-python-package/](https://www.google.com/url?q=https://realpython.com/pypi-publish-python-package/&sa=D&source=editors&ust=1671237776612764&usg=AOvVaw2K_-lPzeYqdkEw4l-hgh0a)

Key concepts which you need to know after reading:

- **Configure** your package
- **Build** your package
- **Versioning** your package
- **Documenting** your package
- **Upload** your package to PyPI
4. Learn about **venv**: [https://realpython.com/python-virtual-environments-a-primer/](https://www.google.com/url?q=https://realpython.com/python-virtual-environments-a-primer/&sa=D&source=editors&ust=1671237776614406&usg=AOvVaw0gUJvBqJ7mIPteSaiS0Ys5) (you can skip section with **virtualenvwrapper**)

Try to practice by following the steps from the article on your local machine.

Key concepts which you need to know after reading:

- What is **venv**
- Main **goal** of using venv
- How does venv work
- How to **create** venv
- How to **activate/deactivate** venv
- How to **install/upgrade** packages inside venv
5. Learn about **Python Environment**: [https://realpython.com/effective-python-environment/](https://www.google.com/url?q=https://realpython.com/effective-python-environment/&sa=D&source=editors&ust=1671237776616542&usg=AOvVaw195f1khvUTV5fwjKD29gAx)

Key concepts which you need to know after reading:

- What is **shell** and which one should i use
- What is **Terminal** and which one should i use
- Run **Python Interpreter** via shell
- Manage **multiple** **versions** of Python on your system
- Manage **multiple projects** that use a single version of Python, using **virtual** Python environments

**Why do we need to use Profiling?**

Serious software development calls for **performance optimization**. Finding out why your program is slow by looking at its source code is a waste of time. It’s extremely **hard to guess** where a complex program is spending its time by just looking at the code. When you start optimizing application performance, you can’t escape looking at **profilers**. Let’s **not guess** and instead use a program to know *exactly* what’s going on in your program at runtime. That kind of program is called a profiler, and it will **save you time** on trial and error optimization.

**Learning path**

6. Learn about **Profilers**: [https://docs.python.org/3/library/profile.html](https://www.google.com/url?q=https://docs.python.org/3/library/profile.html&sa=D&source=editors&ust=1671237776619396&usg=AOvVaw1FhJgpXBPDuSKYK27Rgm8D)

Try to practice by following the steps from the article on your local machine.

Key concepts which you need to know after reading:

- What is **Profiling**
- How to **perform** Profiling
- Understand Profile **result**

**What is data serialization and why do we need to use it?**

Imagine that you want to store the contents of an object to a file, send an object to another process or transmit it across the network, you do have to think about how the object is represented because you will need to convert to a different format.

Serialization allows the developer to save the state of an object and recreate it as needed, providing storage of objects as well as data exchange. Through serialization, a developer can perform actions like sending the object to a remote application by means of a Web Service, passing an object from one domain to another, passing an object through a firewall as an XML string, or maintaining security or user-specific information across applications.

**Learning path**

1. Get familiar with data serialization: [https://en.wikipedia.org/wiki/Serialization](https://www.google.com/url?q=https://en.wikipedia.org/wiki/Serialization&sa=D&source=editors&ust=1671237776621759&usg=AOvVaw2kayKYMvSE9Pdd2zmKSQJl)

Key concepts which you need to know after reading:

- What is data **serialization**
- Difference between **serialization** and **deserialization**
- Use cases
2. Learn about **JSON**:
- [https://www.json.org/json-en.html](https://www.google.com/url?q=https://www.json.org/json-en.html&sa=D&source=editors&ust=1671237776622727&usg=AOvVaw2Qs91i9rLeU_fYTvXVNhcr)
- [https://docs.python.org/3/library/json.html](https://www.google.com/url?q=https://docs.python.org/3/library/json.html&sa=D&source=editors&ust=1671237776623042&usg=AOvVaw17tG1lU5fpaDqD5ILbHygz)

Try to practice by following the steps from the articles on your local machine.

Key concepts which you need to know after reading:

- What is **JSON**
- Understanding **structure**
- Where used
- How to **serialize** Python object to JSON object
- How to **deserialize** JSON object to Python object
- Difference between **loads()** and **load()**
- Difference between **dumps()** and **dump()**
3. Learn about **XML**:
- [https://en.wikipedia.org/wiki/XML](https://www.google.com/url?q=https://en.wikipedia.org/wiki/XML&sa=D&source=editors&ust=1671237776625460&usg=AOvVaw2_rF0CAhmaAReJlaVc8mB0)
- [https://lxml.de/tutorial.html](https://www.google.com/url?q=https://lxml.de/tutorial.html&sa=D&source=editors&ust=1671237776625907&usg=AOvVaw3cdEvlY3XoUPLXGQf3_DNs)

Try to practice by following the steps from the articles on your local machine.

Key concepts which you need to know after reading:

- What is **XML**
- Where used
- Understanding tree **structure**
- Build simple **tree**
- **Accessing** tree elements
- Tree **iteration**
- Use **XPath** to find text
- Serialization

# **Parsing**

- Use **E-factory** for generating XML
- Search elements with **ElementPath**
1. Learn about **YAML**:
- [https://yaml.org/spec/1.2/spec.html](https://www.google.com/url?q=https://yaml.org/spec/1.2/spec.html&sa=D&source=editors&ust=1671237776629326&usg=AOvVaw1SEY2qsV7CSIsUmxnH43Bs)
- [https://pyyaml.org/wiki/PyYAMLDocumentation](https://www.google.com/url?q=https://pyyaml.org/wiki/PyYAMLDocumentation&sa=D&source=editors&ust=1671237776629870&usg=AOvVaw2SO_WGmj5BxA3wr56fwGOC)

Try to practice by following the steps from the articles on your local machine.

****Key concepts which you need to know after reading:

- What is **YAML**
- Where used
- Understanding **syntax**
- Convert YAML object to Python object and vice versa

**Why is debugging important?**

Still **debugging** your code with **print** statements? Learn how to level up your ability to troubleshoot complex code situations by using the power of a fully-featured debugger in this talk aimed at all levels of programming ability

**Learning path**

Learn about **debugging**:

- [https://www.youtube.com/watch?v=5AYIe-3cD-s](https://www.google.com/url?q=https://www.youtube.com/watch?v%3D5AYIe-3cD-s&sa=D&source=editors&ust=1671237776633173&usg=AOvVaw1iruORcwlZPzKiIaE140Wj)
- [https://www.jetbrains.com/help/pycharm/debugging-your-first-python-application.html](https://www.google.com/url?q=https://www.jetbrains.com/help/pycharm/debugging-your-first-python-application.html&sa=D&source=editors&ust=1671237776633787&usg=AOvVaw1OuUjoVKzL8dWV3qWPhLa7)
- [https://docs.python.org/3/library/pdb.html](https://www.google.com/url?q=https://docs.python.org/3/library/pdb.html&sa=D&source=editors&ust=1671237776634258&usg=AOvVaw0Gw1pXe6SecqxTicVl0ZPu)
- [https://docs.python.org/3/library/debug.html](https://www.google.com/url?q=https://docs.python.org/3/library/debug.html&sa=D&source=editors&ust=1671237776634833&usg=AOvVaw1mr2NK4B5iGyZOhKOiUh0u)

Try to practice by following the steps from the articles on your local machine.

Key concepts which you need to know after reading:

- **Advantages** of using **debuggers** instead of **prints**
- Why use **debuggers**
- How to use **pdb** command line debugger
- Most important **commands** pdb
- Debug your code in **PyCharm**

Practical tasks (open in new tab): [https://github.com/gridu/PYTHON-BASIC/tree/master/practice/5_additional_topics](https://www.google.com/url?q=https://github.com/gridu/PYTHON-BASIC/tree/master/practice/5_additional_topics&sa=D&source=editors&ust=1671237776637492&usg=AOvVaw16dQweKH3yAIXZcXYpTThY)