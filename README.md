
Project Title
=============

<!-- ![banner]() -->
<!-- ![badge]() -->
<!-- ![badge]() -->
This is a long description.

Table of Contents
-----------------

-   [Project Background](#projectbackground)
-   [Getting started](#Gettingstarted)
-   [Install & Setup](#installsetup)
-   [Usage](#usage)
-   [Running the tests](#tests)
-   [Authors](#authors)
-   [License](#license)

Background
----------

Huffman Coding is one of the lossless data compression techniques. It assigns variable-length codes to the input characters, based on the frequencies of their occurence. The most frequent character is given the smallest length code. 
This project implements the Huffman coding Algorithm in Python. It is an easy to use program.

Getting started
---------------

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

Install & Setup
---------------

This package depends upon a knowledge of [Python]() and [Linux]().


Usage
-----

First: You have to specify your file path.
You can set your file path in your environment variables
using export FILE_PATH ="your file path" or you can provide the path to your file as a string e.g "/home/user/Desktop/sample.txt"
To  run the HuffmanCompressor,
```python
from modules.HuffmanAlgorithm import HuffmanCompressor
huffman_instance = HuffmanCompressor(path=os.environ.get('SAMPLE_TEXT')) or HuffmanCompressor(path=path_string)
h=huffman_instance.compress() #return the compress file path
huffman_instance.decompress(input_path=h)  #returns the decompress file path
```   


Running the tests
-----------------
There are 11 test cases in this project.
To run all the test cases, you must be in the root directory of the project,and then copy and paste the the command below in your terminal
```python
  python -m unittest -v  test
```   




Authors
-------

* Akola Mbey Denis [:email:](mailto:mdakola@st.knust.edu.gh)  


License
-------

[MIT](https://choosealicense.com/licenses/mit/)
