import os
import random
import shutil


def train_test_split(dataset_path, output_path, split_ratio, seed=250):
    """Builds the train and test image datasets for all image categories given a split ratio"""
    img_categories = os.listdir(dataset_path)  # all the image categories
    if os.path.exists(output_path):
        print('Dataset already exists at the given path')
        exit()  # dataset already built
    else:
        os.mkdir(output_path)
        os.mkdir(output_path + '/train')
        os.mkdir(output_path + '/test')

    # for every image category in the dataset build train and test folders with images in them a/c to split_ratio
    print('Splitting dataset into train and test sets: ')
    for img_category in img_categories:
        print('.', end='')
        # list all the images for this category
        imgs = os.listdir(dataset_path + '/' + img_category)
        # sort and shuffle images randomly
        imgs.sort()
        random.seed(seed)
        random.shuffle(imgs)
        # split the imgs into two halves train and test
        train_split = imgs[:int(split_ratio * len(imgs))]
        test_split = imgs[int(split_ratio * len(imgs)):]

        # built the train set and copy images
        if not os.path.exists(os.path.join(output_path, 'train', img_category)):
            os.mkdir(os.path.join(output_path, 'train', img_category))
        for img in train_split:
            source = os.path.join(dataset_path, img_category, img)
            dest = os.path.join(output_path, 'train', img_category, img)
            shutil.copy(source, dest)

        # built the test set and copy images
        if not os.path.exists(os.path.join(output_path, 'test', img_category)):
            os.mkdir(os.path.join(output_path, 'test', img_category))
        for img in test_split:
            source = os.path.join(dataset_path, img_category, img)
            dest = os.path.join(output_path, 'test', img_category, img)
            shutil.copy(source, dest)
    print('\nSuccess!!')


train_test_split('./Data/kash_dataset_final/items_no_split', './Data/kash_dataset_final/kash_items', 0.83)

