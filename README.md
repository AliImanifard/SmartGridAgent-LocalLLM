# SmartGridAgent

This repository contains the official implementation of the papers:

> **SmartGridAgent: An Educational Framework for Reliable Digital Twin-Based Smart Grid Workforce Training with Locally Hosted LLMs**  
> ***Ali Imanifard**, Babak Majidi, and Abdolah Shamisa*  
> Smart Grids and Sustainable Energy, 2025  
> DOI: https://doi.org/10.1007/s40866-025-00274-0

> **Trustworthy Large Language Model Prompt Engineering for Risk-Free Smart Grid Management Education**  
> ***Ali Imanifard**, Babak Majidi, and Abdolah Shamisa*  
> 2024 14th Smart Grid Conference (SGC), IEEE  
> DOI: https://doi.org/10.1109/SGC64640.2024.10983889
---

## 🔍 Overview

**SmartGridAgent** is an educational platform that integrates digital twin technology with **locally hosted Large Language Models (LLMs)** to support reliable, offline, and privacy-preserving smart grid workforce training. The platform allows interactive, step-by-step learning experiences without dependency on cloud-based APIs.

This project is built upon the structure and concepts introduced by the authors of:

> **Risks of Practicing Large Language Models in Smart Grid: Threat Modeling and Validation**  
> Jiangnan Li, Yingyuan Yang, Jinyuan Sun  
> Arxiv  
> DOI: https://doi.org/10.48550/arXiv.2405.06237

---

## 🚀 Key Features

- 🧠 **Locally Hosted LLMs**: Integrates open-source LLMs to provide on-device question-answering and task explanations.
- ⚡ **Digital Twin Integration**: Simulates real-world smart grid components in an interactive educational interface.
- 🔐 **Offline & Privacy-Preserving**: No internet or cloud dependencies.
- 🧑‍🏫 **Modular Educational Framework**: Designed for reproducible and customizable curriculum-based training.

---

## 📂 Project Structure

```plaintext
SmartGridAgent
├─ evaluation
│  ├─ prompt-extraction
│  │  └─ JSON files             # NEW: JSON responses
│  └─ prompt-injection
│     └─ JSON files             # NEW: JSON responses
├─ SGLLM
│  ├─ attacks.py                # Significantly modified
│  ├─ llms.py                   # Significantly modified
│  └─ utilities.py              # You can access it via the source
├─ evaluate_extraction.py       # NEW: Evaluation layer
├─ other_evaluation_metrics.py	# NEW: Other Evaluation Metrics
├─ prompt_extraction.py         # Significantly modified
├─ prompt_injection.py          # Significantly modified
├─ credentials.py               # You can access it via the source
└─ data                         # You can access it via the source
````

---

## 🛠️ Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/SmartGridAgent-LocalLLM.git
   cd SmartGridAgent-LocalLLM
   ```

2. **Download required files manually**
   Due to licensing restrictions, the following file must be downloaded manually:

   * `utilities.py`: from [Original Repository](https://github.com/jiangnan3/smartgrid-llm/blob/main/SGLLM/utilities.py)
   * `credentials.py`: from [Original Repository](https://github.com/jiangnan3/smartgrid-llm/blob/main/credentials.py)
   * `data folder`: from [Original Repository](https://github.com/jiangnan3/smartgrid-llm/tree/main/data)

   Place it in the appropriate directory as indicated in project structure.

---

## 🔁 Original Work Acknowledgment

This work is based on the original open-source project associated with:

> **Risks of Practicing Large Language Models in Smart Grid: Threat Modeling and Validation**  
> Jiangnan Li, Yingyuan Yang, Jinyuan Sun  
> Arxiv  
> https://doi.org/10.48550/arXiv.2405.06237

We have significantly modified or replaced the following files from the original codebase:

| File                     		| Status                 | Notes                          	         |
| ----------------------------- | ---------------------- | ----------------------------------------- |
| `evaluate_extraction.py`      | ✅ New                 | Evaluation of extraction layer            |
| `other_evaluation_metrics.py` | ✅ New                 | Other Evaluation metrics of extraction    |
| `prompt_extraction.py` 	    | ✅ Modified            | Refactored to support Locally hosted LLMs |
| `prompt_injection.py`         | ✅ Modified            | Refactored to support Locally hosted LLMs |
| `SGLLM/attacks.py` 	        | ✅ Modified            | Refactored to support Locally hosted LLMs |
| `SGLLM/llms.py`    		    | ✅ Modified            | Refactored to support Locally hosted LLMs |
| `utilities.py`           		| ❌ Unchanged (removed) | Please download it separately       	     |
| `credentials.py`         		| ❌ Removed             | Please download it separately    		 |
| `data`         				| ❌ Removed             | Please download it separately    		 |


We have not copied or reused any unchanged code that lacks a clear license.

---

## 📜 Citation

If you use this code or find it helpful, please cite our papers:

```bibtex
@ARTICLE{Imanifard2025SmartGridAgent,
  title     = "{SmartGridAgent}: An educational framework for reliable digital
               twin-based smart grid workforce training with locally hosted
               {LLMs}",
  author    = "Imanifard, Ali and Majidi, Babak and Shamisa, Abdolah",
  journal   = "Smart Grids and Sustainable Energy",
  publisher = "Springer Science and Business Media LLC",
  volume    =  10,
  number    =  2,
  month     =  may,
  year      =  2025,
  copyright = "https://www.springernature.com/gp/researchers/text-and-data-mining",
  doi		= "10.1007/s40866-025-00274-0",
  language  = "en"
}

@INPROCEEDINGS{Imanifard2024SGC,
  author={Imanifard, Ali and Majidi, Babak and Shamisa, Abdolah},
  booktitle={2024 14th Smart Grid Conference (SGC)}, 
  title={Trustworthy Large Language Model Prompt Engineering for Risk-Free Smart Grid Management Education}, 
  year={2024},
  volume={},
  number={},
  pages={1-6},
  abstract={The management and control of smart grids are rapidly evolving to include Artificial Intelligence (AI). Large Language Models (LLMs) are the latest solution for AI-capable Industry 4.0 management. The trustworthiness of the LLMs is an important issue in the management of such systems. In this paper, the behaviors of various locally-hosted LLMs in managing unauthorized operations within smart grids are investigated. To highlight the advantages of local-hosting, we also compare the performance of these models with online LLMs. Our findings show that locally-hosted LLMs perform better in preventing vulnerabilities than their online counterparts. This study proposes an educational platform for future generations of smart grid operators and provides guidelines for teaching the vulnerabilities of LLM prompting needed to be included in the educational curriculum of the smart grid management workforce. Furthermore, the findings of this research can provide guidelines for standardization, legislation and regulations of AI applications in smart grids.},
  keywords={Training;Large language models;Legislation;Reliability engineering;Regulation;Smart grids;Power system reliability;Fourth Industrial Revolution;Prompt engineering;Guidelines;Education Technology;Large Language Model;Prompt Engineering;Power System Education;Smart Grid},
  doi={10.1109/SGC64640.2024.10983889},
  ISSN={2572-6927},
  month={Dec},}
```

And we recommend citing the original foundational paper as well if you build on their ideas.

---

## 🧠 Acknowledgments

We thank the authors of "Risks of Practicing Large Language Models in Smart Grid" for their foundational work, which inspired this project.


