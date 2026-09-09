# Optional synthetic pilot for the class LLM proposal

[Open in Colab](https://colab.research.google.com/github/sunshineluyao/ps1-overleaf-template/blob/main/companion/notebooks/06_ps1_strategic_reasoning_demo.ipynb). This self-contained notebook runs on CPU with no LLM API key.

The sample homework uses the in-class imagined Jia et al. (NeurIPS 2025) study: 22 LLMs, 13 settings, 30 baseline trials. This folder supplies a smaller **synthetic classroom pilot**, not that study or a full replication. The notebook and game implement a finite logit cognitive hierarchy with gamma**k precision; the paper uses gamma*k in its TQRE specification. Numerical source and saved outputs are retained from the earlier checked teaching release.

Run the notebook in a fresh CPU session. For a local source check, run `python -m unittest discover -s tests` from this folder after installing requirements.txt. The static game is in hf_space/; open index.html with model.js alongside it. Upload those files and the Space README to Hugging Face to create a hosted demo. Hosting is pending.

Use the latest Assignment and Review Guide in ../instructions and optional prompts in ../scaffolding. Reviewers use only strengths, constructive criticism and questions for communication; no numerical peer rating is required. Group project GitHub/Colab links in an Open Science Statement, and the Hugging Face link in a Statement of Contribution to the UN's SDGs (SDG 4 Quality Education).

Source paper: https://doi.org/10.52202/085713-1955. The cooperation matrix follows Table 1(b); parameter variations and the synthetic pilot are teaching adaptations. Synthetic output is not evidence about actual human or LLM behavior. Educational benefits of the tool have not been measured.
