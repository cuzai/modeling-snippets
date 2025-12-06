import inspect
from typing import Any

import torch
from transformers import AutoModel, AutoProcessor


class ReverseEngineerModel:
    def __init__(self) -> None:
        self.device = "cuda"
        model_nm: str = "google/gemma-3-27b-it"
        self.model: torch.nn.Module = AutoModel.from_pretrained(model_nm, dtype="bfloat16")
        self.processor: AutoProcessor = AutoProcessor.from_pretrained(model_nm, use_fast=True)
        self._save_model_summary()

    def _save_model_summary(self) -> None:
        # Save model's brief architecture
        with open("./summary/model_architecture", "w") as f:
            f.write(str(self.model))

        # Save model's parameter count
        total_params: int = sum(p.numel() for p in self.model.parameters())
        trainable_params: int = sum(p.numel() for p in self.model.parameters() if p.requires_grad)

        with open("./summary/parameter_count", "w") as f:
            f.write(f"Total parameters: {total_params:,}\n")
            f.write(f"Trainable parameters: {trainable_params:,}\n")

    def _save_source_code(self, module_nm: str) -> None:
        module: torch.nn.Module = getattr(self.model, module_nm) if module_nm else self.model
        module_nm = module_nm if module_nm else "Model"

        with open(f"./source_code/{module_nm}.py", "w") as f:
            if hasattr(module, "forward"):
                f.write(inspect.getsource(module.__init__))
                f.write("\n\n")
                f.write(inspect.getsource(module.forward))
            else:
                f.write(inspect.getsource(module))

    def _hook(
        self_, module: torch.nn.Module, input_args: tuple, input_kwargs: dict[str, Any], outputs: torch.Tensor
    ) -> None:
        self: torch.nn.Module = self_.model
        self

        #################################################################################################
        # 1. Copy default input arguments from the module's forward method (Make sure to remove commas) #
        #################################################################################################

        ####################################################
        # 2. Check kwargs inputs (DO NOT REMOVE THIS CODE) #
        code_to_copy: str = ""
        for k in input_kwargs.keys():
            code_to_copy += f"{k} = kwargs['{k}']\n"
        print("#" * 50)
        print(code_to_copy)
        print("#" * 50)
        ####################################################

        ##########################################################
        # 3. HARD CODE the input_kwargs from `code_to_copy` here #
        ##########################################################

        ##################################
        # 4. Copy source code to analyze #
        ##################################

    def _get_inputs(self):
        # Prepare inputs
        # inputs = self.processor(texts=[text], images=[image], return_tensors="pt").
        # return inputs
        pass

    def __call__(self) -> None:
        # Save source code
        self._save_source_code(module_nm="vision_tower")

        # Register hooks
        self.model.vision_tower.register_forward_hook(self._hook, with_kwargs=True)

        # Execute the model
        inputs = self._get_inputs()
        self.model.to(self.device)(**inputs.to(self.device))


if __name__ == "__main__":
    reverse_engineer_model = ReverseEngineerModel()
    reverse_engineer_model()
