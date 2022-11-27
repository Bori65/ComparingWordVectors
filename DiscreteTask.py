# -*- coding: utf-8 -*-
from utilities import return_df, vectors_as_dict, euclidean_distances, cosine_similarity
import pandas as pd
import unidecode


class DiscreteTask:

    def __init__(self, file, stimulus, response, condition):
        data = pd.read_csv(file)
        self.df = pd.DataFrame(data, columns=[stimulus, response, condition])
        self.word_triples = self.df.values
        print(self.word_triples)
        self.words = " ".join(set([unidecode.unidecode(w) for w in self.word_triples.flat]))
        self.vectors = vectors_as_dict(return_df(self.words))
        self.out_of_vocabulary = self.number_of_missing_vectors()

    def number_of_missing_vectors(self):
        count = 0
        for vector in self.vectors.values():
            count += all(x == 0 for x in vector)
        return count

    def print_euclidean_distance(self):
        for word1, word2, condition in self.word_triples:
            print("Euclidean distance({}): {}  {} -> {} "
                    .format(condition, word1, word2, euclidean_distances(self.vectors[word1], self.vectors[word2])))

    def print_cosine_similarity(self):
        for word1, word2, condition in self.word_triples:
            print("Cosine similarity({}): {}  {} -> {} "
                  .format(condition, word1, word2, cosine_similarity(self.vectors[word1], self.vectors[word2])))

    def dataframe_of_distances(self):
        data = {"Stimulus": [], "Response": [], "Condition": [], "Euclidean distance": [], "Cosine_similarity": [], "Out of vocabulary": []}

        for word1, word2, condition in self.word_triples:
            data["Out of vocabulary"].append(None)
            data["Stimulus"].append(word1)
            data["Response"].append(word2)
            data["Condition"].append(condition)
            data["Euclidean distance"].append(euclidean_distances(self.vectors[unidecode.unidecode(word1)], self.vectors[unidecode.unidecode(word2)]))
            data["Cosine_similarity"].append(cosine_similarity(self.vectors[unidecode.unidecode(word1)], self.vectors[unidecode.unidecode(word2)]))

        data["Out of vocabulary"][0] = self.out_of_vocabulary
        res_df = pd.DataFrame(data)
        return res_df

    def get_csv_table(self, path, df_distances):
        return df_distances.to_csv(path)

    def get_excel_table(self, path, df_distances):
        return df_distances.to_excel(path)


if __name__ == "__main__":
        DT = DiscreteTask(r"..\Sample Data\Discrete\AK09_AD_A_2021_Jul_20_1336.csv",'Stimulus','Response','Condition')
        df = DT.dataframe_of_distances()
        DT.get_csv_table(r"..\Sample Data\Discrete\AK09_AD_A_2021_Jul_20_1336_result.csv", df)
        DT.get_excel_table(r"..\Sample Data\Discrete\AK09_AD_A_2021_Jul_20_1336_result.xlsx", df)


        DT = DiscreteTask(r"..\Sample Data\Discrete\AK10_AD_A_2021_Jul_22_1336.csv",'Stimulus','Response','Condition')
        df = DT.dataframe_of_distances()
        DT.get_csv_table(r"..\Sample Data\Discrete\AK10_AD_A_2021_Jul_22_1336_result.csv", df)
        DT.get_excel_table(r"..\Sample Data\Discrete\AK10_AD_A_2021_Jul_22_1336_result.xlsx", df)

