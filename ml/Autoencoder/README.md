# AutoEncoder for Image Super Resolution:

#### What is Super Image Resolution?

Image super-resolution techniques reconstruct a higher-resolution image or sequence from the observed lower-resolution images.

#### The assests used in the project?

There is a car_image_dataset folder present in Dataset folder where the pretrained weights and car image dataset iis present. The image folder contains the assests for the jupyter notebook

#### What are the Steps used in the project?

1. Import all the neccessary libraries (requirements.txt file is present in the same folder where the notebook resides).
2. Build Encoder Model first. The details are given in the notebook.
3. Build Decoder to complete the full model. The detials about the architecute is given in the notebook.
4. Preprocess the dataset and creating a training routine for the built model to train. (Since the training is computationally high for the given system. I used a pretrained weight instead. It is in the dataset folder.)
5. Predicting and Evaluating the model.

