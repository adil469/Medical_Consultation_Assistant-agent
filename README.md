
# Medical Consultation Assistant (Dynamic Agent)

This project demonstrates how to build a **dynamic medical consultation agent** using the Agentic AI SDK.  
The agent adapts its response style based on the **user role** (Patient, Medical Student, or Doctor).

---

## 🚀 Features
- **Role Detection:** Automatically detects the role (Patient, Medical Student, or Doctor) from the user input.
- **Dynamic Instructions:** Adjusts explanation style depending on the role:
  - **Patient:** Simple, non-technical, empathetic explanations.
  - **Medical Student:** Moderate medical terminology with explanations and learning opportunities.
  - **Doctor:** Full medical terminology, clinical abbreviations, and professional concise explanations.
- **Interactive Prompt:** Takes user input dynamically from the terminal.

---

## 🛠️ Requirements

Install dependencies:

```bash
pip install agentic-ai pydantic rich python-dotenv
```

---

## 📂 Code Structure

- **Person Class** → Defines the user role.
- **detect_role()** → Identifies role from user input.
- **dynamic_medical_assistant()** → Adjusts instructions dynamically according to the role.
- **triage_Agent** → Main agent configured with dynamic instructions.
- **main()** → Runs the program, takes user input, and generates role-specific responses.

---

## ▶️ Usage

Run the program:

```bash
python main.py
```

Then type a prompt, for example:

- `Explain high blood pressure to a patient`
- `I am a medical student. Explain blood sugar.`
- `I am a doctor. Please explain diabetes mellitus in professional terms.`

---

## 🧑‍🏫 Learning Opportunity

This exercise is designed for **intermediate learners** who want to understand how **dynamic instructions** can tailor AI responses.  
It also shows how **context passing** works with `Agent` and `RunContextWrapper`.

---

## 📌 Notes

- Ensure you have a valid **`.env` file** with your API key configured.  
- This example can be extended to other roles or specialized medical fields.

---

✅ You now have a **dynamic role-based medical consultation assistant**!
"# Medical_Consultation_Assistant-agent" 
"# Medical_Consultation_Assistant-agent" 
