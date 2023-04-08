# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 13:59:08 2023

@author: Admin
"""
import torch
import torchvision.transforms as transforms
import random
import matplotlib.pyplot as plt
def generator_data(batch_input,batch_output, p =None):
    if p is None:
        p = {'RHF' : 0.5,
             'RVF' : 0.5,
             'RI' : 0.5}
    # Normalization
    batch_input,batch_output = batch_input/255,batch_output/255
    # def transformations
    transformations_h = transforms.RandomHorizontalFlip(p=1)
    transformations_v = transforms.RandomVerticalFlip(p=1)
    invert_color = transforms.RandomInvert(p=1)
    if random.uniform(0, 1) > p['RHF']:
        batch_input = transformations_h(batch_input)
        batch_output = transformations_h(batch_output)
    if random.uniform(0, 1) > p['RVF']:
        batch_input = transformations_v(batch_input)
        batch_output = transformations_v(batch_output) 
    if random.uniform(0, 1) > p['RI']:
        batch_input = invert_color(batch_input)
        batch_output = invert_color(batch_output)
    
    return batch_input,batch_output



if  __name__ == '__main__':
    noisy1 , noisy2 = torch.load ( r"C:\Users\Admin\Documents\Python Scripts\VISION\data\train_data.pkl")
    res1,res2 = generator_data(noisy1,noisy2)

    fig = plt.figure(figsize=(18, 18))
    ind = 0
    fig.add_subplot(2, 2, 1)
    plt.imshow(noisy1[ind].permute(1,2,0)/255)

    fig.add_subplot(2, 2, 2)
    plt.imshow(noisy2[ind].permute(1,2,0)/255)

    fig.add_subplot(2, 2, 3)
    plt.imshow(res1[ind].permute(1,2,0))

    fig.add_subplot(2, 2, 4)
    plt.imshow(res2[ind].permute(1,2,0))
