from efficientnet_pytorch import EfficientNet
import torch
import torch.nn as nn

class EffNet_basic(nn.Module):
    def __init__(self, backbone = "efficientnet-b0", num_classes = (3,2,7)):
        super(EffNet_basic, self).__init__()
        backbone_model = EfficientNet.from_pretrained(backbone)
        self.features = backbone_model
        self.avgpool = nn.AdaptiveAvgPool2d((1, 1))
        self.classifier1 = nn.Sequential(nn.Dropout(),nn.Linear(1000,3))
        self.classifier2 = nn.Sequential(nn.Dropout(),nn.Linear(1000,2))
        self.classifier3 = nn.Sequential(nn.Dropout(),nn.Linear(1000,7))
        
        self.classifier = nn.Sequential(
            nn.Dropout(),
            nn.Linear(1000,3)
#             nn.ReLU(inplace=True),
#             nn.Linear(32, num_classes),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = self.features(x)
        x = torch.flatten(x, 1)
        x1 = self.classifier1(x)
        x2 = self.classifier2(x)
        x3 = self.classifier3(x)
        return x1,x2,x3
    
