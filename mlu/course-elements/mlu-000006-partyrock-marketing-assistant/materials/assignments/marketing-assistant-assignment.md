# Build and Evaluate an AI Marketing Assistant

**Introduction to Generative AI — Learning to Prompt and Build a Marketing Assistant**

| | |
|---|---|
| **Estimated student time** | 1–2 hours |
| **Tools needed** | AWS PartyRock (free), a web browser, a shared spreadsheet |
| **Level** | Intro digital-literacy or AI-literacy courses |

## Overview

In this guide you will build an AI-powered Marketing Assistant using **Amazon PartyRock** — a
no-code generative AI app builder. Your app will take information about a product or service and
generate professional marketing content. You will then experiment with three different prompt
strategies to see how prompt engineering affects AI output quality.

**What you'll build:** a working app with user inputs (product name, audience, tone, and more) that
generates a marketing headline, social media post, call-to-action, and suggested hashtags.

**Time estimate:** 45–60 minutes for the build; 30 minutes for the prompt comparison exercise.

---

## Part 1 — Getting started with PartyRock

### Step 1 — Access PartyRock

1. Open your browser and go to <https://partyrock.aws>.
2. Click **Sign in** in the top-right corner.
3. Sign in using your **Apple**, **Google**, or **Amazon** account. No AWS account or credit card is
   required.
4. Once signed in, you'll land on the PartyRock home page.

### Step 2 — Create a new app

1. In the list you will see a box titled **Build AI Flows**. Click the **Create a Flow** button.
2. You will be asked what you would like to build. You'll see an area that says *"Describe what you
   would like your app to do?"*
3. Type a description similar to this:

   > Build a marketing assistant app. It should have input fields for: Product/Service Name,
   > Target Audience, Product Description, Tone (friendly, professional, or fun), Platform
   > (Instagram, Twitter, Facebook), and Desired Length in words. It should generate a marketing
   > headline, a short description, a social media post, a call-to-action, and suggested hashtags.

4. Click **Generate app**.
5. PartyRock will auto-generate a working app with widgets. This is your starting point.

---

## Part 2 — Customize your app

PartyRock will generate an initial layout, but you will want to refine it. Here's how to set up each
component.

### Step 3 — Configure your input widgets

Your app should have six input fields. For each one, click on the widget to edit it. If any are
missing, click **+ Add widget** and select **User Input**.

| Input widget | Type | Default value / options |
|---|---|---|
| Product/Service Name | Text input | e.g. Campus Coffee Shop |
| Target Audience | Text input | e.g. College students ages 18–24 |
| Product Description | Text input | e.g. Affordable coffee, breakfast items, and free Wi-Fi |
| Tone | Text input | e.g. Friendly, Professional, Fun, Energetic |
| Platform | Text input | e.g. Instagram, Twitter/X, Facebook, LinkedIn |
| Desired Length | Text input | e.g. 100 words |

To edit an input widget:

1. Click the pencil/edit icon on the widget.
2. Set the **Title** — this is the label users see.
3. Optionally add **Placeholder** text to guide users, e.g. "Enter your product name here".
4. Click **Save**.

### Step 4 — Configure your output widgets

Your app should generate five outputs. These are AI-powered text generation widgets. If PartyRock
didn't create all of them, click **+ Add widget** and select **Text generation**.

For each output widget, you'll write a prompt that references your input widgets using the `@`
symbol.

**Output 1 — Marketing Headline** (Text generation)

```
Generate a catchy marketing headline for @Product/Service Name targeting @Target Audience.
The tone should be @Tone. Keep it under 15 words.
```

**Output 2 — Short Description** (Text generation)

```
Write a short marketing description for @Product/Service Name.
Target audience: @Target Audience.
Key details: @Product Description.
Tone: @Tone.
Keep it to 2–3 sentences.
```

**Output 3 — Social Media Post** (Text generation)

```
Write a social media post for @Platform promoting @Product/Service Name.
Target audience: @Target Audience.
Product details: @Product Description.
Tone: @Tone.
Length: approximately @Desired Length.
Make it engaging and appropriate for the platform.
```

**Output 4 — Call-to-Action** (Text generation)

```
Generate a compelling call-to-action for @Product/Service Name targeting @Target Audience.
Tone: @Tone. Platform: @Platform.
Keep it to one sentence that drives engagement or visits.
```

**Output 5 — Suggested Hashtags** (Text generation)

```
Suggest 5–7 relevant hashtags for a @Platform post promoting @Product/Service Name
to @Target Audience. Make them specific, trending-friendly, and relevant to: @Product Description.
```

### Step 5 — Test your app

Fill in all input fields with the sample data below and review all five outputs.

| Field | Sample value |
|---|---|
| Product/Service | Campus Coffee Shop |
| Target Audience | College students ages 18–24 |
| Product Description | Affordable coffee, breakfast items, and free Wi-Fi |
| Tone | Friendly and energetic |
| Platform | Instagram |
| Desired Length | 100 words |

Try changing inputs — switch the platform to LinkedIn, change the tone to Professional — and observe
how the outputs change.

### Step 6 — Polish and publish

1. Click on your app title at the top to rename it, e.g. "AI Marketing Assistant – [Your Name]".
2. Rearrange widgets by dragging them into a logical order: inputs on top, outputs below.
3. Click **Make public and share** to generate a shareable link.
4. Copy and save your app link — you'll submit this as part of your deliverable.

---

## Part 3 — Prompt engineering experiment

Now for the most important part of this assignment. You will test three different prompt strategies
on the same marketing scenario and compare the results.

### The scenario — use this for all three prompts

- **Product:** Campus Coffee Shop
- **Audience:** College students ages 18–24
- **Details:** Affordable coffee, breakfast, free Wi-Fi

### Prompt A — Basic prompt

Enter this as the prompt for your Social Media Post widget, temporarily replacing your existing
prompt:

```
Write a marketing advertisement for a coffee shop.
```

Copy and save the output before moving to the next prompt.

### Prompt B — Role + context prompt

Now replace the prompt with:

```
You are a marketing specialist. Create an advertisement for a college coffee shop targeting
students between the ages of 18 and 24. The coffee shop offers affordable coffee, breakfast,
and free Wi-Fi.
```

Copy and save the output before moving to the next prompt.

### Prompt C — Structured prompt

Now replace the prompt with:

```
You are a college marketing specialist.
Task: Create an Instagram advertisement for a campus coffee shop.
Target audience: College students ages 18–24.
Tone: Friendly, energetic, and authentic.
Key benefits: Affordable coffee, breakfast, free Wi-Fi.
Length: 75–100 words.
Output:
1. Headline
2. Advertisement
3. Call-to-action
4. Three hashtags
Do not make claims that are not supported by the information provided.
```

Copy and save the output before moving to the next step.

### Step 7 — Compare and analyze

After running all three prompts, evaluate the results using the table below.

| Evaluation criteria | Prompt A (Basic) | Prompt B (Role + Context) | Prompt C (Structured) |
|---|---|---|---|
| **Relevance** — does it match the target audience? | | | |
| **Specificity** — does it include key product details? | | | |
| **Tone** — is the tone appropriate for the audience? | | | |
| **Completeness** — does it include all needed elements? | | | |
| **Usability** — could you actually post this as-is? | | | |

---

## Part 4 — What to submit

Your deliverable should include all four of the following components.

1. **PartyRock app link** — the shareable URL to your working marketing assistant.
2. **Screenshot(s)** — at least one screenshot showing your app with sample inputs and generated
   outputs.
3. **Prompt comparison document** — including:
   - the three prompts (A, B, and C) you used;
   - the AI-generated output for each prompt;
   - your completed comparison table.
4. **Reflection (150–250 words)** — address the following:
   - Which prompt strategy produced the most effective marketing content? Why?
   - What specific elements — role, context, tone, constraints, output format — had the biggest
     impact on output quality?
   - What did this exercise teach you about working with generative AI tools?
   - How could prompt engineering skills be valuable in a marketing or business career?

---

## Tips for success

- **Be specific in your prompts.** Vague instructions produce vague results. The more context you
  give the AI, the better the output.
- **Iterate.** Don't settle for the first output. Tweak your prompts and regenerate to see
  improvements.
- **Use the `@` references.** This is what makes your app dynamic — the outputs change based on user
  inputs.
- **Think like a marketer.** Evaluate the AI output the way a marketing professional would: is this
  on-brand? Would this resonate with the audience? Is it ready to publish?
- **Document as you go.** Take screenshots and save outputs before making changes — you'll need them
  for your submission.

## Troubleshooting

| Issue | Solution |
|---|---|
| PartyRock won't generate my app | Try simplifying your description, or create a blank app and add widgets manually |
| An output widget isn't referencing my inputs | Make sure you use the `@` symbol followed by the exact widget title name |
| Outputs are too long or too short | Add explicit length constraints in your prompt, e.g. "Keep it under 100 words" |
| Outputs feel generic | Add more specific context, constraints, and audience details to your prompt |
| I can't find the share button | Look for **Make public and share** in the top-right area of the app editor |

## Key concepts to remember

| Term | Definition |
|---|---|
| **Prompt engineering** | The practice of designing and refining inputs to AI systems to get better, more useful outputs. |
| **Role prompting** | Assigning the AI a specific persona or expertise, e.g. "You are a marketing specialist". |
| **Contextual prompting** | Providing background information, audience details, and constraints. |
| **Structured prompting** | Organizing your prompt with labeled sections (Task, Audience, Tone, Output Format) for maximum clarity. |
| **Iterative refinement** | The process of testing, evaluating, and improving prompts based on output quality. |
