# Scientific Article Summarization using LSTMs
This system is aimed at generating automated summary(abstract) of a scientific article using Deep Learning tools. Specifically, we **use LSTMs over representations of different portions of a scientific article for generating its abstract**. The repository contains all the codes needed for running different modules of our framework.

A detailed proposal of this project can be found here: [PROJECT PROPOSAL LINK]()
A descriptive presentation containing the final results can be found here: [PROJECT PRESENTATION LINK]()

## System Overview
![Scientic Article Summarization Overview](https://github.com/ash-shar/Scientific-Article-Summarization-using-LSTMs/blob/master/System-Overview.PNG?raw=true "Title")



## Major Challenge

Scientific articles are too long to be processed for current GPUs using LSTMs. Hence, we need to get to a compressed representation of the paper retaining important information conveyed by the paper, before applying the **sequence-to-sequence mapping** task.

## Dataset Used

LaTeX sources of articles from **arxiv.org** (16,780 articles in total).

## Prerequisites

For using our framework you will need Python 2.7+ with the following modules installed:

- [plasTeX](https://pypi.python.org/pypi/plasTeX/1.0)
- [tensorflow]()
- nltk
- stemming.porter2

## Running the System

### Step 1: Pre-processing Latex Sources

For parsing latex sources, we make use of the python library [pylatexenc](). We make following modification to this library for effective pre-preprocessing of the articles:

1. Sections and Subsections of articlewere identified and marked
2. Figures, Tables and Mathematical Equationswere replaced by representative tokens
3. Obtained Structure was converted to LSTM input format

For running our pre-processor, use the shell script [preprocess.sh](1-Preprocessing/preprocess.sh). Provide Input Folder (Containing unzipped folders for each paper-downloaded from arxiv.org) and Output Folder (folder where you want the output to be generated). Sample run:
```
./preprocess.sh ../Sample_Data/Papers_Folder/ ../Sample_Data/Output/
```
2 major outputs will be generated in the output folder:

- **all-parsed-papers-category.txt:** File with a paper in each row. Each row contains 4 columns: paper_id, title of the paper and a dictionary containing all the sections of the paper, and paper's abstract - all tab separated. The dictionary has section's heading as its keys and the section's content as the corresponding value.

- **Final_Output:** Folder containing 2 subfolders: 
        - *input:*  Folder containing a file corresponding to each paper. Files contain corresponding paper text.
        - *model:* Folder containing a file corresponding to each paper. Files contain corresponding paper abstract.

Sample Input is present in the [Sample_Data](Sample_Data/) folder.

### Step 2: Generating representations using Para2Vec
Next, we use Para2vec for generating representations of the parsed articles. Para2Vec learns continuous representations for larger blocks of text, such as sentences, paragraphs or entire documents in an unsupervised fashion.

![Para2Vec Model](https://github.com/ash-shar/Scientific-Article-Summarization-using-LSTMs/blob/master/Para2Vec-Model.jpg?raw=true "Title")

For , 

### Step 3: Training and Testing the LSTM model
