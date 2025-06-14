import os
import shutil
import torch
from PIL import Image
import numpy as np
import cv2

def tensor_to_pil(image_tensor: torch.Tensor, batch_index: int = 0 )-> Image:
    image_tensor = image_tensor[batch_index]
    if image_tensor.shape[0] > 4:
        image_tensor = image_tensor.permute(2, 0, 1)
    i = 255.0 * image_tensor.cpu().numpy()
    if image_tensor.shape[0] == 1:
        img = Image.fromarray(np.clip(i.squeeze(), 0, 255).astype(np.uint8), mode='L')
    elif image_tensor.shape[0] == 3:
        img = Image.fromarray(np.clip(i.transpose(1, 2, 0), 0, 255).astype(np.uint8))
    else:
        raise ValueError(f"输入的张量必须是形状为 [batch, channels, height, width] 的四维张量，{image_tensor.shape} 且通道数应为 1 或 3。")
    return img

def tensor_to_video(image_tensor: torch.Tensor, output_path: str, fps: int = 30):
    batch_size, channels, height, width = image_tensor.shape
    if channels != 3:
        raise ValueError("输入的张量必须具有 3 个通道（RGB）。")
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    for i in range(batch_size):
        frame = image_tensor[i].permute(1, 2, 0).cpu().numpy()
        frame = np.clip(frame * 255.0, 0, 255).astype(np.uint8)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        video_writer.write(frame)
    video_writer.release()
    print(f"视频已保存到 {output_path}")
