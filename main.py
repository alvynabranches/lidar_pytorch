from dataset import KittiTrainDataset

directory = '/kitty_dataset'
data = KittiTrainDataset(directory)

print(f'root {directory=}')
for d in data[0]:
    [print(e) for e in d] if type(d) is list else print(d)