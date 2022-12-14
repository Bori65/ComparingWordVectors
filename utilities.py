# -*- coding: utf-8 -*-

import sparknlp
from sparknlp.annotator import *
from pyspark.ml import Pipeline
spark = sparknlp.start(memory="2G")



def euclidean_distances(v1, v2):
    if all(x == 0 for x in v1) or all(x == 0 for x in v2):
        return None
    distance = 0
    for dim1 in v1:
        for dim2 in v2:
            distance += (dim1 - dim2) ** 2
    distance = distance ** (1/2)
    return distance


def cosine_similarity(v1, v2):
    if all(x == 0 for x in v1) or all(x == 0 for x in v2):
        return None
    numerator = 0
    sum1 = 0
    sum2 = 0
    for dim1 in v1:
        for dim2 in v2:
            numerator += (dim1 * dim2)
            sum1 += dim1 ** 2
            sum2 += dim2 ** 2
    denominator = (sum1 ** (1/2)) * (sum2 ** (1/2))
    if denominator == 0:
        return None
    return numerator/denominator

def return_df(text):
    documentAssembler = DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")


    tokenizer = Tokenizer() \
    .setInputCols("document") \
    .setOutputCol("token")


    embeddings = WordEmbeddingsModel.load("//w2v_cc_300d_sk_3.4.1_3.0_1647457801748") \
    .setInputCols(["document", "token"]) \
    .setOutputCol("embeddings")

    pipeline = Pipeline(stages=[documentAssembler, tokenizer, embeddings])

    data = spark.createDataFrame([[text]]).toDF("text")

    model = pipeline.fit(data)

    r = model.transform(data)

    return r.select("embeddings")


def vectors_as_dict(df):
    res = {}
    rows = df.collect()[0].asDict()['embeddings']
    for row in rows:
        res[row.asDict()['metadata']['token']] = row.asDict()['embeddings']
    return res
