from gpt4all import GPT4All

import os
# os.environ['VULKAN_IMPLEMENTATION'] = 'C:\\path\\to\\vulkan.dll'
#os.environ['VULKAN_BACKEND'] = '1'
#os.environ["LLAMA_CONTEXT_USE_VULKAN"] = "1"  # Use Vulkan for GPU acceleration


from gpt4all import GPT4All

print(GPT4All.list_gpus())  # output: ['kompute:Radeon RX 580 Series']


class GPT4AllClient:
    def __init__(self, model_path: str):
        self.model = GPT4All(model_path, device='amd')
        self.pre_prompt = list()

    @staticmethod
    def prompt_read(file_path: str):
        """Read the content from the file and return as a list of messages."""
        with open(file_path, "r") as file:
            content = file.read().strip().split("+-+-+-+-+")
        content = [item.strip() for item in content]
        messages = [{"role": "system", "content": content[0]}]
        for i in range(1, len(content)):
            if i % 2 == 1:
                messages.append({"role": "user", "content": content[i]})
            else:
                messages.append({"role": "assistant", "content": content[i]})
        return messages

    def set_pre_prompt(self, pre_prompt: list):
        self.pre_prompt = pre_prompt

    def query_with_pre_prompt(self, message: str):
        query_msg = self.pre_prompt + [{"role": "user", "content": message}]
        prompt = ""
        for msg in query_msg:
            prompt += msg["content"] + "\n"
        with self.model.chat_session():
            response = self.model.generate(prompt)
        return response.strip()

    def query_without_pre_prompt(self, message: str):
        with self.model.chat_session():
            response = self.model.generate(message)
        return response.strip()
