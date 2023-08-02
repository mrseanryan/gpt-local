import sys
from ctransformers import AutoModelForCausalLM

if len(sys.argv) != 4:
    print(f"USAGE: {sys.argv[0]} <path_to_model> <model_type> <prompt>")
    exit(666)

path_to_model = sys.argv[1]
model_type = sys.argv[2]
prompt = sys.argv[3]

print(f"AI model: {path_to_model} [{model_type}]")

print(f">> {prompt}")

llm = AutoModelForCausalLM.from_pretrained(path_to_model, model_type=model_type)

print(llm(prompt))

def get_user_input():
    return input("How can I help you? [press ENTER to exit] >>")

prompt = get_user_input()
while(len(prompt)>0):
    print(llm(prompt))
    prompt = get_user_input()
