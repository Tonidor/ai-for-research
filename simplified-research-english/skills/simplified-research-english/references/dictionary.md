# Dictionary

Each entry gives one word, its type, its one meaning, and the words that you must not use for that meaning. Use the word in the first column.

A word that is not in this dictionary is acceptable if it is plain English and has one clear meaning in its sentence. Unlike ASD-STE100, this dictionary has no closed list of general words.

How to edit this file:

- Keep the column names. [check.py](../scripts/check.py) reads every table that has a “Do not use” column.
- Separate the items in “Do not use” with commas. Add “?” after an item to make it a hint, not an error, for words that also have an acceptable use.
- Mark an entry that Kai did not confirm with “(provisional)” in its meaning.

## 1. Evidence words

Use these words to show how strong a claim is (rule R1). Each word has one level.

| Word | Type | Meaning | Do not use |
|---|---|---|---|
| prove | evidence verb | A mathematical proof is in this document or in a cited source. | |
| show | evidence verb | Direct evidence supports the claim in its stated scope: a proof, a complete experiment, or a computation. | demonstrate, establish, reveal |
| suggest | evidence verb | Some evidence supports the claim, but the evidence does not settle it. For example, one calibration or a small number of runs. | indicate, point to |
| expect | evidence verb | An argument supports the claim, but there is no evidence yet. | anticipate, presumably |
| conjecture | evidence verb | We think that a mathematical statement is true, but we cannot prove it yet. | |
| assume | evidence verb | The model takes the statement as given. It is not a claim about the world. | posit, presume |
| according to | evidence phrase | A source states the result, and we did not check the result. Write “according to Smith (2020), ...”. | |
| unknown | evidence adjective | No evidence supports or rejects the claim. | |
| (delete, or give the evidence) | | | clearly, obviously, evidently, undoubtedly, certainly |
| can, or an evidence word | | See rule 3.2. | may, possibly, potentially, probably, maybe, seem? |
| can, or an evidence word | | See rule 3.2. In working notes, “might” is allowed for open speculation. | might |

## 2. Connecting words and function words

Each word has one meaning. Use these words to connect sentences (rule 4.4).

| Word | Type | Meaning | Do not use |
|---|---|---|---|
| because | connecting word | A cause. | due to the fact that, owing to |
| (because for a cause, from for a start time) | | | since |
| thus | connecting word | A logical result of the previous statement. | hence, therefore, consequently, thereby, accordingly |
| as a result | connecting phrase | An effect that the previous event causes. | |
| but | connecting word | A contrast. | however, whereas, nevertheless, nonetheless |
| although | connecting word | A fact that does not stop the main statement from being true. | albeit, even though |
| then | connecting word | The next step in a sequence. | subsequently, thereafter |
| also | connecting word | An addition. | moreover, furthermore, additionally |
| for example | connecting phrase | An example follows. | e.g., for instance |
| against, or compared with | function word | A comparison of two things. | v.s., vs. |
| with respect to | function word | In relation to a variable. | w.r.t., w.r.t |
| that is | connecting phrase | The same statement in different words follows. | i.e., namely |
| if | connecting word | A condition. | provided that, in case |
| when | connecting word | A time, or a condition that occurs again and again. | whenever |
| (when for a time, but for a contrast) | | | while |
| through | function word | By means of, or along a route. | via |
| about | function word | On the topic of. Do not use it for numbers. | regarding, concerning, with regard to |
| approximately | function word | Near a number. | roughly, circa |
| to | function word | A purpose. | in order to, so as to |
| (give all the items) | | | etc. |
| (write each pair in full) | | | respectively |
| (write the noun again) | | | the former, the latter |

## 3. Words to avoid

These words are vague, inflated, or empty (rule 1.1). Write the replacement in the first column.

| Write instead | Meaning | Do not use |
|---|---|---|
| use | Apply a thing for a purpose. | utilize, leverage, employ, make use of |
| examine | Study a thing in detail. | delve, delve into |
| take into account | Include a thing in a decision or a model. | cater for |
| allow | Make a thing possible. | facilitate, enable |
| help | Make a thing easier. | foster, empower |
| many, or the number | A large number. | numerous, a plethora of, a myriad of |
| some, or the number | An unknown small number. | a number of, various, a variety of |
| show, or give | Make a thing visible. | showcase, underscore, highlight? |
| (state the property and its size) | | robust?, powerful, seamless, comprehensive, holistic, novel, innovative, groundbreaking, cutting-edge |
| (delete, or say why it matters) | | crucial, vital, pivotal, paramount, notably, importantly, interestingly, remarkably |
| (state the amount, or name the statistical test) | | significant?, significantly? |
| (delete) | | it is worth noting that, it should be noted that, it is important to note that, in fact, needless to say, as a matter of fact |
| (state the specific relation) | | plays a role in, in terms of, landscape, realm, tapestry, paradigm shift, unlock, harness |

## 4. Technical names

The nouns of Kai's research field (rule 1.8). The meanings come from Kai's notes and Zotero library (October 2026). The symbol is the default. In a document, each symbol has only one meaning (rule R3).

| Word | Type | Meaning | Symbol | Do not use |
|---|---|---|---|---|
| Karma | technical name | The non-tradable artificial currency that agents hold, bid, pay, and receive. Use it as a mass noun: “10 Karma”. Write it with a capital K, also in the middle of a sentence. In a quoted title, keep the original case. For the mechanism, write “the Karma mechanism”, not “Karma”. | | Karma points, `karma` |
| Karma mechanism | technical name | The rules of one Karma economy: the allocation rule, the payment rule, and the redistribution rule. | | |
| Karma economy | technical name | A population that uses one Karma mechanism for one resource over time. | | |
| agent | technical name | One decision maker that holds Karma and bids for the resource. For an AI system, write “LLM agent” or “AI agent” in full. | $i$, number $N$ | user?, player?, participant?, individual?, bidder?, stakeholder? |
| population | technical name | All agents of the model, finite or a continuum. Use “society” only in a normative statement. | | |
| resource | technical name | The scarce thing that the mechanism allocates in each round. | | |
| round | technical name | One allocation event. | index $t$ | time step? |
| urgency | technical name | The private value that an agent gets from the resource in one round. | $u_i$ | priority? |
| urgency process | technical name | The Markov chain that changes the urgency of an agent over time. | $\phi_\tau[u^+ \mid u]$ | |
| preference | technical name | The full private information that elicitation tries to get (provisional). | | |
| type | technical name | The fixed private class of an agent: its urgency process, its discount factor, and its rewards. | $\tau$ | |
| state | technical name | The private state of one agent: its urgency and its Karma balance. For the population, write “social state”. | $x = (u, k)$ | |
| social state | technical name | The distribution of the population over types and states, together with the policy. | $(d, \pi)$ | |
| Karma balance | technical name | The Karma that one agent holds now. | $k_i$, $k_i^t$ | Karma account, wealth? |
| total Karma | technical name | The sum of all Karma balances. Redistribution keeps it constant. | $K^{\mathrm{tot}}$ | |
| Karma cap | technical name | The maximum Karma balance of one agent. | $k_{\max}$ | |
| bid | technical name | The Karma that an agent offers in one round. A bid is at most the Karma balance. | $b_i \le k_i$ | |
| bidding policy | technical name | The map from the state of an agent to a distribution of bids. For a planner, write “control policy”. | $\pi_i(b \mid u, k)$ | bid policy, bidding strategy, strategy? |
| allocation | technical name | The act of giving the resource to agents. Use “dispatch” only for taxi and energy dispatch. | | assignment? |
| allocation rule | technical name | The rule that gives the resource from the bids. The highest bid wins, and the tie-breaking rule decides ties. | | |
| payment rule | technical name | The rule that sets the Karma that a winner pays: first price, second price, or peer-to-peer. | | |
| tie-breaking rule | technical name | The rule that decides between equal bids. | | |
| clearing price | technical name | The lowest winning bid of a round. Under uniform pricing, every winner pays it. | $p^\star$ | clearing bid, threshold bid |
| pot | technical name | The collected Karma payments of one round, before redistribution (provisional). | $P_t$ | surplus?, income? |
| redistribution | technical name | The return of the pot to the agents. | $r_i(t)$ | |
| redistribution rule | technical name | The rule that sets the share of the pot that each agent receives. | | |
| redistribution weight | technical name | The relative claim of an agent on the pot. Do not shorten it to “weight”. | $\theta_i$ | redistribution share, entitlement?, access right? |
| uniform redistribution | technical name | Redistribution with equal redistribution weights. | $P_t / N$ | |
| access rate | technical name | The long-run fraction of rounds in which an agent gets the resource. | $A_i$ | win rate, serve rate, service rate, access share |
| win probability | technical name | The probability that an agent gets the resource in one round, for a given bid. | | winning probability |
| capacity | technical name | The amount of the resource in one round. For a fraction of the population, write “capacity fraction”. | $C$; fraction $\lambda$ | |
| discount factor | technical name | The weight that an agent gives to future rewards. | $\gamma$ | |
| reward | technical name | The gain of an agent in one round: its urgency if the agent gets the resource. | $R_i$ | payoff?, satisfaction?, benefit? |
| utility | technical name | The long-run expected reward of one agent (provisional). | $U_i$ | |
| welfare | technical name | The value that a social welfare function computes from the utilities of all agents (provisional). | $W$ | |
| social welfare function (SWF) | technical name | A rule that combines the utilities of all agents: utilitarian, Nash, maximin, or α-fair. | $W$ | |
| Nash welfare | technical name | The sum of the logarithms of the agent utilities. Do not write “Nash” alone. | | Nash social welfare, log welfare |
| long-run Nash welfare (LNW) | technical name | The Nash welfare of the long-run average rewards. MLNW is its maximization. | | |
| weighted Nash welfare (WN) | technical name | The Nash welfare with a Nash weight for each agent. | | |
| Nash weight | technical name | The weight of an agent in weighted Nash welfare. It is a different object from the redistribution weight. | $w_i$ | welfare weight? |
| constrained Nash (CN) | technical name | The Nash welfare problem with added constraints on the access rates. | $h(A) \le 0$ | |
| Karma user problem (KU) | technical name | The problem of one agent: maximize its utility subject to the long-run budget constraint. | | |
| stationary Nash equilibrium (SNE) | technical name | A stationary state distribution and a policy profile in which each bidding policy is a best response. Do not write “equilibrium” alone in Karma text. | | |
| Karma equilibrium (KE) | technical name | Each agent solves KU, the resource clears, and every budget balances. It is a different concept from SNE. | | |
| value function | technical name | The expected discounted reward from a state. | $V_\tau[u, k]$ | |
| shadow price | technical name | The multiplier of the Karma budget constraint, that is, the marginal value of Karma. | $\kappa_i$ | |
| hard budget | technical name | A budget that must balance in each round. | | |
| long-run budget constraint | technical name | A budget constraint on long-run averages only. | | |
| auto-bidder | technical name | Software that bids for an agent from the type that the agent reports. | | autobidder, auto bidder, bidding agent, automated bidder |
| direct mechanism | technical name | A mechanism in which agents report their types. In an indirect mechanism, agents submit bids. | | |
| incentive compatible (IC) | technical name | No agent gains from a false report. Use “strategy-proof” only for the dominant-strategy version, and “truthful” only for a report. | | |
| comparability | technical name | The property that the utility scales of different agents can be compared. | | |
| α-fairness | technical name | A family of social welfare functions. α = 0 is utilitarian, α = 1 is Nash, and α → ∞ is maximin. Always give the criterion of fairness. | $\alpha$ | |
| maximin | technical name | The social welfare function that maximizes the minimum utility. | | maxmin, max-min |
| monotonicity | technical name | The property that the access rate increases when the redistribution weight increases. | | |
| feedback tuning | technical name | The change of the redistribution weights in a closed loop, from observed signals. | | |
| signal | technical name | An observed outcome that feedback tuning uses, for example the access rate. | | |
| coalition | technical name | A set of agents that act together in the mechanism. | size $m$ | |
| hoarding | technical name | Keeping Karma without spending it, to gain from redistribution or from ties. | | |
| market power | technical name | The effect of one agent on the clearing price when there are few agents. | | |
| elicitation | technical name | Getting the private information of agents. | | |
| designer | technical name | The person who sets the rules of the mechanism. | | system designer, mechanism designer |
| operator | technical name | The entity that runs the mechanism in each round. | | central controller |
| planner | technical name | The optimizer with full information that serves as a benchmark. | | social planner |

## 5. Technical verbs

The verbs of Kai's research field (rule 1.12).

| Word | Type | Meaning | Do not use |
|---|---|---|---|
| allocate | technical verb | Give the resource to agents in a round. | assign? |
| bid | technical verb | Offer Karma for the resource. | |
| win | technical verb | Get the resource in a round. The opposite is “lose”. | |
| pay | technical verb | Give Karma for the resource that the agent won. | spend? |
| collect | technical verb | Put the payments of all winners into the pot. | |
| redistribute | technical verb | Give the pot back to the agents by the redistribution rule. | |
| receive | technical verb | Get Karma from redistribution. | |
| yield | technical verb | Let other agents get the resource now, to keep Karma for later rounds. For the sense “produce”, write “give” (provisional). | |
| consume | technical verb | Use the resource in a round. | |
| converge | technical verb | Reach an equilibrium in learning or in a solver. | |
| tune | technical verb | Change the redistribution weights from feedback. | adapt? |
| implement | technical verb | Cause an outcome through a mechanism: “the Karma mechanism implements Nash welfare”. For software, write “code” or “program” (provisional). | |
| approximate | technical verb | Implement an outcome only in a limit, for example in a large population. | |
| induce | technical verb | Cause an outcome as an effect of the equilibrium. | |
| maximize | technical verb | Choose the option with the highest value of the objective. | |
| elicit | technical verb | Get private information from agents. | |
| report | technical verb | Give a type to a direct mechanism or to an auto-bidder. | |
| learn | technical verb | Estimate a bidding policy or a parameter from data. Agents and auto-bidders learn. The designer tunes. | |
| break ties | technical verb | Choose between equal bids. | |
| steer | technical verb | Move an equilibrium by design. | |
| internalize | technical verb | Make agents carry the cost of an externality. | |

## 6. Words with two meanings in Kai's notes

Use each word only for the meaning in the second column (rule 1.3). The checker cannot see meanings, so check these words when you read the text again.

| Word | Use only for | For the other meaning, write |
|---|---|---|
| efficiency | Allocative or Pareto efficiency. Always give the type. | “charging efficiency” or “energy efficiency” for a physical ratio |
| price | The clearing price, or the shadow price, always with its full name | “first-price” or “second-price” for an auction format |
| budget | The long-run budget constraint or the hard budget, always with its full name | “money budget” for advertisers |
| balance | The Karma balance | “budget balance” when payments equal redistribution |
| weight | Do not use it alone | “redistribution weight” or “Nash weight” |
| value | Do not use it alone | “value function”, or “shadow price” for the marginal value of Karma |
| access | Getting the resource | “information about” for information |
| income | Do not use it in Karma text | “redistributed Karma”. Use “income” only for money. |
| stage | An MDP stage | “phase” for a project phase |
| proxy | A measurable stand-in for a quantity that you cannot observe | “auto-bidder” for the software that bids for an agent |
| mechanism | An allocation mechanism | “process” for a causal process |
| capacity | The amount of the resource in one round | “capacity fraction” for a fraction |

## 7. Symbols

The default symbols for Kai's Karma work (rule R3). In Kai's notes, these symbols also have other meanings. In each document, give a symbol only one meaning.

| Concept | Default symbol | Other symbols in Kai's notes |
|---|---|---|
| urgency | $u_i$ | $u$ also for utility and for a control input |
| redistribution weight | $\theta_i$ (provisional) | $w_i$. $\theta$ also for type, demand level, and item quality. |
| Nash weight | $w_i$ | |
| type | $\tau$ | $\theta$, $i$ |
| discount factor | $\gamma$ (provisional) | $\alpha_i$, $\alpha_\tau$, $\delta$, $\beta$. $\alpha$ is for α-fairness. |
| total Karma | $K^{\mathrm{tot}}$ | $K$ also for the Karma cap |
| Karma cap | $k_{\max}$ | $K^{\mathrm{cap}}$, $K$ |
| capacity | $C$; fraction $\lambda$ | $\lambda$ also for multipliers and arrival rates |
| access rate | $A_i$ (provisional) | $a_i$ |
| clearing price | $p^\star$ (provisional) | $b^{\theta,*}$, $b^*$, $b^\star$ |
| utility | $U_i$ | $V_i$, $u_i$, $J_i$ |

## 8. Spelling

| Write | Meaning | Do not use |
|---|---|---|
| long-run | The adjective for long-run averages. As a noun, write “in the long run”. | long-term? |
| strategy-proof | | strategyproof |
| mean-field | | |
| two-sided | | double-sided |
| non-comparable | | noncomparable |
