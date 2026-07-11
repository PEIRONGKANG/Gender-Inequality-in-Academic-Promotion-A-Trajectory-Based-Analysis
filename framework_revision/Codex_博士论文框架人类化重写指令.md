# Codex Revision Prompt: Humanise and Restructure the Doctoral Dissertation Proposal into a Formal Dissertation Framework

## 0. Source file

Revise the following document:

`/mnt/data/Doctoral_Dissertation_Proposal_PEI_Rongkang_revised_tracked.docx`

Do not overwrite the source file.

Create:

1. `Doctoral_Dissertation_Framework_PEI_Rongkang_tracked.docx`
2. `Doctoral_Dissertation_Framework_PEI_Rongkang_clean.docx`
3. `revision_memo.md`
4. `terminology_control_table.csv`
5. `research_question_mapping.csv`
6. `citation_audit.csv`
7. `unresolved_issues.md`

The revised document should no longer read like an over-engineered proposal or a technical protocol. It should read like the opening framework of a formal doctoral dissertation that can later absorb empirical results, tables, figures, and discussion chapters.

---

# 1. Main revision goal

Transform the current proposal into a coherent dissertation manuscript framework with three studies:

- Study 1: promotion timelines
- Study 2: institutional mobility and promotion timing
- Study 3: KAKEN-related academic resources and stage-specific promotion

The structure should support later insertion of:

- descriptive results;
- event-history results;
- interaction results;
- sequence-analysis results;
- robustness checks;
- substantive interpretation;
- chapter-level discussion.

The text must sound like a human scholar wrote it.

Avoid language that sounds machine-generated, overly symmetrical, over-defensive, or excessively exhaustive.

---

# 2. Final research questions

Use exactly one research question for each study.

## RQ1

**Where do gender differences appear in observed academic promotion timelines in Japan?**

## RQ2

**How is the number of institutional moves associated with promotion timing, and does this association differ between women and men?**

## RQ3

**How is access to KAKEN-related academic resources associated with promotion across different career stages, and do these associations differ between women and men?**

Do not retain RQ2a–RQ2e or RQ3a–RQ3d as formal research questions.

Move their useful content into:

- analytical dimensions;
- hypotheses;
- model specifications;
- secondary analyses;
- robustness checks.

---

# 3. Dissertation logic

Use the following progression:

> Study 1 identifies where gender differences appear.  
> Study 2 examines whether institutional mobility is associated with promotion timing.  
> Study 3 examines whether KAKEN-related academic resources are associated with promotion across career stages.

Use this shorter logic in the Introduction and chapter transitions:

> timing → mobility → academic resources

Do not repeatedly restate the full dissertation logic in every chapter.

---

# 4. Humanisation rules

The current document is too polished in a template-like way. Revise it to sound more natural, selective, and intellectually authored.

## 4.1 Reduce excessive symmetry

Avoid repeated constructions such as:

- “frequency, timing, and type”
- “origin, destination, and direction”
- “access, intensity, and status”
- “observed pathways, hypothesized mechanisms, and unobserved private costs”

Keep only distinctions that are substantively necessary.

Prefer natural prose over repeated three-part or four-part lists.

## 4.2 Reduce defensive repetition

The current document repeatedly states that the analysis is:

- descriptive;
- associational;
- non-causal;
- not a measure of merit;
- not directly observed.

Retain causal caveats in only three main places:

1. Abstract
2. Methods
3. Limitations

Elsewhere, use precise non-causal verbs naturally:

- associated with
- related to
- differs by
- observed among
- corresponds to

Do not repeat “this does not identify causal effects” in every section.

## 4.3 Remove engineering language from the main text

Move database field names, status codes, and pipeline labels out of the conceptual chapters.

Examples to move to Appendix or Methods:

- `v_jp_researchers_kaken_project.research_category`
- `LINKED_CONFIDENT`
- `UNRESOLVED_LINKAGE`
- `SOURCE_COVERAGE_LIMITED`
- `TIER_1`
- `NOT_OBSERVED`
- script names
- file names
- raw schema labels

In the main text, use readable academic language.

Example:

Instead of:

> Project category comes directly from `v_jp_researchers_kaken_project.research_category`.

Write:

> The original KAKEN project category is retained in the analysis to preserve differences across funding schemes.

Put the raw field name in the Appendix.

## 4.4 Reduce over-detailed method catalogues

Do not list every robustness option in the main chapter.

For example, do not foreground all of the following together:

- Optimal Matching
- transition-rate costs
- Dynamic Hamming
- PAM
- Ward
- silhouette
- resampling stability
- alternative windows
- multiple thresholds

In the main text, state the methodological strategy clearly and briefly.

Move technical alternatives to:

- Appendix;
- Methods subsection;
- robustness plan.

## 4.5 Use a stronger authorial voice

Prefer statements that show theoretical judgment.

Preserve and emphasize sentences such as:

> The ability to move may itself be an unequally distributed career resource.

Also retain the idea that:

> The same institutional move may carry different career implications for women and men.

Use fewer generic transition sentences such as:

- “This dissertation therefore…”
- “The empirical implication is…”
- “These findings motivate…”

Vary sentence openings.

## 4.6 Avoid AI-style overqualification

Do not qualify every sentence.

Use limitations where they matter, but allow the argument to proceed.

For example:

Too AI-like:

> Mobility may reflect strategic matching, constrained choice, temporary adjustment, sector change, or unobserved preference.

More natural:

> Institutional moves can reflect both career strategy and constraint. Their meaning therefore depends on when they occur and where they lead.

---

# 5. Study 2 revision

## 5.1 Core focus

Study 2 must focus on one main explanatory variable:

> **number of institutional moves**

The central question is whether repeated institutional movement is associated with faster or slower promotion, and whether the association differs between women and men.

## 5.2 Primary outcome

Primary outcome:

- time to first Associate Professor appointment.

Where feasible, include:

- time from Associate Professor to Full Professor.

But AP transition remains the main outcome.

## 5.3 Main variables

Primary variables:

- cumulative institutional move count before year t;
- move count before AP;
- gender;
- gender × move count;
- time since PhD;
- field;
- cohort.

Secondary mobility variables:

- upward moves;
- lateral moves;
- downward moves;
- internal versus external promotion;
- time since last move;
- mobility rate per observed career year.

These are not separate research questions.

## 5.4 Institutional prestige

Retain institutional prestige as a secondary measure.

Use:

- annual within-ranking percentile;
- three-year pre-move median;
- broad prestige tiers.

Do not make ranking systems the theoretical centre of Study 2.

THE, QS, and ARWU should be described as alternative measures.

Do not overload the chapter with detailed ranking formulas in the main prose.

Place formulas and thresholds in the Methods or Appendix.

## 5.5 Institution size

Retain institution size as a contextual or robustness variable.

Use:

- total students;
- graduate students;
- doctoral students;
- full-time faculty;
- annual size percentile.

Do not treat institution size as equivalent to prestige.

Do not make student numbers a second central theory.

## 5.6 Sequence analysis

Keep sequence analysis as a secondary analytical component.

Its role is to identify typical mobility pathways after the main event-history analysis.

Do not present sequence analysis as a separate study.

The main text should state:

> Sequence analysis will be used to identify recurring patterns of institutional stability and movement across academic careers.

Detailed distance metrics and clustering diagnostics belong in the Appendix.

## 5.7 Theoretical framing

The Study 2 theory section should engage:

- career mobility;
- status attainment;
- segmented labour markets;
- gendered organizations;
- linked lives;
- dual-career coordination;
- family and relocation constraints.

The main theoretical claim should be:

> Institutional mobility may offer career opportunities, but the capacity to move is not equally distributed.

Do not write that women are naturally less willing to move.

Use structural language.

## 5.8 Study 2 hypotheses

Convert the old RQ2a–RQ2e into a small set of hypotheses or expectations.

Recommended:

**H2.1** More institutional moves are associated with promotion timing.

**H2.2** The association between move count and promotion timing differs between women and men.

**H2.3** Upward moves are more strongly associated with promotion than lateral or downward moves.

Do not create more than three main hypotheses.

---

# 6. Study 3 revision

## 6.1 Core focus

Study 3 must focus on:

> KAKEN-related academic resources and promotion across career stages.

The main comparison is between:

- PhD to Associate Professor;
- Associate Professor to Full Professor.

## 6.2 Main conceptual domains

Group KAKEN resources into four domains:

1. access;
2. project leadership;
3. funding;
4. project-based network position.

Do not list every variable in the research question.

## 6.3 Main variables

Access:

- any KAKEN participation.

Leadership:

- PI;
- Co-I;
- cumulative PI experience;
- Co-I-to-PI progression.

Funding:

- direct funding;
- log positive funding;
- field-year standardized funding.

Project context:

- original KAKEN project category.

Network:

- degree;
- PI outdegree;
- PI indegree.

Weighted degree should remain a robustness measure.

## 6.4 Stage-specific design

Study 3 should explicitly compare two promotion stages.

### Stage 1

- PhD to Associate Professor.

### Stage 2

- Associate Professor to Full Professor.

Use stage-specific models rather than one pooled model unless a pooled interaction model is theoretically justified.

## 6.5 Main interaction logic

The central analytical structure is:

- KAKEN resource;
- gender;
- career stage;
- gender × resource;
- stage × resource;
- gender × stage × resource only where substantively justified and statistically supported.

Do not include every possible interaction in one model.

Use separate model families.

## 6.6 Post-promotion trajectories

Post-AP trajectories should remain optional and secondary.

Do not present them as a fourth core component of Study 3.

If retained, place them under:

> Supplementary analysis: post-promotion resource trajectories

## 6.7 Theoretical framing

Study 3 should engage:

- cumulative advantage;
- academic capital;
- sociology of science;
- project leadership;
- network position;
- gendered returns to academic resources.

The main theoretical claim should be:

> Access to academic resources and the career value attached to those resources may vary by gender and career stage.

## 6.8 Study 3 hypotheses

Recommended:

**H3.1** Greater access to KAKEN-related academic resources is associated with faster promotion.

**H3.2** The association between KAKEN resources and promotion differs between women and men.

**H3.3** The association between KAKEN resources and promotion varies across career stages.

Do not add more than three main hypotheses.

---

# 7. Formal dissertation structure

Restructure the document as a dissertation framework rather than a proposal report.

Use the following chapter structure.

## Front Matter

- Title Page
- Abstract
- Acknowledgements
- Table of Contents
- List of Tables
- List of Figures
- List of Abbreviations

## Chapter 1. Introduction

### 1.1 Background
### 1.2 Research Problem
### 1.3 Research Questions
### 1.4 Theoretical Orientation
### 1.5 Data and Methodological Overview
### 1.6 Dissertation Structure
### 1.7 Contribution

## Chapter 2. Gender Inequality in Japanese Academic Careers

### 2.1 Japanese Academic Career Structure
### 2.2 Promotion and Rank Inequality
### 2.3 Institutional Mobility
### 2.4 KAKEN and Academic Resources
### 2.5 Gendered Organizations and Career Constraints
### 2.6 Cumulative Advantage
### 2.7 Research Gap

This chapter should synthesize the literature.

Do not divide it into too many small sections.

## Chapter 3. Data and Methods

### 3.1 Data Sources
### 3.2 Research Population
### 3.3 Researcher and Institution Linkage
### 3.4 Career and Promotion Measures
### 3.5 Institutional Mobility Measures
### 3.6 KAKEN Resource Measures
### 3.7 Event-History Analysis
### 3.8 Sequence Analysis
### 3.9 Missing Data and Validation
### 3.10 Ethics and Limitations

Move all variable-construction detail here or to Appendix.

## Chapter 4. Study 1: Gendered Promotion Timelines

### 4.1 Introduction
### 4.2 Research Question
### 4.3 Data and Measures
### 4.4 Analytical Strategy
### 4.5 Results
### 4.6 Discussion
### 4.7 Chapter Summary

Study 1 already has results, so preserve them.

## Chapter 5. Study 2: Institutional Mobility and Promotion Timing

### 5.1 Introduction
### 5.2 Theoretical Expectations
### 5.3 Research Question
### 5.4 Variables and Measures
### 5.5 Analytical Strategy
### 5.6 Results
### 5.7 Robustness Checks
### 5.8 Discussion
### 5.9 Chapter Summary

Insert placeholders where results are not yet available.

Use explicit placeholders such as:

- `[Insert descriptive mobility results here]`
- `[Insert event-history results here]`
- `[Insert gender interaction figure here]`
- `[Insert sequence typology here]`

Do not invent results.

## Chapter 6. Study 3: KAKEN Resources and Stage-Specific Promotion

### 6.1 Introduction
### 6.2 Theoretical Expectations
### 6.3 Research Question
### 6.4 Variables and Measures
### 6.5 Stage-Specific Analytical Strategy
### 6.6 Results: PhD to Associate Professor
### 6.7 Results: Associate Professor to Full Professor
### 6.8 Gender Differences in Resource Associations
### 6.9 Robustness Checks
### 6.10 Discussion
### 6.11 Chapter Summary

Insert placeholders.

Do not invent Stage 2 results if they are not yet available.

## Chapter 7. General Discussion

### 7.1 Summary of Findings
### 7.2 Promotion Timing
### 7.3 Mobility as a Gendered Career Strategy
### 7.4 Gendered Access to Academic Resources
### 7.5 Career-Stage Differences
### 7.6 Theoretical Contributions
### 7.7 Policy Implications
### 7.8 Limitations
### 7.9 Future Research

## Chapter 8. Conclusion

Keep this concise.

## Appendices

- variable dictionary;
- ranking construction;
- institution-size construction;
- mobility coding;
- KAKEN coding;
- network construction;
- robustness specifications;
- data-quality diagnostics;
- additional tables;
- additional figures.

---

# 8. Results placeholders

Because the dissertation is not yet complete, add structured placeholders.

For every unfinished empirical section, use this format:

## Results placeholder

**Descriptive finding:**  
`[Insert result here]`

**Main model:**  
`[Insert coefficient, uncertainty interval, and interpretation here]`

**Gender comparison:**  
`[Insert predicted probabilities or marginal effects here]`

**Robustness:**  
`[Insert robustness summary here]`

**Substantive interpretation:**  
`[Insert interpretation linked to theory here]`

Do not fabricate any values.

---

# 9. Writing style

Use clear academic English.

The prose should be:

- direct;
- analytical;
- restrained;
- readable;
- discipline-appropriate;
- consistent.

Avoid:

- excessive bullet lists in the main body;
- repeated “this study therefore” constructions;
- overlong catalogue sentences;
- generic claims of novelty;
- artificial symmetry;
- repetitive caveats;
- technical field names in theoretical prose;
- overly polished “AI” transitions.

Prefer paragraphs with:

1. one clear claim;
2. supporting evidence or literature;
3. link to the present analysis.

---

# 10. Terminology control

Use these terms consistently:

- researchmap
- KAKEN
- Associate Professor
- Full Professor
- AP
- FP
- PI
- Co-I
- institutional mobility
- institutional move
- promotion timing
- promotion risk
- researcher-year
- event-history analysis
- multichannel sequence analysis
- KAKEN-related academic resources
- project-based collaboration networks
- career stage
- right-censoring
- time-ordered association

Do not alternate between:

- job mobility / institutional mobility / school hopping;
- promotion speed / promotion time / promotion duration

without a clear reason.

Preferred main term:

> promotion timing

Use:

> promotion risk

only in event-history model interpretation.

---

# 11. Specific content reductions

Shorten the current document by removing or relocating:

- repeated causal disclaimers;
- detailed raw field names;
- complete status-code lists;
- full diagnostic inventories;
- every robustness option;
- repeated statements of the dissertation logic;
- excessive lists of variables in the Abstract;
- engineering-style workflow descriptions.

The main dissertation text should explain the research.

The Appendix should document the technical implementation.

---

# 12. Abstract revision

Rewrite the Abstract to approximately 250–300 words.

It should include:

1. research problem;
2. data sources;
3. one sentence for each study;
4. central theoretical contribution;
5. non-causal interpretation boundary.

Do not list every variable.

Do not list every method.

Do not use “timing → mobility → resources” in the Abstract unless it reads naturally.

---

# 13. Introduction revision

The Introduction should answer:

- Why gender inequality in Japanese academic careers matters;
- What is not yet known;
- Why institutional mobility matters;
- Why KAKEN resources matter;
- Why longitudinal data are needed;
- How the three studies fit together.

Do not introduce all operational details in Chapter 1.

---

# 14. Chapter transitions

At the end of each empirical chapter, add a short transition.

## End of Study 1

Explain that promotion timing alone does not reveal whether organizational movement shapes advancement.

## End of Study 2

Explain that mobility captures organizational movement, while Study 3 examines access to academic resources within and across those career stages.

## End of Study 3

Link results to the General Discussion.

Keep each transition under one paragraph.

---

# 15. Literature review revision

Reduce the number of small literature-review subsections.

Integrate related literatures.

Use theory only where it informs:

- variable selection;
- model design;
- interpretation.

Do not add theory for decorative breadth.

For Study 2, prioritize:

- career mobility;
- gendered organizations;
- linked lives.

For Study 3, prioritize:

- cumulative advantage;
- sociology of science;
- gendered returns to resources.

---

# 16. Citation requirements

Do not invent references.

Verify all references against Zotero or authoritative web sources.

Preserve foundational references where relevant.

Flag any unverified citation in `unresolved_issues.md`.

Create `citation_audit.csv` with:

```text
citation
verified
doi
used_in_text
in_reference_list
notes
```

---

# 17. Visual and structural requirements

Preserve the Tohoku University visual identity on the title page.

Create a formal dissertation-style Table of Contents.

Add:

- List of Tables;
- List of Figures;
- List of Abbreviations.

Ensure chapter numbering is consistent.

Do not use proposal-style milestone tables in the main dissertation body.

Move the work plan to an Appendix or remove it from the dissertation version.

---

# 18. Final quality checks

Before delivery:

1. verify only one formal RQ per study;
2. verify Study 2 focuses on move count and promotion timing;
3. verify Study 3 focuses on KAKEN resources across career stages;
4. verify all old RQ2a–e and RQ3a–d labels are removed;
5. verify no results are fabricated;
6. verify placeholders are clearly marked;
7. verify terminology is consistent;
8. verify engineering detail is moved to Appendix;
9. verify the main text reads as a dissertation, not a data-processing manual;
10. render both DOCX files and visually inspect every page;
11. fix table overflow, broken headings, clipped text, or misplaced captions;
12. confirm tracked and clean versions contain the same substantive text.

---

# 19. Revision memo

In `revision_memo.md`, explain:

- how the research questions were simplified;
- how Study 2 was narrowed;
- how Study 3 was reorganized by career stage;
- which AI-like features were removed;
- which technical details were moved to the Appendix;
- how the document was converted from proposal format into dissertation format;
- which sections still require empirical results.

---

# 20. Final instruction

The goal is not to make the document longer.

The goal is to make it clearer, more scholarly, more selective, and easier to complete as a dissertation.

Use judgment.

Do not preserve unnecessary detail merely because it already exists.

Do not simplify away the core sociology.

Do not invent findings.

Do not change the established names of datasets, ranks, or KAKEN roles without reason.
