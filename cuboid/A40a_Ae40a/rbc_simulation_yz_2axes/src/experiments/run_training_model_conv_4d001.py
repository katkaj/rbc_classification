import sys
sys.path.insert(0,'../')

import libs
import libs_dataset
import models.model_conv_4d001.src.model as Modelconv_4d001

from dats_config import *

'''
create dataset with pairs training testing
labels corresponds to class IDs
for details see libs_dataset/cells_dataset.py
'''
dataset = libs_dataset.CellsDataset(training_files, training_labels, testing_files, testing_labels, window_size = 128, classes_count = 2, augmentations_count=100, cols = [14, 15, 17, 18, 20, 21, 23, 24])



#train 100 epochs
epoch_count = 100

#cyclic learning rate cheduler
learning_rates  = [0.001, 0.001, 0.0001, 0.0001, 0.0001, 0.00001, 0.00001]

train = libs.Train(dataset, Modelconv_4d001, batch_size = 256, learning_rates = learning_rates)
train.step_epochs(epoch_count, log_path = "../models/model_conv_4d001")

'''
training result saved into ../models/model_conv_4d001/result

training progress saved into file training.log columns description
epoch               [int]
training_accuracy   [%]
testing_accuracy    [%]
training_loss_mean  [float]
testing_loss_mean   [float]
training_loss_std   [float]
testing_loss_std    [float]

best model is saved into ../models/model_conv_4d001/trained
and results into ../models/model_conv_4d001/result/best.log
'''
