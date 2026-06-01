import torch
import torch.nn as nn
import torch.optim as optim

class PriorityPredictor(nn.Module):
    def __init__(self, input_dim: int, hidden_dim: int, output_dim: int):
        super(PriorityPredictor, self).__init__()
        self.layer1 = nn.Linear(input_dim, hidden_dim)
        self.relu = nn.ReLU()
        self.layer2 = nn.Linear(hidden_dim, output_dim)
        self.softmax = nn.Softmax(dim=1)

    def forward(self, x):
        x = self.layer1(x)
        x = self.relu(x)
        x = self.layer2(x)
        return self.softmax(x)

class PriorityModelManager:
    def __init__(self):
        self.model = PriorityPredictor(input_dim=128, hidden_dim=64, output_dim=4)
        self.optimizer = optim.Adam(self.model.parameters(), lr=0.001)
        self.criterion = nn.CrossEntropyLoss()

    def train_step(self, X: torch.Tensor, y: torch.Tensor):
        self.model.train()
        self.optimizer.zero_grad()
        outputs = self.model(X)
        loss = self.criterion(outputs, y)
        loss.backward()
        self.optimizer.step()
        return loss.item()

    def predict(self, X: torch.Tensor):
        self.model.eval()
        with torch.no_grad():
            outputs = self.model(X)
            return torch.argmax(outputs, dim=1)
