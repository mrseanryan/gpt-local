# gpt-local README

Local LLM for GPT (llama 2 or dolly or gpt etc.) via Python - using the excellent ctransformers project.

This is basically a wrapper for quickly setting up a local LLM.

## What is GPT ?

*Generative Pre-trained Transformers, commonly known as GPT, are a family of neural network models that uses the transformer architecture and is a key advancement in artificial intelligence (AI) powering generative AI applications such as ChatGPT. GPT models give applications the ability to create human-like text and content (images, music, and more), and answer questions in a conversational manner.*


## Usage

```
./go.sh <path_to_model> <model_type> <prompt>
```

OR

```
python3 local-llama2.py <path_to_model> <model_type> <prompt>
```

Output:

```
AI model: /home/sean/Downloads/models/llama-2-13b-chat.ggmlv3.q4_0.bin [llama]
>> If Mary is faster than Joe and Sam is slower than Mary, then who is the fastest?

The answer is Mary.
How can I help you? [press ENTER to exit] >>
```

## Test

1. Download a compatible model. To know what model types are supported, see the [ctransformers](https://github.com/marella/ctransformers) project.

Quality models are available at hugging face - see [TheBloke](https://huggingface.co/TheBloke).

Example: https://huggingface.co/TheBloke/Llama-2-13B-chat-GGML/resolve/main/llama-2-13b-chat.ggmlv3.q4_0.bin

OR via bash:

```
./download-llama-2-13B-model.sh
```

2. Send a prompt to the model

note: This test assumes that the model is located under ~/Downloads/model.

```
./test.sh
```

## Dependencies

- Python 3
- pip3
- OS: Unix - Tested on Ubuntu

```
pip install ctransformers
```

# References

- [ctransformers](https://github.com/marella/ctransformers)
