# SSL-Data-Bias

This repository contains related code and information for the following paper: <br>
["Don't speak too fast: The impact of data bias on self-supervised speech models"](https://arxiv.org/abs/2110.07957). *ICASSP 2022*

### Usage
#### Related information for the biased dataset generation and settings (3 aspects discussed in the paper) <be>

All the pre-training datasets in the paper are fixed to 100 hours (selected subset from LibriSpeech *train-clean-100* and *train-clean-360*)


#### 1. Gender
Code for generating gender-biased datasets with different male-to-female ratios

* require a metadata .txt file of all audio files in the pool (same format as libri_metadata_100_360.txt)
```
python random_gender.py [-h] [-i INPUT_DATA] -n OUTPUT_NAME [-a AUDIO_EXTENSION] -f FEMALE_RATIO -m MALE_RATIO

options:
  -h, --help            show this help message and exit
  -i INPUT_DATA, --input_data INPUT_DATA
                        Path to your metadata
  -n OUTPUT_NAME, --output_name OUTPUT_NAME
                        name of output folder
  -a AUDIO_EXTENSION, --audio_extension AUDIO_EXTENSION
                        audio file type (.wav / .flac / .mp3 / etc)
  -f FEMALE_RATIO, --female_ratio FEMALE_RATIO
                        female speaker files duration ratio
  -m MALE_RATIO, --male_ratio MALE_RATIO
                        male speaker files duration ratio
```

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
