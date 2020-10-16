This Class is used to generate Augmented Images of an original dataset that can be used to suplement the original dataset. This also helps in reducing overfitting

The class in gridmask.py takes 6 arguments. The functionality of these arguments are as follows:
num_grid: Size of the grid to be generated in the mask.
fill_val: Value to be filled in the mask
rotate: maximum and minimum angle that the mask will be rotated.
mode: Different mode of masks to be generated.
always_apply: Whether to always apply this augmentation.
p: probability of whether the augmentation is applied to the image

This Augmentation can be used to force the NN model to find other minor features and to generalise the model and prevent overfitting.

This class is created to be used with albumentations using albumentation.Compose