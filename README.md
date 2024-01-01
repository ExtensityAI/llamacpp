# LlamaCpp Neuro-Symbolic Backend

Running a Llama server as a Neuro-Symbolic backend. This backend is a wrapper around the LlamaCpp project.

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

Initialize submodules:

```bash
git submodule update --init --recursive
```

## Compile LlamaCpp for your System

```bash
cd llama.cpp
make
```

For more information, see the [LlamaCpp](https://github.com/ggerganov/llama.cpp).

## [Optional] Prepare the Weights for LlamaCpp


### [Optional] Get Weights from Meta

If you don't have the gguf weights, you can download them from Meta:

```
https://ai.meta.com/llama/
```

### [Optional] Convert Weights to LlamaCpp Format

If you don't have the gguf weights (only the downloaded weights from Meta) then you will need to convert them to the LlamaCpp format. To do this, you will need to install the following dependencies:

```bash
pip install llama-recipes transformers datasets accelerate sentencepiece protobuf==3.20 py7zr scipy peft bitsandbytes fire torch_tb_profiler ipywidgets
# create a folder for all models
mkdir models
```

Now move all models (weights) obtained from Meta into the `models` directory and rename them to follow the following sub-folder naming convention: '7B', '7Bf', '13B', '13Bf', '30B', '34B', '65B', '70B', '70Bf'.
Here B stands for Billion and f stands for float16.
Then run the following commands:

```bash
# start ipython
ipython
```

Now we convert the weights to the HuggingFace format as follows:

```python
# set the conversion script path for HuggingFace
TRANSFORM="""`python -c "import transformers;print('/'.join(transformers.__file__.split('/')[:-1])+'/models/llama/convert_llama_weights_to_hf.py')"`"""
# set the model path
model_dir = './models'
# set the model size and name
model_size = '13Bf'
# set the output path
hf_model_dir = './hf_models/llama-2-13b-chat'
# run the HuggingFace conversion
!python $TRANSFORM --input_dir $model_dir --model_size $model_size --output_dir $hf_model_dir
```

Now run the `gguf`` conversion script:

```bash
# navigate to the llama.cpp directory
# run the gguf conversion
python convert.py /path/to/hf_models/llama-2-13b-chat
# now you should have the gguf weights in the same directory
# you can now rename and move the `ggml-model-f16.gguf` weights to the models directory of your llama.cpp installation
```

### [Optional] Quantize the Weights

If you want to quantize the weights to reduce the memory requirements, you will need to run the following command from the llama.cpp directory:

```bash
./quantize models/ggml-model-llama-2-13B-f16.gguf models/ggml-model-llama-2-13B-f16-q5_k_m.gguf Q5_K_M
```

In this example, we quantize the weights to 5 bits for the kernel and 5 bits for the mask (Q5_K_M) and save the quantized weights to the `models/ggml-model-llama-2-13B-f16-q5_k_m.gguf` file.

## Run the Server

```bash
./server -m models/ggml-model-llama-2-13B-f16-q5_k_m.gguf -c 2048
```
