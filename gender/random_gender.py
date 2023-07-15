import os
import sys
from distutils.dir_util import copy_tree
import shutil
import glob
import random
import argparse
from tqdm import tqdm

ROOT = '/groups/public/LibriSpeech' # path to LibriSpeech
DEST_ROOT = '/groups/yenmeng' # output dataset destination

def get_args():

    parser = argparse.ArgumentParser(
        description='preprocess arguments for any dataset.')

    parser.add_argument('-i', '--input_data', default='libri_metadata_100_360.txt',
                        type=str, help='Path to your metadata', required=False)
    parser.add_argument('-n', '--output_name', type=str, help='name of output folder', required=True)
    parser.add_argument('-a', '--audio_extension', default='.flac', type=str,
                        help='audio file type (.wav / .flac / .mp3 / etc)', required=False)
    parser.add_argument('-f', '--female_ratio', type=float,
                        help='female speaker files duration ratio', required=True)
    parser.add_argument('-m', '--male_ratio', type=float,
                        help='male speaker files duration ratio', required=True)

    args = parser.parse_args()
    return args

def preprocess(file_path):
    male = [line.strip() for line in open(file_path).readlines()[1:] if line.split(',')[-1].strip() == 'M']
    female = [line.strip() for line in open(file_path).readlines()[1:] if line.split(',')[-1].strip() == 'F']
    random.shuffle(male)
    random.shuffle(female)
    return male, female

def get_data(args, male, female):
    duration_f = 0.0
    duration_m = 0.0
    f_ratio = args.female_ratio
    m_ratio = args.male_ratio
    assert f_ratio + m_ratio == 1.0, "the sum should equal to 1"
    data = []
    print('collecting female data...')
    #split,filename,duration,gender
    for i, line in enumerate(female):
        if duration_f < 100 * 60 * 60 * f_ratio:
            duration_f += float(line.split(',')[2])
            data.append(line)
    print('collecting male data...')
    for i, line in enumerate(male):
        if duration_m < 100 * 60 * 60 * m_ratio:
            duration_m += float(line.split(',')[2])
            data.append(line)
    
    print(f'female: {duration_f/60/60}hr')
    print(f'male: {duration_m/60/60}hr')
    print(f'total files: {len(data)}')
    return data

def make_folder(output_path, output_name, data):
    # save to txt for reference
    os.makedirs('./data_txt', exist_ok=True)
    with open(os.path.join('data_txt', output_name+'.txt'), "w") as outfile:
        outfile.write("\n".join(data))

    for line in tqdm(data):
        #split,filename,duration,gender
        split = line.split(',')[0]
        fname = line.split(',')[1]
        srcfile = os.path.join(ROOT, split, fname.split('-')[0], fname.split('-')[1], fname)
        dest = os.path.join(output_path, fname.split('-')[0], fname.split('-')[1])
        os.makedirs(dest, exist_ok=True)
        destfile = os.path.join(dest, fname)
        #print(f'[{i+1}] adding {srcfile}')
        shutil.copy(srcfile, destfile)
        

def main():
    args = get_args()

    file_path = args.input_data  # metadata
    output_name = args.output_name # ex. rand1
    output_path = os.path.join(DEST_ROOT, output_name, 'train-clean-100')
    print(f'[DEST] {output_path}')
    os.makedirs(output_path, exist_ok=True)
    male, female = preprocess(file_path)
    data = get_data(args, male, female)
    make_folder(output_path, output_name, data)

if __name__ == '__main__':
    main()
