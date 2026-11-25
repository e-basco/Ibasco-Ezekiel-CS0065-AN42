
# Laboratory Activity 2: Sentiment Analysis

This project contains a Python solution for Laboratory Activity 2. It is designed to run in Google Colab and includes the required sentiment-analysis activity and the challenge as separate cells.

## Requirements

The notebook uses the following Python libraries:

- `textblob` for polarity-based sentiment analysis
- `nltk` for the public Opinion Lexicon dataset
- `re`, from the Python standard library, for extracting words from sentences

The import cell installs the external libraries automatically.

## How to Run in Google Colab

1. Open [Google Colab](https://colab.research.google.com/).
2. Create a new notebook.
3. Add three code cells.
4. Copy the supplied code into the cells in this order:
   1. Import cell
   2. Activity cell
   3. Challenge cell
5. Run the import cell first and wait for it to finish.
6. Run the activity cell and enter 10 sentences when prompted.
7. Run the challenge cell and enter one sentence when prompted.
8. Take screenshots of the actual results produced by Google Colab.

## Import Cell

The import cell performs the following tasks:

- Installs TextBlob and NLTK.
- Imports the required modules.
- Downloads NLTK's public Opinion Lexicon dataset.

This cell must be run before either of the program cells.

## Activity: TextBlob Sentiment Analysis

The activity asks the user to enter 10 sentences. Each sentence is analyzed using TextBlob's polarity score.

The classifications are:

- Polarity less than `0`: Negative
- Polarity equal to `0`: Neutral
- Polarity greater than `0`: Positive

The program counts each classification and prints a summary after all 10 sentences have been entered.

### Suggested Activity Inputs

Enter these sentences one at a time:

1. `I am very happy and excited today.`
2. `This is the best day of my life.`
3. `The movie was wonderful and enjoyable.`
4. `I love spending time with my family.`
5. `The food tastes delicious.`
6. `I am sad and disappointed.`
7. `This experience was terrible.`
8. `I hate waiting for a long time.`
9. `The book is on the table.`
10. `Today is Wednesday.`

TextBlob determines the final classification, so results depend on the polarity assigned by the library.

## Challenge: Happy and Sad Word Analysis

The challenge uses NLTK's Opinion Lexicon as a public dataset of positive and negative words.

The program:

1. Converts the sentence to lowercase.
2. Removes punctuation and extracts individual words.
3. Counts words found in the positive-word dataset.
4. Counts words found in the negative-word dataset.
5. Compares the two totals.

The tone is classified as:

- Positive when the happy-word count is higher.
- Negative when the sad-word count is higher.
- Neutral when both counts are equal.

### Suggested Challenge Inputs

Positive test:

```text
I feel happy, wonderful, and excited.
```

Negative test:

```text
I feel sad, terrible, and lonely.
```

Neutral test:

```text
The book is on the table.
```

Mixed test:

```text
I am happy and excited, but my friend feels sad and lonely.
```

## Important Notes

- Internet access must be enabled when running the import cell because Colab needs to install the libraries and download the Opinion Lexicon dataset.
- Run the cells in order to avoid missing-import or missing-dataset errors.
- The submitted screenshots should show real program execution; this documentation does not include simulated output.
- The challenge counts exact dataset matches. A related word may not be counted if its particular form is absent from the lexicon.

## Reference Dataset

The challenge uses the NLTK Opinion Lexicon, a collection of English positive and negative opinion words maintained as part of the NLTK data packages.
