# Sentiment and Tone Analysis Program

## Overview

This Python program contains two independent text-analysis sections designed to run in Google Colab:

1. **Sentiment Analysis** - uses TextBlob to classify 10 sentences as positive, neutral, or negative.
2. **Tone Analysis Challenge** - counts happy and sad words using NLTK's Opinion Lexicon and determines the overall tone of one sentence.

## Requirements

The program requires Python 3 and the following libraries:

- `textblob`
- `nltk`

The import cell installs these libraries in Google Colab and downloads the `opinion_lexicon` dataset.

## Running the Program in Google Colab

Place the code in three separate Colab cells and run them in this order:

1. **Import cell**
2. **Activity cell**
3. **Challenge cell**

The import cell must be run before either program section. The activity and challenge cells can then be run independently.

## Sentiment Analysis

The sentiment-analysis section asks the user to enter 10 sentences. Each sentence is passed to TextBlob, which calculates a polarity score from `-1` to `1`.

| Polarity | Classification |
| --- | --- |
| Less than `0` | Negative |
| Equal to `0` | Neutral |
| Greater than `0` | Positive |

After every entry, the program displays its classification and polarity score. After all 10 sentences have been processed, it displays the total number of positive, neutral, and negative sentences.

Example input:

```text
I am very happy and excited today.
```

## Tone Analysis Challenge

The challenge section asks the user to enter one sentence. It extracts the words from the sentence, converts them to lowercase, and compares them with two lists from NLTK's public Opinion Lexicon:

- Positive words are treated as happy words.
- Negative words are treated as sad words.

The tone is determined using the following rules:

| Comparison | Tone |
| --- | --- |
| Happy count is greater than sad count | Positive |
| Sad count is greater than happy count | Negative |
| Both counts are equal | Neutral |

The program displays the number of happy words, the number of sad words, and the resulting tone.

Example input:

```text
I feel happy and excited, but my friend feels sad.
```

## Functions

### `extract_words(sentence)`

Converts a sentence to lowercase and extracts words while ignoring punctuation.

### `number_happy(sentence)`

Returns the number of extracted words found in the positive-word dataset.

### `number_sad(sentence)`

Returns the number of extracted words found in the negative-word dataset.

## Notes and Limitations

- The program analyzes English text.
- TextBlob assigns sentiment using its built-in language model, so a sentence's classification may differ from a person's interpretation.
- The challenge counts individual words and does not fully understand context, sarcasm, or negation. For example, it may count the word `happy` in `not happy` as a happy word.
- Repeated emotional words are counted each time they appear.
- Words absent from the Opinion Lexicon do not affect the happy or sad totals.
