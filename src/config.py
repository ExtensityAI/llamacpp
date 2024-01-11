import subprocess

from symai import Expression
from symai.functional import EngineRepository

from .engine import LLaMACppClientEngine


class EngineConfig(Expression):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def forward(self, model: str, host: str = 'http://localhost', port: int = 8080, *args, **kwargs):

        subprocess.call(['./llama.cpp/server', '-m', model, '--port', str(port)])

        # initialize the engine
        engine = LLaMACppClientEngine(host=host, port=port)
        EngineRepository.register('neurosymbolic', engine, allow_engine_override=True)

        return engine
