
MODEL_TRAINER_BASE_ACCURACY: float = 0.6
MODEL_TRAINER_DIR: str = "model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR: str = "trained_model"
MODEL_TRAINER_MODEL_NAME: str = "finance_estimator"
MODEL_TRAINER_LABEL_INDEXER_DIR: str = "label_indexer"

MODEL_TRAINER_MODEL_METRIC_NAMES = ["f1",
                                    "weightedPrecision",
                                    "weightedRecall",
                                    "weightedTruePositiveRate",
                                    "weightedFalsePositiveRate",
                                    "weightedMeasure",
                                    "truePositiveRateByLabel",
                                    "falsePositiveRateByLabel",
                                    "precisonByLabel",
                                    "recallByLabel",
                                    "fMeasureByLabel"
                                    ]