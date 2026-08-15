# Interview Models

Prompt logic and (optionally) fine-tuned/local model artifacts for
generating interview questions and scoring answers. The default
implementation calls hosted LLMs via `backend/app/ai/router.py`;
drop local model weights or ONNX/GGUF files here if you add offline
inference later.
