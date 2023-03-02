# python script to prepare data, writes the txt files containing input and label path that are necessary for yolor 

import argparse
import sys
import glob
import os

def prep_data(train_directory, valid_directory, test_directory):
    
    file_train = open("data/train.txt", "w")
    file_valid = open("data/valid.txt", "w")
    file_test = open("data/test.txt", "w")
    
    for image in sorted(os.listdir(train_directory)):
        if image.endswith((".JPG", ".jpg", ".PNG", ".png")):
            file_train.write(train_directory + "/" + image + "\n")
            
    for image in sorted(os.listdir(valid_directory)):
        if image.endswith((".JPG", ".jpg", ".PNG", ".png")):
            file_valid.write(valid_directory + "/" + image + "\n")
        
    for image in sorted(os.listdir(test_directory)):
        if image.endswith((".JPG", ".jpg", ".PNG", ".png")):
            file_test.write(test_directory + "/" + image + "\n")
    
    file_train.close()
    file_valid.close()
    file_test.close()
    
        
def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('--train-dir', type=str, 
                        help='path of folder containing the training images',
                        default='data/ISIC16_3B_Train_Lesion')
    parser.add_argument('--valid-dir', type=str,
                        help='path of folder containing the validation images',
                        default='data/ISIC16_3B_Test_Lesion')
    parser.add_argument('--test-dir', type=str,
                        help='path of folder containing the test images',
                        default='data/ISIC16_3B_Test_Lesion')       
    parsed_args = parser.parse_args(args)
    return parsed_args

def main(args):
    args = parse_args(args)
    prep_data(train_directory = args.train_dir, valid_directory = args.valid_dir, test_directory = args.test_dir)
if __name__ == '__main__':
    main(sys.argv[1:])
    
    
    