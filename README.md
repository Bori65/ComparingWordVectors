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
In the fluency task, we calculated the Euclidean distance and cosine similarity between pairs of words in a dataset and categorizes them as associative or dissociative based on their categories.</br>

First, we create an instance of the class FluencyTask with the path to the CSV file:
*	name of an csv file
	
To get the data frame, we call its method dataframe_of_distances().</br>

Save the results to an Excel file::
*	the filename of the new excel or csv table with the path
*	the before created data frame</br>

The result will be xlsx file file where in the first and second columns are the pairs of words, in the last two columns, are the Euclidean and cosine distances of these word vectors.</br>

# Generate Training Data 

This script provides a class called GenerateTrainingData for generating word vectors and saving them to a CSV file.
Define an instance of the GenerateTrainingData class with the following parameters:
*	GTD = GenerateTrainingData(file, col1, col2)
*	file (string): The file path of the Excel file containing word-category data.
*	col1 (string): The name of the column containing the words.
*	col2 (string): The name of the column containing the corresponding categories.

Call the save_word_vectors_to_csv method to generate and save the word vectors to a CSV file:
*	GTD.save_word_vectors_to_csv(path)

# Generate Test Data
This script provides a class called GenerateTestData for generating word vectors from test data and saving them to a CSV file.

Define an instance of the GenerateTestData class with the following parameters:
*	GTD = GenerateTestData(file, col1, col2, condition)
*	file (string): The file path of the CSV file containing test data.
*	col1 (string): The name of the column ("Stimulus") containing the first set of words.
*	col2 (string): The name of the column ("Response") containing the second set of words.
*	condition (string): The name of the column containing the condition (associated/dissociated).

Call the save_word_vectors_to_csv method to generate and save the word vectors to a CSV file:
*	GTD.save_word_vectors_to_csv(path)


