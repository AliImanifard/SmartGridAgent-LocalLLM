from .llms import GPT4AllClient

# import os
# os.environ['VULKAN_IMPLEMENTATION'] = 'C:\\path\\to\\vulkan.dll'
# os.environ['VULKAN_BACKEND'] = '1'
# os.environ["LLAMA_CONTEXT_USE_VULKAN"] = "1"  # Use Vulkan for GPU acceleration

class PromptInjection:
    def __init__(self, gpt4all_client=None):
        self.gpt4all_client = gpt4all_client


    def query_gpt4all_evaluation(self, message: list, injection_prompt=None, verbose=False):
        """ If injection_prompt is None, then it is a normal query """
        regulated_response = list()
        counter = 0
        for msg in message:
            counter += 1
            if verbose:
                print(f"\nQuerying the {counter}th message {msg}")
            try:
                if injection_prompt is None:
                    response = self.gpt4all_client.query_with_pre_prompt(msg).strip()
                else:
                    response = self.gpt4all_client.query_with_pre_prompt(msg + injection_prompt).strip()

                if verbose:
                    print(f"response: {response}")

                response_result = response.split("#")[0].strip()

                if response_result not in ["yes", "no"]:
                    regulated_response.append("invalid")
                else:
                    regulated_response.append(response_result)
            except Exception as e:
                print(e)
                regulated_response.append("invalid")

        return regulated_response
