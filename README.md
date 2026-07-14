# Multimodal Fashion & Context Retrieval

An end-to-end multimodal image retrieval system built for the **Glance ML Internship Assignment**. The system retrieves relevant fashion images from a collection using natural language queries by combining **OpenCLIP embeddings**, **BLIP image captions**, and **metadata-aware reranking**.

---

## Overview

Traditional CLIP-based retrieval relies only on embedding similarity, which often struggles with fine-grained fashion attributes and compositional queries (e.g., *"red tie with white shirt inside an office"*).

To improve retrieval quality, this project combines semantic embeddings with structured metadata extracted from image captions.

The retrieval pipeline consists of:

- OpenCLIP for image and text embeddings
- BLIP for automatic image caption generation
- Rule-based attribute extraction
- Qdrant as the vector database
- Metadata-aware reranking

---

# Architecture

```
                    IMAGE
                      │
        ┌─────────────┴─────────────┐
        ▼                           ▼
   BLIP Captioning             OpenCLIP
        │                     Image Embedding
        ▼                           │
 Attribute Parser                   │
        │                           │
        └─────────────┬─────────────┘
                      ▼
                 Qdrant Index
      (Embedding + Caption + Metadata)


                     QUERY
                       │
          ┌────────────┴────────────┐
          ▼                         ▼
 Attribute Parser             OpenCLIP
          │                 Text Embedding
          └────────────┬────────────┘
                       ▼
               Vector Search
                       ▼
            Metadata-aware Reranking
                       ▼
                 Top-K Images
```

---

# Repository Structure

```
fashion-retrieval/

├── models/
│   ├── clip_model.py
│   ├── caption_model.py
│   └── attribute_parser.py
│
├── indexer/
│   ├── select_images.py
│   ├── generate_metadata.py
│   ├── generate_embeddings.py
│   └── build_index.py
│
├── retriever/
│   ├── parse_query.py
│   ├── search.py
│   └── rerank.py
│
├── vector_db/
│   └── qdrant.py
│
├── data/
├── outputs/
├── requirements.txt
└── README.md
```

---

# Dataset

- Fashionpedia Images
- Randomly sampled **800 images**
- Selection is deterministic using `selected_images.txt`

No dataset annotations were used during indexing.

The system relies entirely on visual understanding, making it zero-shot and dataset-agnostic.

---

# Installation

## Clone repository

```bash
git clone <repo-url>

cd fashion-retrieval
```

## Create virtual environment

```bash
python -m venv .venv

source .venv/bin/activate
```

## Install dependencies

```bash
pip install -r requirements.txt
```

---

# Running Qdrant

```bash
docker run -d \
--name qdrant-fashion \
-p 6333:6333 \
-v $(pwd)/qdrant_storage:/qdrant/storage \
qdrant/qdrant
```

---

# Indexing Pipeline

### Step 1

Generate deterministic image subset

```bash
python select_images.py
```

### Step 2

Generate captions + metadata

```bash
python generate_metadata.py
```

### Step 3

Generate embeddings and build vector index

```bash
python build_index.py
```

---

# Retrieval

Run

```bash
python evaluate.py
```

Example queries:

- A person in a bright yellow raincoat
- Professional business attire inside a modern office
- Someone wearing a blue shirt sitting on a park bench
- Casual weekend outfit for a city walk
- A red tie and a white shirt in a formal setting

---

# Retrieval Strategy

Instead of relying only on vector similarity, retrieved candidates are reranked using structured metadata.

Final ranking considers:

- Vector similarity
- Clothing type
- Clothing color
- Scene
- Style

This improves compositional retrieval compared to a vanilla CLIP pipeline.

---

# Sample Result

Query

> A person in a bright yellow raincoat

Top Result

> a little girl in a yellow raincoat and red tights

---

## Why not Vanilla CLIP?

Vanilla CLIP retrieves images purely using embedding similarity, which can struggle with compositional fashion queries.

This project augments semantic retrieval with structured metadata extraction and metadata-aware reranking, improving retrieval for clothing attributes, scene context, and style.

---

# Technologies

- Python
- PyTorch
- OpenCLIP
- BLIP
- HuggingFace Transformers
- Qdrant
- Docker

---

# Limitations

- Caption quality depends on BLIP.
- Fine-grained fashion attributes may be missed if they are absent from generated captions.
- Metadata extraction is rule-based.

---

# Future Work

- Replace rule-based parser with an LLM or lightweight information extraction model.
- Fine-tune a fashion-specific vision-language model.
- Incorporate weather, city, and location metadata.
- Learn reranking weights instead of using heuristic scoring.
- Support large-scale distributed indexing.
