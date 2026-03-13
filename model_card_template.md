# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

This model is a binary classifier that predicts whether a person’s income is above or below 50K based on Census Bureau–style features. It was built with scikit-learn’s **RandomForestClassifier** (default hyperparameters, random_state=50 for reproducibility). Categorical inputs are one hot encoded and continuous features are used as-is. After training on the preprocessed data, the model predicts either “<=50K” or “>50K,” and the API returns that label directly.

## Intended Use

The model is intended for educational/demonstrational use as part of a ML DevOps pipeline (training, evaluation, slicing, deployment with FastAPI). It is suitable for illustrating inference APIs and slice-based performance analysis. It is not intended for high-value decisios.

## Training Data

Training uses the census.csv dataset. The data includes features such as age, workclass, education, occupation, relationship, race, sex, capital gain/loss, hours per week, and native country. The target is **salary**, displayed as <=50K or >50K, later binarized. The full dataset is split with an 80/20 train/test split. Only the 80% training portion is used to fit the model and the one hot encoder. No scaling is applied to continuous features.

## Evaluation Data

Evaluation uses the held-out 20% test set from the same census.csv split. This set is processed with the same one hot encoder and label binarizer fitted on the training set (no refitting). Performance is reported on this test set overall and on slices defined by categorical feature values (see slice_output.txt).

## Metrics

The metrics used are precision, recall, and F1 score (beta=1), computed with scikit-learn’s precision_score, recall_score, and fbeta_score with zero_division=1.  

**Overall test-set performance** (representative run): Precision ≈ 0.75, Recall ≈ 0.64, F1 ≈ 0.69. Performance varies by slice - for example, slices with more data (workclass "Private", education "HS-grad") have more stable metrics, while rare slices ("Without-pay", "Preschool") can show very high or unstable precision/recall due to small sample sizes. Detailed per-slice metrics are in slice_output.txt.

## Ethical Considerations

The model uses demographic and employment-related features that can correlate with income and with protected attributes. The dataset is US-centric and may not work on other populations. Use in any non-educational manner (credit, employment, benefits) would require more analysis and human oversight. This implementation is only for pipeline and API demonstration.

## Caveats and Recommendations

- **Data quality:** The census data contains missing or placeholder values ("?"), the pipeline uses the data as provided. For production use, define and document handling of missing values and outliers.
- **Slice performance:** Some slices have very few samples, leading to volatile precision/recall. Rely on overall metrics and well-populated slices when summarizing model quality. Use slice_output.txt to identify underperforming or high-variance subgroups.
- **Reproducibility:** Training and split use fixed random seeds (random_state=50). Retraining with the same code and data should yield the same model and very similar metrics.
- **Deployment:** The model is served via a FastAPI app that loads the saved model and encoder. Ensure the same preprocessing (feature set, one-hot encoding, column order) is used at inference as in training. Consider adding input validation, rate limiting, and monitoring before any production use.
