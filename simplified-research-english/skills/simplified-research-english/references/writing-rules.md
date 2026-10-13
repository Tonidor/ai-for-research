# The writing rules

This file gives the writing rules of Simplified Research English.
Sections 1 to 9 and the general recommendations follow the 53 rules and 4 recommendations of ASD-STE100 (Issue 7), in the summary of 0xpili/simplified-technical-english.
We changed some rules for research text, and we wrote research examples.
“Change from STE” marks a rule that is different from STE.
Section 10 adds rules for research claims.
The dictionary is in [dictionary.md](dictionary.md).

In the examples, “Not” shows unwanted text, and “Write” shows correct text.

## Contents

- Section 1: Words (rules 1.1 to 1.14)
- Section 2: Noun clusters (rules 2.1 to 2.3)
- Section 3: Verbs (rules 3.1 to 3.7)
- Section 4: Sentences (rules 4.1 to 4.4)
- Section 5: Procedural writing (rules 5.1 to 5.5)
- Section 6: Descriptive writing (rules 6.1 to 6.6)
- Section 7: Cautions and warnings (rules 7.1 to 7.3)
- Section 8: Punctuation and word count (rules 8.1 to 8.7)
- Section 9: Writing practices (rules 9.1 to 9.4)
- General recommendations (GR-1 to GR-4)
- Section 10: Research claims (rules R1 to R8)

There are two types of text:

- **Descriptive text** gives information: papers, reports, notes, summaries, and captions. Most research text is descriptive.
- **Procedural text** tells the reader to do something: setup steps, reproduction steps, and requested changes in a review.

## Section 1: Words

**Rule 1.1:** Use only these words: plain words with one clear meaning, the words of the dictionary, technical names, and technical verbs.
Do not use the words in the “Do not use” columns of the dictionary.
Section 3 of the dictionary gives the vague, inflated, and empty words, and their replacements.
Change from STE: STE has a closed list of approved words. This skill does not.
- Not: “We leverage a robust framework.”
- Write: “We use a model that stays stable when the noise level changes.”

**Rule 1.2:** Use a word only as the part of speech that the dictionary gives.
- Not: “The algorithm reaches convergence after 50 iterations.” (In the dictionary, “converge” is a verb.)
- Write: “The algorithm converges after 50 iterations.”

**Rule 1.3:** Use a word only with its one meaning.
The dictionary gives the meaning of the key words.
Section 6 of the dictionary gives the words that have two meanings in Kai's notes.
- Not: “The solution is efficient.” (Efficient in computation, or in the Pareto sense?)
- Write: “The solution is Pareto efficient.” or “The algorithm runs in linear time.”

**Rule 1.4:** Use only the standard forms of verbs and adjectives. Do not make a comparative of an absolute adjective.
- Not: “a more optimal policy”
- Write: “a policy that is closer to the optimum”

**Rule 1.5:** You can use a word as a technical name when it is a term of mathematics, science, engineering, or computing.
Names of persons, groups, organizations, documents, and parts of documents are also technical names.
Numbers, units of measurement, and times are also technical names.
Change from STE: STE gives 19 categories of technical names.

**Rule 1.6:** You can use a word from a “Do not use” column only when it is a part of a technical name.
- Permitted: “dominant strategy” (a term of game theory)
- Not: “the strategy of the agent”
- Write: “the policy of the agent”

**Rule 1.7:** Do not use a technical name as a verb.
- Not: “We Nash-solve the game.”
- Write: “We compute the Nash equilibrium of the game.”

**Rule 1.8:** Use the technical names that agree with the nomenclature of the field.
Section 4 of the dictionary gives the technical names of Kai's field.
If a term is not in the dictionary, use the standard term of the field.
Define the term at first use, and propose the term as a dictionary entry.

**Rule 1.9:** When you must select a technical name, select a name that is short and easy to understand.

**Rule 1.10:** Do not use slang or jargon as technical names.
- Not: “the knob of the controller”
- Write: “the gain of the controller”

**Rule 1.11:** Use only one technical name for one item. Do not change between names for variety.
- Not: “Each agent chooses an action.” “Then every player receives a reward.”
- Write: “Each agent chooses an action.” “Then every agent receives a reward.”

**Rule 1.12:** You can use a technical verb when no common verb has the same meaning.
Section 5 of the dictionary gives the technical verbs of Kai's field.
Use a common verb if one is available.
- Not: “If you detect broken links, repair them.”
- Write: “If you find broken links, repair them.”

**Rule 1.13:** Do not use a technical verb as a noun.
The past participle of a technical verb is permitted as an adjective, for example “the estimated parameters”.

**Rule 1.14:** Use American English spelling. Write “behavior”, not “behaviour”.

## Section 2: Noun clusters

**Rule 2.1:** Write noun clusters of maximum three words. Articles and prepositions do not count. Break long clusters with prepositions.
- Not: “the controller gain update rule”
- Write: “the update rule for the controller gain”

**Rule 2.2:** When a technical name has more than three words, write the full name one time. Then give a short name, and define the short name at first use.
- Write: “the alternating direction method of multipliers (ADMM)”, and after that “ADMM”

You can also put hyphens between the words that make one unit, for example “closed-loop transfer function”.
Do not put hyphens between more than three words.

**Rule 2.3:** Use an article (“the”, “a”, “an”) or “this” or “these” before a noun.
Do not remove these words to make a sentence shorter.
Exception: do not use “the” before a noun with an identifier. Write “Theorem 2” and “agent $i$”.
- Not: “Controller with higher gain reacts faster.”
- Write: “A controller with a higher gain reacts faster.”

## Section 3: Verbs

**Rule 3.1:** Use only the verb forms that rule 3.2 permits. For a technical verb, use only the meaning that the dictionary gives.

**Rule 3.2:** Use only these verb forms: infinitive, imperative, simple present, simple past, past participle as an adjective, and future.
All other tenses are not permitted. Use the tenses as follows:
- The simple present for facts, for results, and for what the document does: “Theorem 2 shows that the equilibrium exists.”
- The simple past for a specified past action: “We ran 50 simulations.” “Smith (2020) proposed the method.”
- The future with “will” only for planned work: “We will test the policy on real data.”

Use only “can”, “must”, and “will” as helping verbs.
Use “can” for a possibility or an ability, “must” for a necessity, and “will” for the future.
Do not use “should”, “would”, “may”, “might”, “shall”, or “ought”.
Use “could” only as the past tense of “can”.
To show uncertainty, use an evidence word (rule R1).
- Not: “The policy may reduce delays.”
- Write: “The results suggest that the policy reduces delays.”
- Not: “Without feedback, the error would grow.”
- Write: “If there is no feedback, the error grows.”

Change from STE: in working notes, for example brainstorming notes and meeting notes, you can use “might” for open speculation. Papers and reports use only evidence words.

**Rule 3.3:** Use the past participle only as an adjective, before a noun or after “to be” or “to become”.
This use shows a condition and is not the passive voice.
- Permitted: “The constraint is satisfied.”

**Rule 3.4:** Do not use helping verbs to make complex verb structures.
- Not: “Prior work has shown that the iterates converge.”
- Write: “Smith (2020) showed that the iterates converge.”
- Not: “The equilibrium can be computed by value iteration.”
- Write: “We can compute the equilibrium by value iteration.”
- Not: “The policy is expected to be able to reduce delays.”
- Write: “We expect that the policy reduces delays.”

**Rule 3.5:** Use the “-ing” form only as a modifier in a technical name or in a title.
Technical names are permitted, for example “learning rate” and “sampling time”.
The other permitted “-ing” words are the STE words “during”, “missing”, “remaining”, “opening”, “routing”, “lighting”, “mating”, and “servicing”.
- Not: “Using the new controller, the overshoot decreases.” (Who uses the controller?)
- Write: “When the operator uses the new controller, the overshoot decreases.”

**Rule 3.6:** Use the active voice in procedural text. Use the active voice as much as possible in descriptive text.
Do not use the passive voice to hide who did something.
- Make the agent the subject: “The controller rejects the disturbance.”
- Use the imperative: “Run the script again.”
- If there is no other agent, use “we” (the authors) as the subject.
- Not: “It was found that the iterates converge.”
- Write: “We found that the iterates converge.”

**Rule 3.7:** Use a verb to show an action. Do not use a noun or another part of speech.
- Not: “We perform an evaluation of the controller.”
- Write: “We evaluate the controller.”

## Section 4: Sentences

**Rule 4.1:** Write short and clear sentences. Give specific information. Write only one topic in each sentence.
- Not: “The results are good.”
- Write: “The mean computation time decreases by 12%.”

**Rule 4.2:** Keep all the necessary words. Do not use contractions.
- Keep the subject, the verb, and the articles.
- Keep “that” after verbs such as “show”, “find”, “assume”, and “expect”.
- Not: “We show the equilibrium exists.”
- Write: “We show that the equilibrium exists.”
- Write “do not”, not “don't”.

**Rule 4.3:** Use a vertical list for complex text, for example for three or more parallel items that each need a clause.
Put a colon at the end of the first line.
In a list of commands with “not”, write “not” again in each item.
Change from STE: in paper prose, an inline list with (i), (ii), and (iii) is also permitted.

**Rule 4.4:** Use connecting words to connect sentences with related topics.
Section 2 of the dictionary gives one meaning for each connecting word:
- “thus” for a logical result
- “as a result” for an effect
- “but” for a contrast
- “because” for a cause
- “then” for the next step

## Section 5: Procedural writing

**Rule 5.1:** Write short sentences. Use a maximum of 20 words in each sentence. This limit also applies to cautions and warnings.

**Rule 5.2:** Write only one instruction in each sentence. Two or more actions in one sentence are permitted only when they occur at the same time.

**Rule 5.3:** Write each instruction in the imperative.
- Write: “Set the random seed to 7.”

**Rule 5.4:** When a condition or a description comes before a command, put a comma between the two.
- Write: “If the solver does not converge, decrease the step size to 0.01.”

**Rule 5.5:** Write a note only to give information. A note must not give an instruction or a requirement.
If the information prevents data loss or results that are not valid, write a caution.
A note has a maximum of 25 words.

## Section 6: Descriptive writing

**Rule 6.1:** Give information gradually. Introduce an object before you use the object. Put the claim before its details.

**Rule 6.2:** Use key words and connecting words to make the structure of the text clear.
Use the same key word again in the sentence that follows.
Do not replace the key word with a synonym or with an unclear pronoun.

**Rule 6.3:** Write short sentences. Use a maximum of 25 words in each sentence.

**Rule 6.4:** Use paragraphs to show related information. Start each paragraph with a topic sentence. The other sentences give more data about the topic.

**Rule 6.5:** Write only one topic in each paragraph.

**Rule 6.6:** Write a maximum of six sentences in each paragraph.

## Section 7: Cautions and warnings

A caution shows a risk of data loss, or a risk of results that are not valid.
A warning shows a risk of injury or death to persons, for example in lab work.
Change from STE: in STE, a caution shows a risk of damage to objects.

**Rule 7.1:** Use “CAUTION” or “WARNING” to show the level of risk.

**Rule 7.2:** Start a caution or a warning with a clear and simple command or condition.

**Rule 7.3:** Give an explanation of the risk or of the possible result.
- Write: “CAUTION: Make a copy of the results folder before this step.” “The script overwrites all previous runs.”

## Section 8: Punctuation and word count

**Rule 8.1:** You can use all the standard English punctuation marks, but not the semicolon. Write two sentences, or join the clauses with a connecting word.

**Rule 8.2:** Use hyphens to connect words that are closely related, for example in a compound modifier.
- Write: “a closed-loop system”, “a two-player game”, “the long-run average”

**Rule 8.3:** You can use parentheses for a symbol, an abbreviation, a citation, a reference, a short explanation, or an alternative.
Do not put an argument in parentheses.
- Write: “the alternating direction method of multipliers (ADMM)”, “the discount factor ($\gamma$)”, “(refer to Figure 3)”

**Rule 8.4:** In a vertical list, a colon has the same effect on the word count as a full stop. Each item of the list counts as a new sentence.

**Rule 8.5:** Text in parentheses counts as one word in its sentence. The same text also counts separately as its own sentence.

**Rule 8.6:** Each of these items counts as one word:
- a number, or a number with its unit
- an abbreviation, an acronym, or an identifier
- an inline formula, or a citation
- quoted text, or the title of a work

**Rule 8.7:** A hyphenated group counts as one word. For example, “closed-loop transfer function” counts as three words.

## Section 9: Writing practices

**Rule 9.1:** When a word-for-word replacement does not give a clear sentence, use a different construction.
Make sure that the new sentence keeps the correct meaning.
The primary objective is that the reader immediately understands each sentence.

**Rule 9.2:** Use each word correctly. Read the meaning in the dictionary before you use a key word.
- “efficiency” is only allocative or Pareto efficiency. For a physical ratio, write “energy efficiency”.
- “stage” is only a stage of a Markov decision process. For a part of a project, write “phase”.

**Rule 9.3:** Do not put two words together to make a phrasal verb.
- Not: “We set up the simulation and carry out 50 runs.”
- Write: “We configure the simulation and run it 50 times.”

**Rule 9.4:** Use a consistent style. Use the same words for the same type of statement, and the same name for the same item.
In descriptive text, changes of construction are permitted to make the text easy to read.
- Write each result as: “In [scope], [method] changes [metric] by [amount] relative to [baseline].”

## General recommendations

**GR-1:** Keep the conjunction “that” after verbs such as “make sure”, “show”, “find”, and “assume”.

**GR-2:** The preposition “with” can make a sentence unclear.
If “with” can mean “that has”, “together with”, or “by means of”, write the exact phrase.
- Not: “We train the policy with the simulation data.”
- Write: “We use the simulation data to train the policy.”

**GR-3:** If a pronoun can refer to more than one noun, replace the pronoun with the noun.

**GR-4:** Always put a noun after “this” and “these”. If “this” can refer to more than one thing, give the full context again.
Change from STE: STE asks for the noun only when “this” is not clear.
- Not: “The controller saturates the input at each step.” “This keeps the state bounded.”
- Write: “The controller saturates the input at each step.” “This saturation keeps the state bounded.”

## Section 10: Research claims

These rules are not in STE. They make the strength and the scope of each claim clear.

**Rule R1:** Use the evidence words of the dictionary to show how strong each claim is. Use one evidence word for each claim. Do not put two hedges together.
- Not: “The results may possibly indicate that the iterates converge.”
- Write: “The results suggest that the iterates converge.”

**Rule R2:** Give the scope of each result: the model, the scenario, the calibration or the dataset, and the units. Do not make a claim that is larger than this scope.

**Rule R3:** Name the object before its symbol at first use. Give each symbol one meaning in a document. Section 7 of the dictionary gives the default symbols.
- Write: “the discount factor $\gamma$ of the agent”

**Rule R4:** In a comparison, name the two sides and the metric.
- Not: “The new solver performs better.”
- Write: “The new solver decreases the mean computation time by 12% relative to the interior-point method.”

**Rule R5:** Replace a vague qualifier with the criterion or the number. Use “significant” only for a statistical test, and name the test.

**Rule R6:** Put the citation immediately after the claim that the citation supports.

**Rule R7:** Do not use Latin abbreviations in prose. Write “for example” and “that is”. Instead of “etc.”, give all the items. Use “et al.” only in citations.

**Rule R8:** Use the possessive form only for persons, agents, and organizations.
- Not: “the game's equilibrium's welfare”
- Write: “the welfare at the equilibrium of the game”
