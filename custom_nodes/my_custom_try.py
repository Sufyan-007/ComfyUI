from PIL import Image
import numpy as np
import comfy.utils
import time

# custom_nodes/SubmitConfig.py

class SubmitConfig():
    LABEL = "Submit Config"
    CATEGORY = "Actions"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "trigger": ("EVENT",),
                "title":   ("STRING",),
                "items":   ("LIST",),        # assume you collect items into a Python list
            }
        }

    RETURN_TYPES = ("JSON",)
    FUNCTION = "on_submit"

    def on_submit(self, trigger, title, items):
        # Build and validate the config
        # Call your external function
        # Return the JSON representation (or whatever you need)
        return ()



class MyCustomNode:
    @classmethod
    def INPUT_TYPES(s): 
        return {"required":
                    {}
                }

    RETURN_TYPES = ()
    FUNCTION = "func"

    OUTPUT_NODE = True

    CATEGORY = "custom/try"

    def func(self):
        print("Hello from MyCustomNode!")
        return {}

    @classmethod
    def IS_CHANGED(s, images):
        return time.time()

# custom_nodes/config_models.py
from pydantic import BaseModel
from typing import List, Optional



class TitleInput():
    LABEL = "Title"
    CATEGORY = "Inputs"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "title": ("STRING", {
                    "default": "My Config",
                    "multiline": False
                })
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "get"

    def get(self, title):
        return (title,)

class Item(BaseModel):
    name: str
    value: int
    children: Optional[List["Item"]] = None  # recursive!

    class Config:
        orm_mode = True

Item.model_rebuild()

class FullConfig(BaseModel):
    title: str
    items: List[Item]


NODE_CLASS_MAPPINGS = {
    "MyCustomNode": MyCustomNode,
    "SubmitConfig":SubmitConfig,
    "TitleInput":TitleInput
}
