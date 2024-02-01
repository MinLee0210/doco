import math

def call_parameter(model):
  pytorch_total_params = sum(p.numel() for p in model.parameters())
  trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
  untrainable_params = pytorch_total_params - trainable_params
  print(f'Model {model.__class__.__name__} has {pytorch_total_params} parameters in total\n'\
        f'Trainable parameters: {trainable_params}\nUntrainable parameters: {untrainable_params}')
  return pytorch_total_params