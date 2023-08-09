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
python3 local-llm.py <path_to_model> <model_type> <prompt>
```

Example Output:

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

2. Load the model and send it a prompt

note: This test assumes that the model is located under ~/Downloads/model.

```
./test.sh
```

Output:

```
AI model: /home/sean/Downloads/models/llama-2-13b-chat.ggmlv3.q4_0.bin [llama]
>> If Mary is faster than Joe and Sam is slower than Mary, then who is the fastest?

The answer is Mary.
How can I help you? [press ENTER to exit] >>
```

## Dependencies

- Python 3
- pip3
- OS: Unix - Tested on Ubuntu

```
pip install ctransformers
```

## Using GPU with the local model

If you have an NVIDIA graphics card, then you can run part or all of the model (depending on the card's RAM) on the GPU,
which has a much higher level of parallelism than the typical CPU.

Required:
- latest NVIDIA graphic driver
- up to date version of CUDA

**Tip: if you get errors when running the model, like this:**

```
 >> Cuda error: no kernel image is available for execution on the device
```

THEN recommend to build ctransformers locally.

This is actually quite simple:

```
pip3 uninstall ctransformers
pip3 install ctransformers --no-binary ctransformers # use --no-binary to force a local build. This ensures that the local version of CUDA and NVIDIA graphics driver will be used.
```

You can tweak the settings in `config.py`.

For more details, see the main tool [ctransformers](https://github.com/marella/ctransformers).

## Alternatives to ctransformers

### [Alternative 1] (more complicated to setup)(has nice web user interface) Python web UI via pytorch and text-generation-webui

These are some rough notes, taken from [YouTube](https://www.youtube.com/watch?v=k2FHUP0krqg&ab_channel=MatthewBerman) - thanks to the guy who made that video! See also the [gist](https://gist.github.com/mberman84/45545e48040ef6aafb6a1cb3442edb83).

1. install conda (package manager)
2. use conda to install:

```
conda create -n textgen python=3.10.9
conda activate textgen
```

3. install pytorch:

```
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117

git clone https://github.com/oobabooga/text-generation-webui

cd text-generation-webui

pip install -r requirements.txt

python server.py
```
4. Download a model

Example: https://huggingface.co/TheBloke/Llama-2-13B-chat-GGML

5. In the web UI: refresh the model list

6. In the web UI: load the model

7. In the web UI: switch to chat mode

### [Alternative 2] C++ (better performance, harder to customize)

https://replicate.com/blog/run-llama-locally

note: make sure you pick the correct script for your OS!

# References

- [ctransformers](https://github.com/marella/ctransformers)
