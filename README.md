# SSL-Data-Bias

This repository contains related code and information for the following paper: <br>
["Don't speak too fast: The impact of data bias on self-supervised speech models"](https://arxiv.org/abs/2110.07957). *ICASSP 2022*

### Usage
#### Related information for the biased dataset generation and settings (3 aspects discussed in the paper) <br>
All the pre-training datasets in the paper are fixed to 100 hours (selected subset from LibriSpeech *train-clean-100* and *train-clean-360*)

For each biased aspect, we provide either the metadata for the utterances contained or the code for generating the dataset

#### 1. Gender
require a metadata .txt file of all audio files in the pool

#### 2. Content (perplexity)
metadata for the selected *highest 100 hours perplexity (ppl) dataset* and the *lowest 100 hours perplexity (ppl) dataset*

#### 3. Prosody (speech rate)
metadata for the selected *highest 100 hours words per minute (wpm) dataset* and the *lowest 100 hours words per minute (wpm) dataset*

### References
If you use anything from this repository, please consider citing our paper:

```
@inproceedings{meng2022don,
  title={Don't speak too fast: The impact of data bias on self-supervised speech models},
  author={Meng, Yen and Chou, Yi-Hui and Liu, Andy T and Lee, Hung-yi},
  booktitle={ICASSP 2022-2022 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)},
  pages={3258--3262},
  year={2022},
  organization={IEEE}
}
```
