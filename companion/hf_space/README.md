---
title: COMSCI ECON 206 Strategic Reasoning Lab
emoji: 🎲
colorFrom: blue
colorTo: green
sdk: static
app_file: index.html
pinned: false
---
# Strategic Reasoning Lab
COMSCI/ECON 206 · Week 3 · Instructor Luyao Zhang.

Open `index.html` locally to play. To host after review, create a Hugging Face Space with the Static SDK, then upload this README, index.html and model.js at its root. No secrets, package installation, build command, backend or API calls are required. These files have not been published to a Space.

The model is a simplified truncated logit cognitive hierarchy for a coordination game. It is an original classroom adaptation inspired by Jia et al., NeurIPS 2025, https://doi.org/10.52202/085713-1955 and Camerer, Ho & Chong, QJE 2004, https://doi.org/10.1162/0033553041502225. The baseline matrix follows Jia et al., Table 1(b); variations are teaching examples. Synthetic play is neither human-subject evidence nor a replication of the original LLM study.

Companion: notebook 06 in the class repository. Run both at tau=1.5, gamma=1.2, Safe=5 to compare probabilities. No responses are transmitted or stored. Refreshing resets the pseudorandom sequence and local display.

The instructor will configure the final course repository and Space URLs. Official Static Space guide: https://huggingface.co/docs/hub/spaces-sdks-static
