
from utilities import return_df, vectors_as_dict, euclidean_distances, cosine_similarity
import pandas as pd
import unidecode


class ChainAssocationTask:

    def __init__(self, file, col1, col2):
        data = pd.read_excel(file)
        self.df = pd.DataFrame(data, columns=[col1, col2])
        self.word_pairs = self.df.values
        self.words = " ".join(set([unidecode.unidecode(w) for w in self.word_pairs.flat]))
        self.vectors = vectors_as_dict(return_df(self.words))
        self.out_of_vocabulary = self.number_of_missing_vectors()

    def number_of_missing_vectors(self):
        count = 0
        for vector in self.vectors.values():
            if all(x == 0 for x in vector):
                count += 1
        return count


    def dataframe_of_distances(self):
        data = {"Prime": [], "Response": [], "Euclidean distance": [], "Cosine_similarity": [], "Out of vocabulary": []}
        for word1, word2 in self.word_pairs:
            data["Out of vocabulary"].append(None)
            data["Prime"].append(word1)
            data["Response"].append(word2)
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
        ChAT = ChainAssocationTask(r"..\Sample Data\Chain\Subj1.xlsx", 'Prime', 'Response')
        df = ChAT.dataframe_of_distances()
        ChAT.get_csv_table(r"..\Sample Data\Chain\Subj1_result1.csv", df)
        ChAT.get_excel_table(r"..\Sample Data\Chain\Subj1_result1.xlsx", df)

        ChAT = ChainAssocationTask(r"..\Sample Data\Chain\Subj2.xlsx", 'Prime', 'Response')
        df = ChAT.dataframe_of_distances()
        ChAT.get_csv_table(r"..\Sample Data\Chain\Subj2_result1.csv", df)
        ChAT.get_excel_table(r"..\Sample Data\Chain\Subj2_result1.xlsx", df)
