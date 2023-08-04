import sys
from ctransformers import AutoModelForCausalLM

import config
import util_time

if len(sys.argv) != 4:
    print(f"USAGE: {sys.argv[0]} <path_to_model> <model_type> <prompt>")
    exit(666)

path_to_model = sys.argv[1]
model_type = sys.argv[2]
prompt = sys.argv[3]

gpu_message = f"Using {config.LOCAL_GPU_LAYERS} GPU layers" if config.IS_GPU_ENABLED else "NOT using GPU"
print(f"AI model: {path_to_model} [{model_type}] [{gpu_message}]")

print(f">> {prompt}")

llm = None

if config.IS_GPU_ENABLED:
    llm = AutoModelForCausalLM.from_pretrained(path_to_model, model_type=model_type, gpu_layers=config.LOCAL_GPU_LAYERS)
else:
    llm = AutoModelForCausalLM.from_pretrained(path_to_model, model_type=model_type)

def next_prompt(prompt):
    start = util_time.start_timer()
    rsp = llm(prompt)
    print(rsp)
    seconds_elapsed = util_time.end_timer(start)
    print(f" -- Responded after {util_time.describe_elapsed_seconds(seconds_elapsed)}")

def get_user_input():
    return input("How can I help you? [press ENTER to exit] >>")

next_prompt(prompt)

prompt = get_user_input()
while(len(prompt)>0):
    next_prompt(prompt)
    prompt = get_user_input()
