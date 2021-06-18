import os
from torch.utils.data import Dataset

class KittiTrainDataset(Dataset):
    def __init__(self, directory:str, total_sub_directories:int=10, total_odometer_files:int=31):
        self.data_calibration_directory = os.path.join(directory, 'data_calibration', 'sequences')
        self.data_label_directory = os.path.join(directory, 'data_labels', 'dataset', 'sequences')
        self.data_veloydne_directory = os.path.join(directory, 'data_veloydne', 'sequences')
        
        self.total_sub_directories = [f'0{x}' if x < 10 else f'{x}' for x in range(total_sub_directories)]
        self.total_odometer_files = [f'00000{x}' if x < 10 else f'0000{x}' if x < 100 else f'000{x}' if x < 1000 else f'00{x}' if x < 10000 else f'0{x}' if x < 100000 else f'{x}' for x in range(total_odometer_files)]
    
    def __getitem__(self, index:int):
        times_file = os.path.join(self.data_calibration_directory, self.total_sub_directories[index], 'times.txt')
        calib_file = os.path.join(self.data_calibration_directory, self.total_sub_directories[index], 'calib.txt')
        
        label_files = [os.path.join(self.data_label_directory, self.total_sub_directories[index], 'labels', i + '.label') for i in self.total_odometer_files]
        
        poses_file = os.path.join(self.data_label_directory, self.total_sub_directories[index], 'poses.txt')
        
        veloydne_file = [os.path.join(self.data_veloydne_directory, self.total_sub_directories[index], 'veloydne', i + '.bin') for i in self.total_odometer_files]
        
        return times_file, calib_file, poses_file, label_files, veloydne_file
    
    def __len__(self):
        return len(self.total_sub_directories)