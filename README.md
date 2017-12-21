# Scientific Article Summarization using LSTMs
This system is aimed at generating automated summary(abstract) of a scientific article using Deep Learning tools. Specifically, we **use LSTMs over representations of different portions of a scientific article for generating its abstract**. The repository contains all the codes needed for running different modules of our framework.

A detailed proposal of this project can be found here: [PROJECT PROPOSAL LINK](https://drive.google.com/open?id=1TIoWlD0SArTUc9oR1sJDHri1lIKQr8_c)
A descriptive presentation containing the final results can be found here: [PROJECT PRESENTATION LINK](https://drive.google.com/open?id=1GgALEC6UvImVtl9eQYoY389g8ZbiICeg)

## System Overview
![Scientic Article Summarization Overview](https://github.com/ash-shar/Scientific-Article-Summarization-using-LSTMs/blob/master/System-Overview.PNG?raw=true "Title")



## Major Challenge

Scientific articles are too long to be processed for current GPUs using LSTMs. Hence, we need to get to a compressed representation of the paper retaining important information conveyed by the paper, before applying the **sequence-to-sequence mapping** task.

## Dataset Used

LaTeX sources of articles from **arxiv.org** (16,780 articles in total).

## Prerequisites

For using our framework you will need Python 2.7+ with the following modules installed:

- [plasTeX](https://pypi.python.org/pypi/plasTeX/1.0)
- [tensorflow](https://www.tensorflow.org/)
- [nltk](www.nltk.org/)
- [stemming](https://pypi.python.org/pypi/stemming/1.0)

## Running the System

### Step 1: Pre-processing Latex Sources

For parsing latex sources, we make use of the python library [pylatexenc](https://github.com/phfaist/pylatexenc) (source code available in the repository. No need to install separately). We make following modification to this library for effective pre-preprocessing of the articles:

1. Sections and Subsections of articlewere identified and marked
2. Figures, Tables and Mathematical Equationswere replaced by representative tokens
3. Obtained Structure was converted to LSTM input format

For running our pre-processor, use the shell script [preprocess.sh](1-Preprocessing/preprocess.sh). Provide Input Folder (Containing unzipped folders for each paper-downloaded from arxiv.org) and Output Folder (folder where you want the output to be generated). Sample run:
```
$ ./preprocess.sh ../Sample_Data/Papers_Folder/ ../Sample_Data/Output/
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

For generating representations using Para2Vec, use the code [create_embeddings.py](2-Para2Vec/create_embeddings.py). It takes as input 4 command-line arguments: Output Folder (same as the one used in Step 1), creating embeddings for abstract or article ("abs" for abstract, "art" for article), and variation of Para2Vec Model to use ("DM" or "DBOW"). Sample run:

```
python create_embeddings.py ../Sample_Data/Output/ art DBOW
```
It will store the learned representations in [Para2Vec_Models](2-Para2Vec/Para2Vec_Models) folder. Use [test_embeddings.py](2-Para2Vec/test_embeddings.py) for extracting the learned representations. The function *get_embedding(article_fname, para = True, algo = "DM")* returns the learned embedding given a paper_id as input. Ex:

```
get_embedding('1603.04918.txt')
```
### Step 3: Training and Testing the LSTM model
Finally, we train a sequence-to-sequence model with attention mechanism which encodes the Para2Vec representations of different sections of an article and generates its abstract while decoding. The attention mechanism informs the decoder which part of the input sentence it should focus on to generate the next word. 

To train the model, use [run.sh](3-LSTM_Models/UsingPara2Vec/run.sh). Change the inputs, outputs and model parameter inside the script. Sample run:

```
./run.sh
```


## Evaluation

For checking the goodness of the summary generated by our system, we use the **ROUGE** (Recall-Oriented Understudy for Gisting Evaluation) Metrics.

The results and examples generated using different approaches can be found in the presentation, in the root directory of the project.

## References

1. Erkan, Günes, and Dragomir R. Radev. "LexRank: Graph-based lexical centrality as salience in text summarization." Journal of Artificial Intelligence Research 22 (2004): 457-479.

2. [Text Summarization with Tensorflow](https://research.googleblog.com/2016/08/text-summarization-with-tensorflow.html) (Generation of News Headlines) by Peter Liu and Xin Pan 

3. Le, Quoc V., and Tomas Mikolov. "Distributed Representations of Sentences and Documents." ICML. Vol. 14. 2014.

4. Kim, Minsoo, Moirangthem Dennis Singh, and Minho Lee. "Towards Abstraction from Extraction: Multiple Timescale Gated Recurrent Unit for Summarization." arXiv preprint arXiv:1607.00718 (2016).

5. Lin, Chin-Yew. "Rouge: A package for automatic evaluation of summaries." Text summarization branches out: Proceedings of the ACL-04 workshop. Vol. 8. 2004.