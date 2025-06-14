# 见 README.md 说明
# JoyCaption 节点主入口
from .joycaption_beta_one import *

NODE_CLASS_MAPPINGS = {
    "SmellLoadJoyCaptionBetaOne": JoyCaptionBetaOne,
    "SmellJoyCaptionBetaOneProcessor": JoyCaptionBetaOneProcessor,
    "JoyCaptionBetaOneExtraOptions": JoyCaptionBetaOneExtraOptions,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SmellLoadJoyCaptionBetaOne": "🌱Smell Load JoyCaptionBetaOne",
    "SmellJoyCaptionBetaOneProcessor": "🌱Smell JoyCaptionBetaOne Processor",
    "JoyCaptionBetaOneExtraOptions": "🌱Smell JoyCaptionBetaOne Extra Options",
}
