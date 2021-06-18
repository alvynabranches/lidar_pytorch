# Lidar PyTorch

## Kitty Odometer Dataset

1. The data needs to be preprocessed first.
2. The labelled semantic dataset will be shared and the car class needs to be extracted from the Lidar point cloud (as a preprocessing step).
3. Once the data is preprocessed, it is ready to be trained. The training step involves implementation of a variational Autoencoder that takes as input the preprocessed Lidar scans (partial point cloud of cars) and trains the model such that at the time of inference, it is able to predict the actual shape of the car.
4. It involves an intermediate step as well which is basically training the VAE with Shapenet dataset.
5. The training architecture and other details that need to be followed are given in this paper
6. After training, testing(inference) needs to be done and a few parameters(such as chamfer distance, inference time, etc) need to be evaluated
