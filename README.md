# Geography Question Answering Framework

This project is a Python-based framework designed for answering questions using geographical data. The framework evaluates the quality of answers using the following metrics: Grammar, Lexical Diversity, Phraseology, Matrix-based Phraseology, Vocabulary, Cohesion, and Convention.

## Installation

First, ensure that you have Streamlit installed. You can install it via pip:
```
pip install streamlit
```

## Usage

### Step 1: Set Up OpenAI API Key

Create an OpenAI API key by following the instructions here: [link](https://www.howtogeek.com/885918/how-to-get-an-openai-api-key/). Once you have the API key, use it in the `set_openai_api_key()` function in `model.py`.

### Step 2: Run the Application

Run the Streamlit application using the following command:
```
streamlit run streamlit_ui.py
```

Once the application is running, you will receive a localhost endpoint in your command line or terminal. Open this endpoint in your web browser to access and interact with the user interface.

## Results

![Screenshot](https://github.com/BatMrE/Answer-evaluation-and-correction/assets/48859022/3ea27f3b-573b-4af6-a124-ece6ac917716)


### Evaluation

You can find the fine-tuned model evaluation code in following notebooks:

[gen_model_eval.ipynb](https://github.com/BatMrE/Answer-evaluation-and-correction/blob/master/gen_model_eval.ipynb)

[GPT_BLOOM_eval.ipynb](https://github.com/BatMrE/Answer-evaluation-and-correction/blob/master/GPT_BLOOM_eval.ipynb)

Fine-tuned models can be downloaded from the following links:

[BLOOM](https://drive.google.com/drive/folders/1utL7Nz-uPcIUrGVYb01lkMEgb-DQuRQ2?usp=sharing)

[GPT](https://drive.google.com/drive/folders/1YwRBPBSyWQfbWbSvhwLEmH4ih1z_K8O3?usp=sharing)

[XLNet](https://drive.google.com/drive/folders/1nPHcBpM6GYWpKgb3q4aej-6D-V4H4K3j?usp=sharing)

[T5-base](https://drive.google.com/drive/folders/1SDl3w1knPVN3wcMt6O3JDra_Mb0884g8?usp=sharing)

[Flan-T5](https://drive.google.com/drive/folders/1N-WQyz1P9VZ3IencQyZxOEnCZ7X5RCYu?usp=sharing)

