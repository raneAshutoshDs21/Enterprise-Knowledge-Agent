## Findings

### Successful Components

The following components were successfully configured and validated:

* Azure AI Foundry Project
* GPT-4.1 Mini Deployment
* Prompt Agent Creation
* File Search Tool Integration
* Vector Store Creation (enterprise_index)
* Document Upload and Indexing
* Grounded Question Answering
* Source-Aware Responses

The agent was able to correctly retrieve and answer questions related to:

* Employee Leave Policy
* Travel Reimbursement Policy
* Employee Handbook

The agent successfully identified and used the relevant uploaded documents when generating responses.

---

### Issue Identified

A grounding reliability issue was discovered during testing.

When asked:

"What is the maternity leave policy?"

the agent generated a detailed maternity leave policy even though no maternity leave information existed in any uploaded document.

This demonstrated that:

* Retrieval was functioning correctly.
* Document indexing was functioning correctly.
* The model was still capable of falling back to its own knowledge when retrieval returned no relevant information.

This behavior resulted in an ungrounded response (hallucination).

---

### Root Cause Analysis

Investigation confirmed that:

* The Employee Leave Policy document contained no maternity leave section.
* The uploaded files were indexed correctly.
* File Search was operational.
* The model generated information from its pretrained knowledge instead of restricting itself to retrieved content.

This highlighted an important enterprise AI challenge:

Retrieval alone does not guarantee grounded responses.

Even when retrieval systems are functioning correctly, large language models may still answer from prior knowledge if instructions are not sufficiently restrictive. Similar grounding and hallucination challenges are commonly discussed in Azure AI Foundry and RAG evaluation guidance.

---

### Corrective Action

The system instructions were updated to enforce strict grounding behavior.

The revised instructions required the agent to:

* Answer only using uploaded documents.
* Verify information exists in retrieved content before responding.
* Avoid assumptions and inferred policies.
* Avoid use of general model knowledge.
* Return a standard response when information is unavailable.

Required fallback response:

"The requested information was not found in the available documents."

---

### Validation After Fix

The hallucination test was repeated.

Question:

"What is the maternity leave policy?"

Result:

PASS

Response:

"The requested information was not found in the available documents."

This confirmed that the updated instructions significantly improved grounding behavior and reduced hallucinations.

---

### Key Lessons Learned

This validation exercise demonstrated several important enterprise AI concepts:

1. Successful retrieval does not automatically guarantee grounded responses.
2. Prompt engineering plays a critical role in controlling agent behavior.
3. Evaluation testing is essential before moving into production development.
4. Hallucination testing should be part of every AI application's validation process.
5. Groundedness and observability are important quality metrics for enterprise AI systems. Microsoft Foundry emphasizes evaluation, groundedness, tracing, and observability as part of the AI application lifecycle.

---

### Final Assessment

The Enterprise Knowledge Agent successfully achieved the project objectives:

* Document Retrieval: PASS
* Grounded Question Answering: PASS
* Source Awareness: PASS
* Hallucination Detection: PASS
* Hallucination Mitigation: PASS
* Playground Validation: PASS

Project Status:

VALIDATED FOR DEVELOPMENT PHASE
