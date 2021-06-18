from dataset import KittiTrainDataset

data = KittiTrainDataset('/kitt_dataset')
for d in data[0]:
    print(d)