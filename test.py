import torch
from train import BigramLanguageModel,decode
#testing v0 model
#load

device = 'cuda' if torch.cuda.is_available() else 'cpu'
m = BigramLanguageModel()
m.load_state_dict(torch.load(f="models/tamilgptv0.pth"))

context = torch.zeros((1, 1), dtype=torch.long, device=device)
print(decode(m.generate(context, max_new_tokens=1000)[0].tolist()))
