# Cryptif.ai

## A progressive Flask web app for decryption using cutting edge deep learning techniques.

A personal project for me to learn more about machine learning, handling noisy data and cryptanalysis

# Functionality

#### format text page, allows users to handle large strings and format them

- removing punctuation
- white space
- lower case
- full format

#### Cryptanalysis page has a modern user friendly front end which allows users to visualise every characteristic of the page

- Frequency comparison bar chart to english language
- index of coincidence comparison bar chart
- chi squared score of cipher text for:
  - monogram
  - bigram
  - trigram
- bhattarayya score of cipher text for:
  - monogram
  - bigram
  - trigram

#### Encryption page

- encrypt several classical cipher types using reformatted pycipher module

#### Decryption page

- decrypt several classical cipher types using reformatted pycipher module

#### AI page

- Implemented KNN model to calculate encryption type

#### Keyless decryption page

- implemented statistical model to calculate most probable key for monoalphabetic ciphers
- implemented statistical model to calculate most probable key length and key for polyalphabetic ciphers
