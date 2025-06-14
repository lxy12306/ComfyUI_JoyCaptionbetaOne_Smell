# ComfyUI JoyCaptionbetaOne

本插件为 ComfyUI 的自定义节点，仅包含 JoyCaptionbetaOne 相关功能，**本项目独立拆分自 [lxy12306/ComfyUI_Model_Nodes_Smell](https://github.com/lxy12306/ComfyUI_Model_Nodes_Smell) 源仓库**。

## 目录结构

```
ComfyUI_JoyCaptionbetaOne_Smell/
├── JoyCaption/
│   ├── joycaption_beta_one.py
│   ├── node.py
│   └── json/
│       └── joycaption_beta_one.json
├── Common/
│   ├── common_func.py
│   ├── common_model.py
│   └── image_func.py
├── __init__.py
├── requirements.txt
└── README.md
```

## 安装方法

1. 将本文件夹放入 `ComfyUI/custom_nodes/` 目录下。
2. 安装依赖：
    ```bash
    pip install -r requirements.txt
    pip install git+https://github.com/huggingface/transformers
    ```
3. 下载模型放到合适的模型目录（自定义目录/LLM）。
    - [llama-joycaption-beta-one-hf-llava](https://modelscope.cn/models/fancyfeast/llama-joycaption-beta-one-hf-llava)

## 使用说明

- 启动 ComfyUI 后，相关节点会自动出现在节点面板中。
- 可在 `JoyCaption` 分类下找到对应节点。

该仓库暂不维护，更新在https://github.com/lxy12306/ComfyUI_Model_Nodes_Smell进行更新

