# ComparingWordVectors
This project was created for my bachelor's thesis “Comparing word vectors in favor of lexical semantics”.
This thesis aims to evaluate the semantic similarity between pairs of words. Each word is represented by a vector, the evaluation is based on these vectors’ similarity.</br>
We are using:
* static embeddings (Word2vec)
* and contextual embeddings as well (Slovak BERT)

## Chain association task
In the Chain association task, we compared each pair of words from the associative word chain. In the beginning, we get the vector representation of each word and evaluated the vector distances of these pairs of words. Afterward, we calculated the average of these distances. We also calculated the minimum and the maximum of these.</br>

First, we create an instance of the class ChainAssociationTask, with three parameters:
*	name of an xlsx or csv file
*	name of the first column (“prime”)
*	name of the second column (“response”)</br>
To get the data frame, we call its method dataframe_of_distances().</br>
To create excel file we call the method get_csv_table() or get_excel_table() with two parameters:
*	the filename of the new excel or csv table with the path
*	the before-created data frame</br>
The result will be xlsx file or csv file where in the first and second columns are the pairs of words, in the last two columns are the Euclidean and cosine distances of these word vectors.

## Discrete task
In the discrete task, we evaluated the distances of each pair of word vectors with associative and dissociative meanings. From the Euclidean distances, we calculated the average of these distances of associative meanings and dissociative meanings separately. Then we compared the obtained result.</br>

First, we create an instance of the class DiscreteTask, with four parameters:
*	name of an xlsx or csv file
*	name of the first column (“stimulus”)
*	name of the second column (“response”)
*	name of the third column (“condition”)</br>

To get the data frame, we call its method dataframe_of_distances().</br>
To create excel file we call the method get_csv_table() or get_excel_table() with two parameters:
*	the filename of the new excel or csv table with the path
*	the before-created data frame</br>
The result will be xlsx file or csv file where in the first and second columns are the pairs of words, in the third column are the conditions (associative or dissociative), in the last two columns, are the Euclidean and cosine distances of these word vectors.

## Fluency task
In the fluency task, we calculated the distance between each word vector from a specific category. Then we calculated the average of these results.</br>

First, we create an instance of the class FluencyTask, with two parameters:
*	name of an xlsx or csv file
*	name of the first column (“Response”)</br>
To get the data frame, we call its method dataframe_of_distances().</br>
To create excel file we call the method get_csv_table() or get_excel_table() with two parameters:
•	the filename of the new excel or csv table with the path
•	the before created data frame</br>
The result will be xlsx file or csv file where in the first and second columns are the pairs of words, in the last two columns, are the Euclidean and cosine distances of these word vectors.</br>

