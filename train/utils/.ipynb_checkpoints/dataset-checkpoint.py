from torch.utils.data import Dataset, DataLoader
from PIL import Image
from torchvision import transforms, datasets
from torchvision.transforms import Resize, ToTensor, Normalize

def get_label(path):
    label = 0 
    splitted = path.split('/')
    dr = splitted[-2]
    name = splitted[-1]
    if 'incorrect' in name:
        base = 6
    elif 'mask' in name:
        base = 0
    elif 'normal' in name:
        base = 12
    else:
        print("error : ",path)
        return -1
    
    label+=base
    
    if 'female' in dr:
        label+=3
    else:
        label+=0
    
    age = int(dr.split('_')[-1])
    if age<30:
        label+=0
    elif age<60:
        label+=1
    else:
        label+=2
    return label

def get_labels(path):
    splitted = path.split('/')
    dr = splitted[-2]
    name = splitted[-1]
    if 'incorrect' in name:
        masked_label = 1
    elif 'mask' in name:
        masked_label = 0
    elif 'normal' in name:
        masked_label = 2
    else:
        print(f"error : {f}")
        return -1
    
    if 'female' in dr:
        gender_label = 1
    else:
        gender_label = 0 
    
    age = int(dr.split('_')[-1])
    if age<30:
        age_label=0
    elif age<60:
        age_label=1
    else:
        age_label=2
    
    return masked_label, gender_label, age_label

def get_labels_exact(path):
    splitted = path.split('/')
    dr = splitted[-2]
    name = splitted[-1]
    if 'incorrect' in name:
        masked_label = 1
    elif 'mask' in name:
        masked_label = 0
    elif 'normal' in name:
        masked_label = 2
    else:
        print(f"error : {f}")
        return -1
    
    
    if 'female' in dr:
        gender_label = 1
    else:
        gender_label = 0 
    
    age = int(dr.split('_')[-1])
    if age<30:
        age_label=0
    elif age<60:
        age_label=1
    else:
        age_label=2
    
    return masked_label, gender_label, age    

def default_transform():
    transform = transforms.Compose([
                                    #transforms.CenterCrop((450,225)),
                                    transforms.Resize((224, 224)),
                                    transforms.ToTensor(),
                                    transforms.Normalize(mean=[0.56019358, 0.52410121, 0.501457],
                                                         std=[0.23318603, 0.24300033, 0.24567522]),
                                ])
    return transform

class TestDataset(Dataset):
    def __init__(self, img_paths, transform):
        self.img_paths = img_paths
        self.transform = transform
    
    def __getitem__(self, index):
        f = self.img_paths[index]
        image = Image.open(f)
        
        if self.transform:
            image = self.transform(image)
        return image
        
    def __len__(self):
        return len(self.img_paths)

class MaskTestDataset(Dataset):
    def __init__(self, data_list, transform):
        self.data_list = data_list
        self.transform = transform

    def __getitem__(self, idx):
        image_path = self.data_list[idx]
        label = get_label(image_path)
        img = Image.open(image_path)
        img = self.transform(img)
        return img, label
 
    def __len__(self):
        return len(self.data_list)

    
class MaskTrainDataset(Dataset):
    def __init__(self, data_list, transform):
        """
        data_list: (file_path, augmentation_choice)라는 튜플로 이루어진 리스트
        augmentation_choice는 길이가 5 이하이고, 각 원소는 0에서 4 이하의 정수로 이루어진 튜플 또는 iterable object
        """
        self.data_list = data_list
        self.default_transform = transform
        # 아래의 transform을 augmentation_choice에 따라 적용함
        self.transform = [
            #transforms.Grayscale(3),
            transforms.RandomHorizontalFlip(1),
            transforms.CenterCrop((450,225)),
            transforms.RandomRotation(5),
            transforms.RandomHorizontalFlip(0),
            transforms.RandomHorizontalFlip(0),
            
        ]
        
    def __getitem__(self, idx):
        image_path = self.data_list[idx][0]
        label = get_label(image_path)
        img = Image.open(image_path)
        for i in self.data_list[idx][1]:
            img = self.transform[i](img)
        img = self.default_transform(img)
        return img, label
    
    def __len__(self):
        return len(self.data_list)

        