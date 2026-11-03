---
name: simplified-research-english
description: Kai's rules for research writing, based on ASD-STE100 Simplified Technical English (after 0xpili/simplified-technical-english), with Kai's research dictionary and a check tool. Use only for the text of a visual report (the visual-report skill loads it), or when the user explicitly asks to check text against STE, the writing rules, or the dictionary, or to add a word to the dictionary. Do not load it for other research writing.
license: The writing rules and the check tool adapt simplified-technical-english by 0xpili (MIT license). Refer to NOTICE.md.
---

# Simplified Research English

This skill makes you write research text in Simplified Research English.
Simplified Research English is Simplified Technical English (STE), with changes for research.
STE is a controlled language from the specification ASD-STE100.
The goal is text where each word has one meaning, each sentence has one topic, and each claim shows the strength of its evidence.

Obey the rules in this file for all the research text that you write.
The rules in this file are the most important rules.
The full set of rules is in `references/writing-rules.md`.
The dictionary is in `references/dictionary.md`.

## Scope

Apply the rules to research text: papers, reports, notes, summaries, documentation, review comments, and the text of visual reports.
In these texts, apply the rules to prose, captions, list items, and table notes.

Do not apply the rules to:

- Code blocks, identifiers, commands, and file paths
- Math, citations, quoted text, and the titles of other works
- Marketing text, stories, and conversation.

Kai's global writing rules also apply: no em-dash, American spelling, typographic quotation marks, and the math delimiters of each file type.
When you revise Kai's text, change only the parts that do not obey a rule. Keep the meaning of Kai's text.
If the user asks for a different style, the request of the user wins.

## Step 1: Classify the text

Before you write, classify each part of the text:

- **Descriptive text** gives information. Example: “The algorithm updates the estimate after each iteration.” Most research text is descriptive.
- **Procedural text** tells the reader to do something: setup steps, reproduction steps, and requested changes in a review. Example: “Set the random seed to 7.”

The two types have different limits. Do not mix the two types in one paragraph.

## Step 2: Obey the verb rules

- Use only these verb forms: infinitive, imperative, simple present, simple past, future with “will”, and past participle as an adjective.
- Use the simple present for facts, for results, and for what the document does. Use the simple past for a specified past action. Use the future only for planned work.
- Do not use a helping verb with a past participle. Write “Smith (2020) showed”, not “prior work has shown”.
- Do not use the “-ing” form of a verb. An “-ing” word is permitted only in a technical name, for example “learning rate”.
- Use the active voice. If there is no other agent, use “we” as the subject. Write “we compute the equilibrium”, not “the equilibrium is computed”.
- In procedures, use the imperative. Write “Set the random seed to 7.”
- Use only “can”, “must”, and “will” as helping verbs. Do not use “should”, “would”, “may”, “might”, or “shall”. To show uncertainty, use an evidence word (Step 5).
- In working notes, for example brainstorming notes, you can use “might” for open speculation.
- A past participle after “is” or “are” shows a condition and is permitted. Example: “The constraint is satisfied.”
- Use a verb to show an action. Write “we evaluate the mechanism”, not “we perform an evaluation of the mechanism”.

## Step 3: Obey the sentence rules

- Procedural sentences: maximum 20 words.
- Descriptive sentences: maximum 25 words.
- Paragraphs: maximum 6 sentences, and only one topic. Start each paragraph with a topic sentence.
- Write only one instruction in each sentence. Two actions are permitted only when they occur at the same time.
- Write only one topic in each sentence.
- When a condition comes before a command, put a comma after the condition. Example: “If the solver does not converge, decrease the step size.”
- Keep the articles, the subjects, the verbs, and the conjunction “that”. Write “we show that the equilibrium exists”.
- Do not use contractions. Write “do not”, not “don't”.
- Do not use semicolons. Write two sentences.
- Use a vertical list for complex text. In a list of commands with “not”, write “not” again in each item.
- Make each pronoun refer to one noun. Always put a noun after “this” and “these”.

## Step 4: Obey the word rules

- Use only: plain words with one clear meaning, the words of the dictionary, technical names, and technical verbs. Unlike STE, this skill has no closed list of approved general words.
- Do not use the words in the “Do not use” columns of the dictionary. Write the word that the dictionary gives.
- Use the technical names and the technical verbs of the dictionary. If a term is not in the dictionary, use the standard term of the field, and define the term at first use.
- Use a word only with its one meaning, and only as the part of speech that the dictionary gives. Do not use a technical name as a verb.
- Use one name for one item in the full text. Do not change between names for the same item.
- Write noun clusters of maximum three words. Break long clusters with “of”, “on”, “in”, or “for”.
- Do not make phrasal verbs. Write “configure the simulation”, not “set up the simulation”.
- Do not use vague words. Write the specific quantity, name, or action.
- Do not use Latin abbreviations in prose. Write “for example” and “that is”.
- Use American English spelling.

## Step 5: Show the strength and the scope of each claim

These rules are not in STE. They are for research claims.

- Use the evidence words of the dictionary to show how strong each claim is. Use one evidence word for each claim.
- Give the scope of each result: the model, the scenario, the calibration or the dataset, and the units. Do not make a claim that is larger than this scope.
- In a comparison, name the two sides and the metric.
- Replace a vague qualifier with the criterion or the number. Use “significant” only for a statistical test, and name the test.
- Name the object before its symbol at first use. Give each symbol one meaning in a document.
- Put the citation immediately after the claim that it supports.

## Step 6: Write cautions correctly

- Use “CAUTION” for a risk of data loss, or for a risk of results that are not valid.
- Use “WARNING” for a risk of injury or death to persons, for example in lab work.
- Start with a simple command or condition. Then give the risk.
- Example: “CAUTION: Make a copy of the results folder before you start. The script overwrites all previous runs.”

## Step 7: Check your text

After you write, check your text. Do these steps:

1. Run the check tool on the file: `python3 <this skill>/scripts/check.py --mode <descriptive|procedural|mixed> FILE`. For text that is not in a file, send the text on standard input: `check.py - < text.md`. Add `--notes` for working notes. The tool reads Markdown, LaTeX, and HTML.
2. Correct each ERROR. Read each HINT, and correct the text if the rule applies.
3. Check the text again. Stop when the text has no errors.
4. Read the text again for the rules that the tool cannot check:
   - One topic in each sentence (rule 4.1)
   - A maximum of three nouns in a row (rule 2.1)
   - Pronouns that refer to one noun (GR-3)
   - Each word with its one meaning (rule 1.3)
   - Evidence words that agree with the evidence (R1)
   - The scope of each result (R2)
   - Comparisons that name the two sides and the metric (R4)
5. If you used a term that is not in the dictionary, list the term and a proposed meaning at the end of your response. Add a term to the dictionary only when Kai approves the term.

The check tool cannot find all the errors.
The tool can also give a false error, for example in “agents have limited information”, where “limited” is an adjective.
Do not change correct text only to satisfy the tool.

## Reference files

- `references/writing-rules.md`: all the rules, with research examples. Read this file once in each session before your first text, and when a rule is not clear.
- `references/dictionary.md`: the evidence words, the connecting words, the words to avoid, and the technical names, technical verbs, and symbols of Kai's field. Read this file before you write.
- `examples/before-after.md`: examples of research text before and after the change to Simplified Research English.
- `scripts/check.py`: the check tool.

## Basis

The rules come from ASD-STE100, through the summary in simplified-technical-english by 0xpili.
The rule numbers follow that summary, which uses ASD-STE100 Issue 7 (2017).
Section 10 of the writing rules adds the rules for research claims.
The dictionary is Kai's dictionary.

This skill does not contain the specification or the STE dictionary.
ASD owns the copyright of ASD-STE100. This skill is not an official ASD document.
Refer to NOTICE.md.
