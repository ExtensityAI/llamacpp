import subprocess
import argparse


def run(model: str, port: int):
    subprocess.call(['./llama.cpp/server', '-m', model, '--port', str(port)])


def parse_args():
    parser = argparse.ArgumentParser(description='LLaMA C++ Server')
    parser.add_argument('-m', '--model', type=str, help='model name',  default='models/ggml-model-llama-2-13B-f16.gguf')
    parser.add_argument('-p', '--port',  type=int, help='port number', default=8080)
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_args()
    run(args.model, args.port)
