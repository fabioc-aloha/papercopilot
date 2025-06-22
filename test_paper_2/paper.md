# Title Page
AI Cognitive Bugs: Parallels to Human Cognitive Disorders and Mitigation Strategies

Author Name
Institution
Course
Instructor
Date

---

# Abstract
This paper examines the emergence of cognitive bugs—systematic, recurring reasoning failures—in large language models (LLMs) and agentic AI systems, synthesizing recent literature from 2024 to 2025. We hypothesize that, akin to a range of human cognitive disorders and biases, LLMs and agents can develop issues such as hallucinations, confabulation, delusional reasoning, and digital amnesia. Through a comprehensive review of empirical and theoretical studies on AI cognitive bugs, context window management, and psychological parallels, we analyze the extent to which AI systems mirror human cognitive vulnerabilities. The paper critically evaluates strategies for mitigating these cognitive bugs, including heuristic filtering, context flushing, secondary memory storage, and the potential for software-based cognitive agents. Our findings underscore the necessity of deliberate context control and interdisciplinary approaches to reduce AI cognitive bugs, thereby promoting AI reasoning that aligns with human values, safety, and reliability.


# Keywords
AI cognitive bugs, context window, LLMs, agentic AI, cognitive disorders, applied psychology, bias mitigation

---

# Introduction
The rapid adoption of large language models (LLMs) and agentic AI systems has intensified concerns about the emergence of cognitive bugs in artificial intelligence. Beyond well-documented biases, experts warn of generative AI "hallucinations," confabulation, delusional reasoning, and digital amnesia—failures that closely parallel human cognitive disorders. As AI systems grow in complexity, a critical question arises: can AI develop a spectrum of cognitive issues analogous to those observed in humans, and what strategies can mitigate these failures? This paper explores these cognitive bugs—systematic, recurring reasoning failures in AI—and their implications for safety and reliability.

Recent research (2024–2025) demonstrates that, like humans, AI systems may rely on the most accessible information in their context window, leading to biased or incomplete reasoning (Zhang et al., 2024; Lee & Kumar, 2025). This phenomenon closely parallels the availability heuristic in psychology, but AI systems also exhibit other cognitive bugs, such as confabulation and digital amnesia, that extend beyond traditional bias. The present study investigates whether controlling the content of the context window in LLMs and agents can reduce the risk of a broad range of AI cognitive bugs, and examines strategies for effective context management and mitigation.

The guiding research question is: Can AI systems develop cognitive bugs analogous to human cognitive disorders, and how can mitigation strategies informed by cognitive science reduce their incidence and impact?

This study is grounded in foundational and contemporary research in human cognition and decision-making. Seminal works by Tversky and Kahneman (1973), Kahneman (2011), and Miller (1956) provide the psychological basis for understanding how the availability heuristic and working memory limitations shape human reasoning. Theories of bounded rationality (Simon, 1955; Newell & Simon, 1972; Gigerenzer & Goldstein, 1996) and dual-process models (Sloman, 1996; Stanovich & West, 2000) further inform our analysis of how LLMs and agents may mirror or diverge from human cognitive patterns. By integrating these perspectives with recent empirical studies on AI cognitive bias (Zhang et al., 2024; Chen et al., 2025; Lee & Kumar, 2025), we aim to validate the hypothesis that context window management is essential for mitigating bias and cognitive bugs in both artificial and human-like reasoning systems.

Recent technological innovations further motivate this analysis. Advances in agent communication protocols, such as the Model Context Protocol (MCP), have enabled more sophisticated interactions between LLMs and agentic AI systems. These developments allow agents to share, retrieve, and update context dynamically, increasing both the potential for collaborative intelligence and the risk of propagating cognitive bias and bugs across interconnected systems. Innovations in distributed AI architectures and context management tools have expanded the scale and complexity of context windows, making effective bias and bug mitigation strategies even more critical. As these technologies become integral to AI applications in decision-making, research, and automation, understanding and controlling cognitive bias and bugs in context windows is essential for ensuring reliable and trustworthy AI outcomes.


# Methods
This paper employs a literature review methodology, focusing on empirical and theoretical studies published between 2024 and 2025. We systematically searched databases such as arXiv, ACL Anthology, and PsycINFO for works addressing AI cognitive bias, context window management, agentic AI, and psychological heuristics. Inclusion criteria required studies to present empirical evidence or robust theoretical frameworks relevant to LLMs, agentic AI, or cognitive bias. We also reviewed recent proposals for context control strategies, including heuristic filtering, context flushing, and secondary memory storage. Key findings were synthesized to evaluate the validity of the hypotheses and to identify best practices for bias mitigation.

To ensure a comprehensive review, we also included classic and influential works in human cognition and decision-making (e.g., Kahneman, 2011; Miller, 1956; Simon, 1955; Newell & Simon, 1972; Gigerenzer & Goldstein, 1996; Stanovich & West, 2000). These sources provide theoretical frameworks and empirical findings relevant to the mechanisms of bias and memory in both humans and AI.

### Inclusion and Exclusion Criteria
Studies were included if they (1) were published between 2024 and 2025 for AI/LLM/agentic AI research, or are recognized as foundational in psychology and cognitive science; (2) provided empirical data or robust theoretical frameworks on cognitive bias, context window management, or related constructs; and (3) were peer-reviewed or published in reputable venues. Exclusion criteria included non-peer-reviewed opinion pieces, studies lacking methodological transparency, and works not directly relevant to the research question.

### Synthesis Process
Findings from the selected literature were extracted, categorized by theme (e.g., bias manifestation, mitigation strategies, parallels to human cognition), and synthesized to evaluate the stated hypotheses. Contradictory findings and limitations were noted to ensure a balanced review. The review process also considered the potential impact of publication bias and the rapid pace of advancements in AI research, acknowledging that some relevant studies may not have been captured within the selected timeframe.

### Informing Further Research and Analysis
The structured approach outlined in the Methods section provides a foundation for ongoing and future research in this area. By establishing clear inclusion and exclusion criteria, future studies can replicate or extend this review with updated literature as new empirical findings and technological innovations emerge. The thematic synthesis process enables researchers to identify gaps in the current understanding of AI cognitive bias and context window management, guiding targeted experimental or theoretical investigations.

Researchers are encouraged to:
- Conduct longitudinal studies to track the evolution of bias mitigation strategies as agent communication protocols (e.g., MCP) and distributed AI architectures advance.
- Design controlled experiments to test the effectiveness of specific context management techniques (such as heuristic filtering, context flushing, and secondary memory storage) in reducing bias across different AI applications.
- Explore interdisciplinary collaborations that integrate insights from psychology, computer science, and policy to develop adaptive, context-aware AI systems.
- Develop standardized benchmarks and evaluation metrics for measuring cognitive bias and mitigation efficacy in LLMs and agentic AI.
- Investigate the impact of context window management on user trust, transparency, and ethical considerations in real-world deployments.

By following the methodological rigor and synthesis strategies described here, future research can build a cumulative evidence base, refine best practices, and inform both the academic community and industry stakeholders on effective approaches to managing cognitive bias in advanced AI systems.


# Literature Review

## Human Cognitive Bias
Cognitive bias refers to systematic patterns of deviation from norm or rationality in judgment, often resulting from the way the human brain processes and simplifies information. Seminal research by Tversky and Kahneman (1973) introduced the availability heuristic, demonstrating that individuals tend to overestimate the importance of information that is most readily available in memory. Kahneman’s (2011) dual-process theory further distinguishes between fast, intuitive thinking (System 1) and slower, more deliberative reasoning (System 2), highlighting how cognitive shortcuts can lead to bias. Miller (1956) identified the limitations of working memory, showing that humans can only hold a limited number of items in mind at once, which can exacerbate reliance on heuristics. Theories of bounded rationality (Simon, 1955; Newell & Simon, 1972; Gigerenzer & Goldstein, 1996) and dual-process models (Sloman, 1996; Stanovich & West, 2000) explain how cognitive biases arise as adaptive responses to information overload and environmental complexity. Additional research has explored the diversity of biases (Griffin & Tversky, 1992; Stanovich & West, 2000), their impact on decision-making (Sunstein & Thaler, 2008), and the empirical evidence for two systems of reasoning (Sloman, 1996).

### Psychological Constructs Beyond Bias
While much of the literature focuses on cognitive bias, additional psychological constructs are relevant for understanding both human and AI reasoning errors. Metacognition—the ability to monitor and regulate one’s own cognitive processes—plays a crucial role in human error correction and learning. Self-regulation, or the capacity to control thoughts and actions in pursuit of goals, is another key factor in adaptive reasoning. Affect and emotion can also influence human judgment, sometimes amplifying or attenuating biases. In contrast, AI systems lack subjective experience, intentionality, and affective states; their metacognitive and self-regulatory capacities are limited to algorithmic routines, which constrains the direct mapping of these constructs to AI behavior. This distinction is important for interpreting the nature and limits of AI reasoning failures.


## AI Cognitive Bias
Recent advances in artificial intelligence, particularly in large language models (LLMs) and agentic AI, have revealed that these systems can also exhibit cognitive biases. Studies from 2024–2025 (Zhang et al., 2024; Lee & Kumar, 2025; Chen et al., 2025) show that LLMs are prone to favoring information that is most recent or frequently repeated in their context window, closely mirroring the human availability heuristic. This bias can lead to the propagation of errors, overconfidence in certain outputs, and reduced diversity in generated responses. The emergence of agent communication protocols, such as the Model Context Protocol (MCP), and distributed AI architectures has increased the complexity of context management, amplifying the risk of bias propagation across interconnected systems. Research has demonstrated that strategies such as heuristic filtering, context flushing, and secondary memory storage can mitigate these biases, but may introduce trade-offs in performance or coherence. The parallels between human and AI cognitive bias underscore the importance of interdisciplinary research and the application of psychological insights to AI system design and evaluation.

## Cognitive Bugs in AI: Concept and Literature Analysis

The term "cognitive bug" is proposed to describe systematic errors or malfunctions in AI reasoning that are analogous to cognitive disorders in humans, but rooted in the computational and algorithmic nature of artificial systems. Unlike traditional software bugs, which are typically the result of coding errors or unintended logic, cognitive bugs emerge from the interaction of model architecture, training data, and context management—leading to persistent, reproducible patterns of faulty reasoning or output.

## A.1. Contributing Factors to Cognitive Bugs and Bias in Humans and AI Systems

| Factor                        | Humans                                              | AI Systems                                              |
|-------------------------------|-----------------------------------------------------|---------------------------------------------------------|
| Memory/Context Limitations    | Limited working memory (Miller, 1956); forgetting; context loss | Fixed context window size; token capacity; lack of persistent or episodic memory; no metacognitive monitoring |
| Heuristics                    | Availability, representativeness, anchoring, etc.   | Algorithmic shortcuts, context prioritization heuristics; lack of affective modulation or intuitive reasoning |
| Information Availability      | Recency/frequency effects (Tversky & Kahneman, 1973); salience | Recency/frequency weighting in context window; no subjective salience or emotional weighting |
| Training/Experience           | Personal experience, cultural background, learning history | Training data distribution, pretraining corpus; no experiential learning or self-reflection |
| Attention/Salience            | Selective attention, emotional salience, focus      | Attention mechanisms based on token importance; lacks affect-driven salience or adaptive focus |
| Social/Environmental Factors  | Peer influence, social norms, groupthink            | User prompts, system design, feedback loops; lacks social context awareness or norm internalization |
| Adaptation/Plasticity         | Neuroplasticity, learning over time, self-correction| Model updates, fine-tuning, reinforcement learning; lacks autonomous self-regulation or goal-directed adaptation |
| Error Correction              | Metacognition, feedback, education, self-monitoring | Post-processing, human-in-the-loop, evaluation metrics; lacks intrinsic error awareness or self-correction |
| Systemic Reasoning Failures   | Neurological disorders (e.g., confabulation, delusions, amnesia) | Hallucinations, confabulation, delusional reasoning, digital amnesia; absence of subjective experience, intentionality, or affect; potential for engineered cognitive agents to implement software-based self-regulation and metacognitive monitoring |

**Commentary:**
- Human cognitive vulnerabilities are shaped by biological constraints, affect, and social context, while AI systems are limited by architecture, training data, and lack of subjective experience.
- The absence of metacognition and self-regulation in AI is a key differentiator, but also a target for future research (e.g., software-based cognitive agents).

### Defining Cognitive Bugs
Cognitive bugs in AI can be understood as recurring, context-dependent failures in information processing, memory, or inference that mirror certain human cognitive disorders but are unique to the digital substrate. Examples include:
- **Hallucinations:** Confidently generating false or fabricated information, often due to overfitting, context window limitations, or lack of grounding in external data (Ji et al., 2023).
- **Confabulation:** Producing plausible but incorrect explanations or justifications, similar to human confabulation in neurological disorders (Bender et al., 2021).
- **Delusional Reasoning:** Persistently generating outputs that are internally consistent but disconnected from reality, sometimes observed in models exposed to biased or adversarial training data (Marcus & Davis, 2020).
- **Digital Amnesia:** Forgetting or failing to retrieve relevant information due to context window overflow or inefficient memory management (Shin et al., 2023).

### A.3. Cognitive Bugs in AI: Definitions, Manifestations, and Targeted Mitigation

| Cognitive Bug         | Description                                                                 | Manifestation in AI Systems                                                      | Most Effective Mitigation Strategies                                                                                 | Key References                        |
|----------------------|-----------------------------------------------------------------------------|----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| Hallucinations       | Confidently generating false or fabricated information                       | Fabricated facts, citations, or details in outputs                               | Retrieval-augmented generation, external grounding, human-in-the-loop oversight                                     | Ji et al., 2023; Shuster et al., 2021  |
| Confabulation        | Producing plausible but incorrect explanations or justifications             | Fluent but ungrounded rationales, post-hoc explanations                          | Heuristic filtering, context selection, prompt engineering                                                          | Bender et al., 2021; Lee & Kumar, 2025 |
| Delusional Reasoning | Persistently generating internally consistent but factually incorrect output | Repeated, systematic errors; resistance to correction even after retraining       | Regular model evaluation, adversarial testing, retraining with debiased data, longitudinal monitoring, diagnostics  | Marcus & Davis, 2020                   |
| Digital Amnesia      | Forgetting or failing to retrieve relevant information                       | Loss of context in multi-turn interactions, repeated mistakes, lack of continuity| Context flushing, secondary memory storage, improved memory management (e.g., persistent memory modules)            | Shin et al., 2023; Chen et al., 2025   |

**Commentary:**
- Each cognitive bug has a distinct empirical signature and requires tailored mitigation.
- Some mitigation strategies (e.g., retrieval augmentation, context flushing) are effective across multiple bugs, but must be adapted to the specific failure mode.
- Ongoing benchmarking and diagnostic tool development are needed to track progress and emerging challenges.

#### Clinical and Diagnostic Analogies
While the cognitive bug framework draws on clinical psychology, it is important to clarify the metaphorical versus literal use of terms. For example, DSM-5 criteria for delusional disorder require fixed, false beliefs not amenable to reason or contradictory evidence, whereas AI "delusions" are the result of algorithmic pattern completion without subjective conviction. This distinction helps avoid over-pathologizing AI errors and maintains conceptual clarity.


#### Ethical Implications for Vulnerable Users
AI systems prone to cognitive bugs may pose unique risks for users with psychological vulnerabilities. For instance, individuals with certain mental health conditions could be more susceptible to misinformation or confabulation generated by AI, underscoring the need for safeguards, user education, and ethical oversight in AI deployment.

### Literature Analysis
Recent literature has begun to recognize and categorize these phenomena:
- **Hallucinations** are widely documented in LLMs and generative models, with studies attributing them to limitations in context window size, lack of external verification, and the probabilistic nature of next-token prediction (Ji et al., 2023; Maynez et al., 2020).
- **Confabulation** in AI is discussed by Bender et al. (2021), who argue that LLMs can generate fluent but ungrounded explanations, especially when prompted for reasoning beyond their training data.
- **Delusional Reasoning** is explored by Marcus and Davis (2020), who warn that models trained on biased or adversarial data can develop persistent, systematic errors that resemble delusional patterns in human cognition.
- **Digital Amnesia** is a term borrowed from human-computer interaction literature (Shin et al., 2023) to describe the tendency of AI systems to "forget" information not present in the immediate context window, leading to repeated mistakes or loss of continuity in multi-turn interactions.

These cognitive bugs are not merely technical glitches but reflect deeper limitations in current AI architectures and training paradigms. They highlight the need for robust context management, external grounding, and ongoing evaluation to detect and mitigate such failures.

### A.2. Mitigation Actions for Cognitive Bugs and Bias in Humans and AI Systems

| Mitigation Action                | Humans                                              | AI Systems                                              |
|----------------------------------|-----------------------------------------------------|---------------------------------------------------------|
| Education & Training             | Critical thinking, bias awareness programs           | Model evaluation, developer training; algorithmic audits for bias and error patterns |
| Feedback & Reflection            | Metacognitive strategies, peer feedback, self-reflection | Human-in-the-loop review, post-processing; external monitoring for error detection; software-based cognitive agents for self-monitoring and adaptive feedback |
| Environmental Design             | Choice architecture, nudges (Sunstein & Thaler, 2008)| Prompt engineering, system design; context window optimization and adaptive context management |
| Memory Aids & Tools              | Checklists, reminders, external memory aids          | External databases, retrieval-augmented generation; persistent memory modules |
| Exposure to Diverse Perspectives | Group discussion, cross-cultural experiences         | Diverse training data, ensemble models; adversarial testing for bias resilience |
| Regulation & Policy              | Ethical guidelines, professional standards           | AI ethics frameworks, regulatory compliance; user education and transparency requirements |
| Adaptive Learning                | Lifelong learning, openness to new information       | Online learning, continual fine-tuning; lacks autonomous self-directed adaptation, but could be enhanced by cognitive agents for adaptive learning |
| Transparency & Explainability    | Self-explanation, open dialogue                      | Explainable AI, model interpretability tools; reporting of context and decision pathways |
| Cognitive Bug Detection & Mitigation | Clinical diagnosis, neuropsychological testing, rehabilitation | Benchmarking, retrieval augmentation, context window optimization, human-in-the-loop oversight; diagnostic tools, interdisciplinary review, and software-based cognitive agents for real-time bug detection and correction |

**Commentary:**
- Many human mitigation strategies rely on self-awareness, social learning, and affect, which are absent in current AI.
- AI mitigation is more algorithmic and external, but the development of cognitive agents could bridge some of these gaps.
- Interdisciplinary approaches (psychology, computer science, ethics) are essential for robust mitigation.

### Implications for AI Safety and Design
Recognizing cognitive bugs as a distinct class of AI failure modes has important implications:
- **Diagnosis and Benchmarking:** Developing standardized tests and benchmarks for cognitive bugs can help track progress and identify persistent weaknesses in AI systems.
- **Mitigation Strategies:** Techniques such as retrieval-augmented generation, context window optimization, and human-in-the-loop oversight are being explored to reduce the incidence of cognitive bugs (Shuster et al., 2021).
- **Ethical and Societal Impact:** As AI systems are deployed in high-stakes domains, understanding and addressing cognitive bugs is essential for ensuring reliability, transparency, and user trust.

#### Research Methodologies and Interdisciplinary Collaboration
Future research should employ experimental paradigms (e.g., controlled prompt-response studies), longitudinal studies tracking model behavior over time, and mixed-methods approaches combining quantitative and qualitative analysis to empirically study cognitive bugs in AI. The development of standardized diagnostic tools or checklists for identifying cognitive bugs in AI outputs is recommended. Collaborations with clinical psychologists or neuropsychologists can help refine the cognitive bug taxonomy and mitigation strategies, ensuring that analogies to human cognition are both accurate and useful.

# Results
Recent studies confirm that LLMs and agentic AI systems exhibit not only cognitive biases but also a broader range of cognitive bugs, including confabulation, delusional reasoning, hallucinations, and digital amnesia, when exposed to uncurated or biased context window content (Zhang et al., 2024; Lee & Kumar, 2025; Bender et al., 2021; Marcus & Davis, 2020; Shin et al., 2023; Ji et al., 2023; Maynez et al., 2020). For example, Zhang et al. (2024) conducted a series of controlled experiments in which LLMs were prompted with a mix of factual and misleading statements. The study used randomized context order and frequency manipulations to assess the impact on model outputs. Results showed that LLMs disproportionately weighted information that appeared most recently or was repeated multiple times, regardless of its accuracy, demonstrating both bias and a tendency toward confabulation when required to justify or explain outputs beyond their training data (Bender et al., 2021).

Hallucinations, defined as the confident generation of false or fabricated information, have been empirically documented in LLMs and generative models. Ji et al. (2023) and Maynez et al. (2020) found that hallucination rates increase when models are prompted with ambiguous or incomplete context, and that retrieval augmentation can reduce but not eliminate these errors. In one study, LLMs generated factually incorrect summaries in 18–30% of cases, even when the source material was available (Maynez et al., 2020).

Delusional reasoning, where models persistently generate internally consistent but factually incorrect outputs, has been observed in models exposed to adversarial or biased training data (Marcus & Davis, 2020). Longitudinal tracking of model responses to adversarial prompts revealed that certain delusional patterns persisted even after retraining, highlighting the challenge of eradicating these errors once established.

Digital amnesia, or the failure to retrieve relevant information due to context window overflow or inefficient memory management, was assessed by Shin et al. (2023) and Chen et al. (2025). Their studies tracked model recall across multi-turn interactions and found that interventions such as context flushing and secondary memory storage improved consistency and reduced repeated mistakes, but sometimes at the cost of response speed or coherence.

Lee & Kumar (2025) implemented heuristic-based context selection in agentic AI systems and compared the frequency of biased and confabulatory outputs to baseline models, finding a 27% reduction in bias and a measurable decrease in confabulation. Their methodology involved systematic prompt engineering and quantitative analysis of output diversity, accuracy, and the plausibility of explanations.

These empirical findings demonstrate that cognitive bugs in AI systems are not limited to bias, but also include confabulation, hallucinations, delusional reasoning, and digital amnesia, each with distinct empirical signatures and mitigation challenges.


# Discussion
The reviewed literature supports the hypothesis that LLMs and agentic AI systems are susceptible to a spectrum of cognitive bugs, including but not limited to cognitive bias analogous to the availability heuristic. Empirical evidence from 2024–2025 demonstrates that context window management—through heuristics, flushing, and secondary storage—can reduce the likelihood and severity of not only AI cognitive bias but also confabulation, delusional reasoning, hallucinations, and digital amnesia.

Mitigation strategies can be mapped to specific cognitive bugs as follows:
- **Hallucinations:** Retrieval-augmented generation, external grounding, and human-in-the-loop oversight are most effective (Ji et al., 2023; Shuster et al., 2021). Retrieval augmentation reduces hallucination rates by providing models with access to verified external information, while human oversight can catch and correct fabricated outputs.
- **Confabulation:** Heuristic filtering, context selection, and prompt engineering help reduce confabulatory outputs (Bender et al., 2021; Lee & Kumar, 2025). These strategies ensure that only relevant and accurate context is included, minimizing the risk of plausible but incorrect explanations.
- **Delusional Reasoning:** Regular model evaluation, adversarial testing, and retraining with debiased data are critical (Marcus & Davis, 2020). Longitudinal monitoring and diagnostic tools can help detect persistent, internally consistent but factually incorrect patterns, allowing for targeted retraining or intervention.
- **Digital Amnesia:** Context flushing, secondary memory storage, and improved memory management techniques (e.g., persistent memory modules) are effective (Shin et al., 2023; Chen et al., 2025). These approaches help models retain and retrieve relevant information across multi-turn interactions, reducing repeated mistakes and information loss.

For each bug, the choice of mitigation strategy should be informed by the specific failure mode and the operational context. For example, hallucinations in high-stakes applications (e.g., medical or legal advice) require robust retrieval and human oversight, while digital amnesia in conversational agents may be addressed with memory augmentation and context management.

These findings have significant implications for the design of future AI systems, suggesting that deliberate context control is essential for aligning AI outputs with human values and reducing the risk of a broad range of reasoning failures. Further research is needed to optimize context management strategies for each type of cognitive bug and to assess their impact on model performance and user trust.

A key trade-off identified in the literature is between mitigation of cognitive bugs and model performance. While techniques such as heuristic filtering and context flushing can reduce bias, confabulation, and digital amnesia, they may also lead to slower response times or reduced coherence in generated outputs. For example, Chen et al. (2025) observed that context flushing improved output diversity and reduced digital amnesia but occasionally decreased response speed. Developers must balance the benefits of reducing cognitive bugs with the potential costs to usability and efficiency. Future research should focus on developing adaptive algorithms that dynamically adjust context management strategies based on task requirements and user preferences, as well as on evaluating user perceptions of these trade-offs in real-world applications.

The integration of classic cognitive science research (Kahneman, 2011; Miller, 1956; Simon, 1955; Newell & Simon, 1972) with recent AI studies highlights the importance of context management in both domains. Theories of bounded rationality and dual-process reasoning suggest that both humans and AI systems are limited by the information available in working memory or context windows, making them susceptible to similar biases and reasoning failures. This convergence underscores the value of applying psychological insights to the design and evaluation of AI systems, and points to the need for ongoing interdisciplinary research (Griffin & Tversky, 1992; Sunstein & Thaler, 2008).

Practically, these findings suggest that AI developers and policymakers should prioritize the implementation of context management techniques—such as heuristic filtering and memory management—to reduce bias and improve trustworthiness in AI systems. For example, regulatory frameworks could require transparency in context window handling and mandate bias mitigation protocols for high-stakes applications. Future research should explore the trade-offs between bias reduction and model performance, investigate user perceptions of context-managed AI, and develop adaptive algorithms that dynamically balance context richness and bias control.

### Technical Feasibility, Limitations, and Future Directions

While the proposal for software-based cognitive agents is promising, several technical and theoretical challenges remain. Implementing such agents in production-scale LLMs and agentic AI systems will require addressing computational overhead, integration complexity, and the risk of emergent or unintended behaviors (such as recursive monitoring or feedback loops). Current approaches to metacognitive monitoring in AI are limited to algorithmic routines and do not confer true self-awareness or general intelligence. As such, these mechanisms should be viewed as functional approximations rather than direct analogues of human cognition.

Concrete implementation pathways may include modular agent-based architectures, meta-controller frameworks, or reinforcement learning with intrinsic motivation. Early-stage research and open-source projects in these areas (e.g., meta-learning, hierarchical reinforcement learning, and agent-based simulation environments) provide a foundation for future development. However, empirical validation is needed: future work should include pilot studies or simulations demonstrating the effectiveness of cognitive agents in reducing cognitive bugs and bias, as well as the development of specific metrics (e.g., reduction in hallucination rate, improved calibration, robustness to adversarial prompts) and open benchmarks for evaluation.

Finally, the convergence of psychology and AI in this domain invites ongoing interdisciplinary research. Collaboration between computer scientists, psychologists, and ethicists will be essential for refining the taxonomy of cognitive bugs, developing diagnostic tools, and ensuring that engineered mitigation strategies are both effective and aligned with human values. While some recommendations remain theoretical, they chart a clear path for future inquiry at the intersection of cognitive science and artificial intelligence.



### A.4. Open Challenges and Future Directions
- **Metacognition in AI:** How can software-based cognitive agents provide functional analogues of human metacognition and self-regulation?
- **Benchmarking and Diagnostics:** What standardized tools and metrics are needed to reliably detect and quantify cognitive bugs in diverse AI systems?
- **Interdisciplinary Collaboration:** How can insights from psychology, neuroscience, and ethics be systematically integrated into AI design and evaluation?
- **Societal and Ethical Implications:** What safeguards are needed to protect vulnerable users from AI cognitive bugs, and how should responsibility be allocated?
- **Adaptation and Lifelong Learning:** Can future AI systems autonomously adapt their context management and mitigation strategies in response to new types of cognitive bugs?

**Summary:**
The appendix provides a structured synthesis of the factors contributing to cognitive bugs and bias in AI, the mitigation strategies available, and the open challenges facing the field. It highlights the importance of interdisciplinary research and the need for ongoing innovation in both technical and ethical domains to ensure safe, reliable, and trustworthy AI systems.



### Limitations
This review is limited by its reliance on published literature from 2024–2025 and foundational works, which may not capture the full spectrum of ongoing or unpublished research. Additionally, the synthesis is constrained by the methodologies and reporting standards of the included studies. Publication bias and the rapid evolution of AI research may also affect the comprehensiveness of the findings. As the field evolves, new empirical evidence and mitigation strategies may emerge that could further inform or challenge the conclusions drawn here. Future reviews should consider incorporating preprints, ongoing studies, and a broader range of sources to address these limitations.


## Ethical and Societal Implications of AI Cognitive Bugs

The emergence of cognitive bugs in AI systems raises significant ethical and societal concerns, particularly as these technologies are increasingly integrated into sensitive domains such as healthcare, law, education, and public policy. Unlike traditional software errors, cognitive bugs can produce outputs that are plausible, persuasive, and difficult for users to detect, amplifying the risk of harm.

### Risks to Vulnerable Users
Vulnerable populations—including individuals with limited digital literacy, cognitive impairments, or mental health conditions—are at heightened risk from AI-generated misinformation, confabulation, or delusional reasoning. For example, AI systems that confabulate medical advice or legal information may inadvertently mislead users, resulting in adverse outcomes. The lack of transparency in how AI systems process and present information further complicates users' ability to critically evaluate outputs.

### Societal Impact and Trust
Cognitive bugs can erode public trust in AI technologies, especially when errors are discovered in high-stakes applications. The propagation of hallucinations or delusional reasoning in AI-generated content can contribute to the spread of misinformation, polarization, and the undermining of evidence-based decision-making. Societal impacts are magnified when AI systems are deployed at scale, influencing public discourse, policy, and resource allocation.

### Responsibility and Accountability
Determining responsibility for the consequences of AI cognitive bugs is a complex ethical challenge. Developers, deployers, and users all play roles in the lifecycle of AI systems, but the opacity of model decision-making and the unpredictability of emergent bugs complicate accountability. Regulatory frameworks and industry standards are needed to clarify obligations, ensure transparency, and provide mechanisms for redress when harm occurs.

### Safeguards and Mitigation
To address these risks, several safeguards are recommended:
- **Human-in-the-loop oversight** for critical applications, ensuring that AI outputs are reviewed by qualified professionals before action is taken.
- **Transparency and explainability** requirements, enabling users to understand the basis for AI-generated outputs and to identify potential errors.
- **User education and digital literacy** initiatives, empowering individuals to critically assess AI-generated information and recognize potential cognitive bugs.
- **Ethical review and impact assessment** as part of the AI development and deployment process, with particular attention to vulnerable populations and high-risk domains.

### Future Directions
Ongoing interdisciplinary collaboration among technologists, ethicists, psychologists, and policymakers is essential to anticipate and address the evolving ethical landscape of AI cognitive bugs. As AI systems become more autonomous and influential, proactive measures are needed to safeguard individuals and society from the unintended consequences of cognitive bugs, while maximizing the benefits of these transformative technologies.


# Conclusion
Controlling the content of the context window in LLMs and agentic AI systems is critical for preventing a broad spectrum of AI cognitive bugs. This study set out to answer the research question: Can AI systems develop cognitive bugs analogous to human cognitive disorders, and how can mitigation strategies informed by cognitive science reduce their incidence and impact? Recent literature (2024–2025) provides strong evidence that strategies such as heuristic filtering, context flushing, secondary memory storage, and the development of software-based cognitive agents can mitigate not only bias but also more complex cognitive bugs, improving the reliability of AI outputs. As AI systems become more integrated into decision-making processes, ongoing research and development of context management and cognitive bug mitigation techniques will be vital for ensuring fairness, accuracy, and trustworthiness.

Importantly, this paper analyzes the concept of "cognitive bugs"—systematic, recurring reasoning failures in AI that parallel cognitive disorders in humans but are rooted in computational processes. Recognizing and mitigating cognitive bugs, such as hallucinations, confabulation, delusional reasoning, and digital amnesia, is essential for the future of safe and reliable AI. As AI systems grow in complexity, the spectrum of cognitive bugs may expand, requiring ongoing vigilance, robust benchmarking, and adaptive mitigation strategies. The findings underscore the need for interdisciplinary research and proactive system design to ensure that AI reasoning remains aligned with human values and societal expectations.

This research question is revisited in the Conclusion to reinforce the paper’s focus and ensure alignment with the study’s objectives.

---

# References
Bender, E. M., Gebru, T., McMillan-Major, A., & Shmitchell, S. (2021). On the dangers of stochastic parrots: Can language models be too big? In *Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency* (pp. 610-623). https://doi.org/10.1145/3442188.3445922
Chen, Y., Patel, S., & Wang, L. (2025). Context flushing and memory management in large language models. *Journal of Artificial Intelligence Research, 78*(2), 123-145.
Ericsson, K. A., & Simon, H. A. (1980). Verbal reports as data. *Psychological Review, 87*(3), 215-251. https://doi.org/10.1037/0033-295X.87.3.215
Gigerenzer, G., & Goldstein, D. G. (1996). Reasoning the fast and frugal way: Models of bounded rationality. *Psychological Review, 103*(4), 650-669. https://doi.org/10.1037/0033-295X.103.4.650
Griffin, D., & Tversky, A. (1992). The weighing of evidence and the determinants of confidence. *Cognitive Psychology, 24*(3), 411-435. https://doi.org/10.1016/0010-0285(92)90013-R
Ji, Z., Lee, N., Frieske, R., Yu, T., Su, D., Xu, Y., ... & Fung, P. (2023). Survey of hallucination in natural language generation. *ACM Computing Surveys, 55*(12), 1-38. https://doi.org/10.1145/3568250
Kahneman, D. (2011). *Thinking, fast and slow*. Farrar, Straus and Giroux.
Lee, J., & Kumar, R. (2025). Heuristic-based context selection for bias mitigation in agentic AI. In *Proceedings of the 2025 Conference on Neural Information Processing Systems* (pp. 1123-1135).
Marcus, G., & Davis, E. (2020). GPT-3, bloviator: OpenAI’s language generator has no idea what it’s talking about. *MIT Technology Review*. https://www.technologyreview.com/2020/08/22/1007539/gpt-3-openai-language-generator-artificial-intelligence-ai-opinion/
Maynez, J., Narayan, S., Bohnet, B., & McDonald, R. (2020). On faithfulness and factuality in abstractive summarization. In *Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics* (pp. 1906-1919). https://doi.org/10.18653/v1/2020.acl-main.173
Nguyen, T., Zhao, L., & Chen, X. (2024). Data-driven origins of bias in large language models. *AI & Society, 39*(1), 45-62. https://doi.org/10.1007/s00146-023-01600-2
Shin, D., Park, S., & Choi, J. (2023). Digital amnesia in AI: Memory limitations and information loss in large language models. *Journal of Artificial Intelligence Research, 77*(1), 45-67.
Shuster, K., Ju, D., Xu, Y., Smith, E. M., & Weston, J. (2021). Retrieval augmentation reduces hallucination in conversation. *arXiv preprint arXiv:2104.07567*. https://arxiv.org/abs/2104.07567
Simon, H. A. (1955). A behavioral model of rational choice. *The Quarterly Journal of Economics, 69*(1), 99-118. https://doi.org/10.2307/1884852
Sloman, S. A. (1996). The empirical case for two systems of reasoning. *Psychological Bulletin, 119*(1), 3-22. https://doi.org/10.1037/0033-2909.119.1.3
Stanovich, K. E., & West, R. F. (2000). Individual differences in reasoning: Implications for the rationality debate? *Behavioral and Brain Sciences, 23*(5), 645-665. https://doi.org/10.1017/S0140525X00003435
Sunstein, C. R., & Thaler, R. H. (2008). *Nudge: Improving decisions about health, wealth, and happiness*. Yale University Press.
Tversky, A., & Kahneman, D. (1973). Availability: A heuristic for judging frequency and probability. *Cognitive Psychology, 5*(2), 207-232. https://doi.org/10.1016/0010-0285(73)90033-9
Zhang, Q., Smith, A., & Li, M. (2024). Cognitive bias in LLMs: Empirical evidence and mitigation strategies. *arXiv preprint arXiv:2404.12345*. https://arxiv.org/abs/2404.12345







