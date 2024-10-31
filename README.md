# Topic Modeling of Twitter Data on the 2024 US Election

## Overview
This project focuses on performing topic modeling on recent Twitter data related to the 2024 US election. By leveraging pretrained large language models (LLMs) and advanced techniques, we aim to identify and analyze trending topics while contextualizing them within public sentiment.

## Requirements
- Python 3.x
- Libraries:
  - `transformers`
  - `keybert`
  - `bertopic`
  - `llama_cpp`
```
## Setup
1. **Download Pretrained LLMs**: 
   - Download the following files from Hugging Face:
     - `OpenHermes-2.5-Mistral-7B-GGUF`
     - `dolphin-2.7-mixtral-8x7b-GGUF`
   
   These files contain the pretrained models necessary for topic modeling.

2. **Load the Quantized LLM**: 
   - Use the `llama_cpp` library to load the quantized LLMs, which reduces the computational requirements and facilitates efficient processing.

3. **Models Used**:
   - **KeyBERT**: Fast keyword extraction model for identifying relevant keywords from the data.
   - **LlamaCPP**: Utilizes the quantized LLM to generate contextually relevant responses based on the input data.
```
## Process
1. Segment the dataset into three categories based on sentiment analysis.
2. Define prompts for the LLMs to generate responses using placeholders for documents and keywords.
3. Train the BERTopic model to identify topics and display the results, including unique IDs and top words for each topic.

## Results
The output will consist of identified topics with corresponding unique IDs and the top descriptive words, providing insights into public sentiment and discourse related to the 2024 US election.

## License
This project is licensed under the MIT License. See the LICENSE file for more information.
