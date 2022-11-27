
from utilities import return_df, vectors_as_dict, euclidean_distances, cosine_similarity
import pandas as pd
import unidecode


class FluencyTask:

    def __init__(self, file, col1):
        data = pd.read_excel(file)
        self.df = pd.DataFrame(data, columns=[col1])
        self.words_list = list(self.df.values.flat)
        self.words = " ".join(set([unidecode.unidecode(w) for w in self.words_list]))
        self.vectors = vectors_as_dict(return_df(self.words))
        self.out_of_vocabulary = self.number_of_missing_vectors()

    def number_of_missing_vectors(self):
        count = 0
        for vector in self.vectors.values():
            count += all(x == 0 for x in vector)
        return count

    def dataframe_of_distances(self):
        data = {"Response1": [], "Response2": [], "Euclidean distance": [], "Cosine_similarity": [], "Out of vocabulary": []}
        for i, word1 in enumerate(self.words_list[:-1]):
            for word2 in self.words_list[i+1:]:
                data["Out of vocabulary"].append(None)
                data["Response1"].append(word1)
                data["Response2"].append(word2)
                data["Euclidean distance"].append(euclidean_distances(self.vectors[unidecode.unidecode(word1)],
                                                                      self.vectors[unidecode.unidecode(word2)]))
                data["Cosine_similarity"].append(cosine_similarity(self.vectors[unidecode.unidecode(word1)],
                                                                   self.vectors[unidecode.unidecode(word2)]))
        data["Out of vocabulary"][0] = self.out_of_vocabulary
        res_df = pd.DataFrame(data)
        return res_df

    def get_csv_table(self, path, df_distances):
        return df_distances.to_csv(path)

    def get_excel_table(self, path, df_distances):
        return df_distances.to_excel(path)


if __name__ == "__main__":
        FT = FluencyTask(r"..\Sample Data\Fluency\Participant1.xlsx", 'Response')
        df = FT.dataframe_of_distances()
        FT.get_csv_table(r"..\Sample Data\Fluency\Participant1_result.csv", df)
        FT.get_excel_table(r"..\Sample Data\Fluency\Participant1_result.xlsx", df)

        FT = FluencyTask(r"..\Sample Data\Fluency\Participant2.xlsx", 'Response')
        df = FT.dataframe_of_distances()
        FT.get_csv_table(r"..\Sample Data\Fluency\Participant2_result.csv", df)
        FT.get_excel_table(r"..\Sample Data\Fluency\Participant2_result.xlsx", df)
