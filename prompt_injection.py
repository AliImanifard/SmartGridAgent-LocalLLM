from credentials import OPENAI_API_KEY
# from SGLLM.llms import OpenAIClient
from SGLLM.llms import GPT4AllClient

from SGLLM.attacks import PromptInjection
from SGLLM.utilities import read_json_to_dict, binary_classification_result_evaluation, save_dictionary_to_json # You can access it via the source.

import os

# os.environ['VULKAN_IMPLEMENTATION'] = 'C:\\path\\to\\vulkan.dll'
# os.environ['VULKAN_BACKEND'] = '1'
# os.environ["LLAMA_CONTEXT_USE_VULKAN"] = "1"  # Use Vulkan for GPU acceleration

# GPT4_MODEL = "gpt-4-turbo"
# GPT3_MODEL = "gpt-3.5-turbo"
LLAMA3_MODEL_PATH = "C:\\Path\\to\\gguf\\file\\Meta-Llama-3-8B-Instruct.Q4_0.gguf"
LLAMA3_MODEL_NAME = "llama-3"

LLAMA3_1_MODEL_PATH = "C:\\Path\\to\\gguf\\file\\Meta-Llama-3.1-8B-Instruct-128k-Q4_0.gguf"
LLAMA3_1_MODEL_NAME = "llama-3.1"

LLAMA3_2_MODEL_PATH = "C:\\Path\\to\\gguf\\file\\Meta-Llama-3.2-3B-Instruct-Q4_0.gguf"
LLAMA3_2_MODEL_NAME = "llama-3.2"

QWEN2_MODEL_PATH = "C:\\Path\\to\\gguf\\file\\qwen2-1_5b-instruct-q4_0.gguf"
QWEN2_MODEL_NAME = "qwen2"

MISTRAL_NEMO_MODEL_PATH = "C:\\Path\\to\\gguf\\file\\Mistral-Nemo-Instruct-2407.Q4_0.gguf"
MISTRAL_NEMO_NAME = "mistral-nemo"

QWEN3_MODEL_PATH = "C:\\Path\\to\\gguf\\file\\Qwen_Qwen3-0.6B-Q4_0.gguf"
QWEN3_MODEL_NAME = "qwen3"

DeepSeek_R1_MODEL_PATH = "C:\\Path\\to\\gguf\\file\\DeepSeek-R1-Distill-Qwen-1.5B-Q4_0.gguf"
DeepSeek_R1_MODEL_NAME = "r1"


Phi3_MODEL_PATH = "C:\\Path\\to\\gguf\\file\\Phi-3-mini-4k-instruct.Q4_0.gguf"
Phi3_MODEL_NAME = "phi3"




BINARY_DATA = read_json_to_dict("data/prompt-injection/data_binary_classification.json") # You can access it via the source.
BINARY_TEXTS = [BINARY_DATA[key]['text'] for key in BINARY_DATA.keys()]
BINARY_LABELS = [BINARY_DATA[key]['label'] for key in BINARY_DATA.keys()]
BINARY_LABELS_NUMERIC = [1 if label == 'yes' else 0 for label in BINARY_LABELS]
BINARY_PROMPTS = "data/prompt-injection/prompt_binary_classification.txt" # You can access it via the source.
RESULT_PATH = "evaluation/prompt-injection/"
INJECTION_PROMPT = read_json_to_dict("data/prompt-injection/injection_prompt.json") # You can access it via the source.

def binary_gpt4all_evaluation(model_path, model_name, with_injection=False, inject_prompt="blank", verbose=False):
    gpt4all_client = GPT4AllClient(model_path=model_path)
    gpt4all_client.set_pre_prompt(GPT4AllClient.prompt_read(BINARY_PROMPTS))

    injection_client = PromptInjection(gpt4all_client=gpt4all_client)

    if with_injection:
        injection_prompt_msg = INJECTION_PROMPT[inject_prompt]['msg']
        response = injection_client.query_gpt4all_evaluation(BINARY_TEXTS, injection_prompt=injection_prompt_msg,
                                                             verbose=verbose)
    else:
        response = injection_client.query_gpt4all_evaluation(BINARY_TEXTS, verbose=verbose)

    response_numeric = [1 if resp == 'yes' else 0 for resp in response]

    print("response_numeric" + str(response_numeric))

    incorrect_records = []
    for i in range(len(response_numeric)):
        if response_numeric[i] != BINARY_LABELS_NUMERIC[i]:
            incorrect_records.append(
                {"text": BINARY_TEXTS[i], "original_label": BINARY_LABELS_NUMERIC[i], "result": response_numeric[i]})

    eval_result = binary_classification_result_evaluation(BINARY_LABELS_NUMERIC, response_numeric)
    if with_injection:
        save_dictionary_to_json(eval_result, RESULT_PATH + model_name + f"-{inject_prompt}-temp{0}-injection.json")
    else:
        save_dictionary_to_json(eval_result, RESULT_PATH + f"{model_name}-normal.json")


def prompt_injection_main():

    # Qwen 2
    # normal
    print(f"Running binary classification evaluation for {QWEN2_MODEL_PATH} without injection")
    binary_gpt4all_evaluation(QWEN2_MODEL_PATH, QWEN2_MODEL_NAME, with_injection=False, verbose=True)

    # only_yes injection
    print(f"Running binary classification evaluation for {QWEN2_MODEL_PATH} with injection")
    binary_gpt4all_evaluation(QWEN2_MODEL_PATH, QWEN2_MODEL_NAME, with_injection=True, inject_prompt='only_yes', verbose=True)

    # only_no injection
    print(f"Running binary classification evaluation for {QWEN2_MODEL_PATH} with injection")
    binary_gpt4all_evaluation(QWEN2_MODEL_PATH, QWEN2_MODEL_NAME, with_injection=True, inject_prompt='only_no', verbose=True)

    # reverse injection
    print(f"Running binary classification evaluation for {QWEN2_MODEL_PATH} with injection")
    binary_gpt4all_evaluation(QWEN2_MODEL_PATH, QWEN2_MODEL_NAME, with_injection=True, inject_prompt='reverse', verbose=True)

    # Llama 3.2
    # normal
    print(f"Running binary classification evaluation for {LLAMA3_2_MODEL_PATH} without injection")
    binary_gpt4all_evaluation(LLAMA3_2_MODEL_PATH, LLAMA3_2_MODEL_NAME, with_injection=False, verbose=True)

    # only_yes injection
    print(f"Running binary classification evaluation for {LLAMA3_2_MODEL_PATH} with injection")
    binary_gpt4all_evaluation(LLAMA3_2_MODEL_PATH, LLAMA3_2_MODEL_NAME, with_injection=True, inject_prompt='only_yes', verbose=True)

    # Llama 3
    # normal
    print(f"Running binary classification evaluation for {LLAMA3_MODEL_PATH} without injection")
    binary_gpt4all_evaluation(LLAMA3_MODEL_PATH, LLAMA3_MODEL_NAME, with_injection=False, verbose=True)

    # only_yes injection
    print(f"Running binary classification evaluation for {LLAMA3_MODEL_PATH} with injection")
    binary_gpt4all_evaluation(LLAMA3_MODEL_PATH, LLAMA3_MODEL_NAME, with_injection=True, inject_prompt='only_yes', verbose=True)

    # only_no injection
    # I didn't do it.

    # reverse injection
    print(f"Running binary classification evaluation for {QWEN2_MODEL_PATH} with injection")
    binary_gpt4all_evaluation(QWEN2_MODEL_PATH, QWEN2_MODEL_NAME, with_injection=True, inject_prompt='reverse', verbose=True)

    # other models...

if __name__ == '__main__':
    prompt_injection_main()
