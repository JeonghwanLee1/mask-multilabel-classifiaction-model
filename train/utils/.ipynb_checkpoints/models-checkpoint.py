from efficientnet_pytorch import EfficientNet
import torch
import torcn.nn as nn

class EffNet_basic(nn.Module):
    def __init__(self, backbone = "efficientnet-b6", num_classes: int = 18):
        super(MyModel, self).__init__()
        backbone_model = EfficientNet.from_pretrained(backbone)
        self.features = backbone_model
        self.avgpool = nn.AdaptiveAvgPool2d((1, 1))
        self.classifier = nn.Sequential(
            nn.Dropout(),
            nn.Linear(1000, 32),
            nn.ReLU(inplace=True),
            nn.Linear(32, num_classes),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = self.features(x)
        x = torch.flatten(x, 1)
        x = self.classifier(x)
        return x
    
