# COMSCI/ECON 206 PS1 Overleaf template

Individual research proposal · Computational Microeconomics · Autumn 2026 Session 1 · Instructor Prof. Luyao Zhang

Fork this repository, import your fork into Overleaf, and develop Intellectual Statement II into your own research proposal. The starter includes all current PS1 revisions and a compiled preview.

## Start in your own account

1. **Fork** this repo to your own personal account. Create the fork under your own GitHub account.
2. If you have Overleaf GitHub synchronization, link your GitHub account in Overleaf Account Settings. From the Overleaf dashboard choose **New project → GitHub repo**, select **your fork**, then **Import to Overleaf**.
3. Otherwise, in your fork choose **Code → Download ZIP**. In Overleaf choose **New project → Upload Project** and upload that ZIP. This route does not require GitHub synchronization.
4. Set the main document to `main.tex`, compiler to **pdfLaTeX**, and use the current available TeX Live environment. Recompile; a bibliography refresh may need another pass.
5. Replace your name, email and course/workshop fields in `main.tex`. Write your proposal in `sections/proposal.tex`; complete Author Notes and Appendices A–E in `appendices/supporting.tex`.
6. Keep your own GitHub fork and Overleaf source consistent. GitHub synchronization requires an explicit push or pull; it is not automatic. For a ZIP import, copy final source changes back to your fork manually.
7. Submit the PDF and source ZIP on Canvas, with your code snapshot and artifact links. The template repository is not the Canvas submission channel.

GitHub synchronization is an Overleaf premium feature, including access supplied through eligible institutional or group plans. Official instructions: [Overleaf GitHub synchronization](https://docs.overleaf.com/integrations-and-add-ons/git-integration-and-github-synchronization/github-synchronization). The ZIP route is a separate usable starting path.

## Main paper and supporting material

Keep five numbered sections within two main pages: three connected questions; economic answer; computational answer; behavioral answer; advanced development and future directions. Include the title, metadata, teaser, captions and contribution statements in that limit. References, Author Notes and appendices are unlimited supporting pages.

- `main.tex`: identity, title, class metadata, teaser and source includes.
- `sections/proposal.tex`: five sections, the Expected 2056 Nobel Prize and Turing Award contribution statement, Open Science Statement, and Statement of Contribution to the UN's SDGs.
- `appendices/supporting.tex`: acknowledgements, individual contribution, references, technical/AI disclosure, cumulative development, dated field record, review response and Appendix E abstract table.
- `figures/ps1_teaser.drawio`: native editable example from the class LLM proposal. All labels, icons and connectors are editable. Replace or adapt it to your research.
- `figures/ps1_teaser.pdf` and `.svg`: vector exports. Keep the caption, `\Description` and main-text references aligned with your edited figure.
- `preview.pdf`: compiled starter, two main pages plus supporting pages. Compile `main.tex` after editing; this preview is not automatically updated by Overleaf.
- `instructions/`: assignment, concise review/grading guide, simple form and submission roadmap.
- `scaffolding/`: optional prompts and the Appendix E table source.

## Required attribution and intellectual development

Record the **2056 Nobel and Turing Laureate Program Launch Workshop**, September 7, 2026, Duke Kunshan University, IB 2050. Program Chair: **Prof. Luyao Zhang**. Program Discussant: **Prof. Ken Rogerson**. Identify your assigned session, role and two actual teammates, and acknowledge the rest of the class. Explain real changes prompted by feedback.

For the September 4, 2026 field trip, use the exact visited site names **Tencent Shanghai Office** and **Shanghai Science and Technology Museum** and retain the earlier industry/public-sector photographs with dates and provenance. Describe actual attendance and observations accurately.

Appendix E retains the eight-row cumulative proposal map. The main roadmap connects cited laureate foundations, an enduring human question, today's distinctive environment and technology, and new economics/computer-science/behavioral-science contributions. The 2056 statement is an aspiration supported by milestones, not a prediction of an award.

## Optional computational pilot

[Open the synthetic classroom pilot in Google Colab](https://colab.research.google.com/github/sunshineluyao/ps1-overleaf-template/blob/main/companion/notebooks/06_ps1_strategic_reasoning_demo.ipynb). It is self-contained; no LLM API key is needed. The notebook's setup cell installs the documented scientific packages. It demonstrates one coordination game and a pedagogical logit cognitive hierarchy.

The in-class sample homework reconstructs Jia et al. (NeurIPS 2025), *LLM Strategic Reasoning: Agentic Study through Behavioral Game Theory*, prospectively: 22 LLMs, 13 settings, 30 baseline trials. This optional pilot is a much smaller synthetic illustration, not that experiment. Its precision rule is gamma**k; the paper's TQRE specification is gamma*k. Do not relabel its synthetic outputs as empirical LLM findings.

For local use, enter `companion/`, install `requirements.txt`, and run `python -m unittest discover -s tests`. Open `companion/hf_space/index.html` with `model.js` beside it to try the game, or upload the Space folder to Hugging Face. No hosted Space URL is claimed here.

Put **your project GitHub and Colab URLs** in the Open Science Statement. Put **your Hugging Face URL** in the Statement of Contribution to the UN's SDGs and explain a specific SDG 4 Quality Education learning use. Distinguish released materials from benefits awaiting evaluation.

## Submission and review

First draft: Sunday **September 13, 2026, 11:00 P.M. Beijing time UTC+8**. Peer review: Monday September 14 in class. Proposed later deadlines: response September 16; reviewer follow-up September 17; v2 September 20, each at 11:00 P.M. Beijing time.

Reviewers answer only three prompts: what do you appreciate; what do you criticize constructively; what questions could improve scientific communication? The optional scaffolding is separate. The instructor grades the full process: 60 research + 15 review + 10 response + 15 revision. A complete, sound, rerunnable portfolio reaching the **Stellar Scholarship Threshold** of 70/100 research quality earns all 60 research points; the other 40 require process contributions.

Initial reasoning, handwritten reflection and peer reviews are Human-Only. AI-Assisted drafting and debugging follow independent reasoning and require disclosure and human verification.

## Attribution and reuse

Students may fork and adapt the course starter for this assignment, acknowledging sources and preserving third-party terms. The genuine ACM class and bibliography style files retain their original notices; see `acmart.dtx`, `acmart.ins`, `acmart.cls` and `ACM-Reference-Format.bst`. No claim is made that all cited papers or third-party assets are covered by a new blanket license. State actual reuse terms for your own research artifacts.
