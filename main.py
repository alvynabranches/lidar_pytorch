from dataset import KittiTrainDataset

directory = '/kitty_dataset'
data = KittiTrainDataset(directory)

print(f'root {directory=}')

for d in data:
    for dt in d:
        [print(e) for e in dt] if type(dt) is list else print(dt)
    print()
    print()
    print()