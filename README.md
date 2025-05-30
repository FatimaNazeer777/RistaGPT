

# 💖 RishtaGPT: DilSe

>                  *"Tumhari qismet likhne aaye hain hum..."*

**RishtaGPT: DilSe 💖** is a fun, culturally rich AI-powered rishta assistant that blends wit, Urdu flair, and modern matchmaking tools into one delightful Streamlit application. From writing shayari-based manifestations to generating TikTok-worthy shaadi scripts — it has everything you need to make your rishta profile shine!

---

## 📸 Live Preview

> Coming soon...

---

## 🛠️ Tech Stack

* **Frontend & UI**: Streamlit
* **Backend**: Python
* **AI Models**: OpenRouter GPT-3.5-Turbo
* **Environment Management**: Python-dotenv
* **Deployment**: Streamlit Cloud / Local Machine

---

## 🔑 Features

| Feature                        | Description                                                                   |
| ------------------------------ | ----------------------------------------------------------------------------- |
| 🌸 **Manifestation Generator** | Generates beautiful Urdu shayari/duas to manifest your dream rishta.          |
| 🧕 **Bio Beautifier**          | Transforms dull bios into heartfelt, vibrant introductions in Urdu + English. |
| 🎭 **Rishta Quiz**             | A playful personality quiz to discover your unique rishta persona.            |
| 🎬 **Shaadi Drama Generator**  | Generates short, dramatic, funny desi shaadi scripts for content creation.    |
| 📸 **Rishta DP Frame**         | Suggests selfie frame ideas and captions in poetic desi style.                |
| 🎯 **Pickup Line Generator**   | Delivers charming Urdu-English mix pickup lines based on your vibe.           |
| 🗓️ **Shaadi Planner**         | Wedding countdown + task checklist personalized by date, budget, and style.   |

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/rishtagpt.git
cd rishtagpt
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Create a `.env` File

Inside the project root:

```bash
touch .env
```

Add your OpenRouter API key:

```env
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

### 4. Run the App

```bash
streamlit run main.py
```

---

## 🌐 API Usage

The app uses [OpenRouter.ai](https://openrouter.ai) to send prompts to `gpt-3.5-turbo`:

* **Endpoint**: `https://openrouter.ai/api/v1/chat/completions`
* **Model**: `openai/gpt-3.5-turbo`
* **Headers**:

  * `Authorization: Bearer <API_KEY>`
  * `HTTP-Referer`: Required by OpenRouter
  * `X-Title`: Project name

---

## 🎨 UI Styling

The app includes custom HTML/CSS to create a soft, romantic UI:

* Pink and white palette (`#FFF5F5`, `#FF4B4B`)
* Card-style feature boxes
* Stylish buttons and hover effects
* Responsive two-column layouts

---

## 🤖 Prompt Engineering Highlights

Each feature uses a unique prompt style with the model:

* Cultural context: **Pakistani rishta traditions**
* Language mix: **Urdu + English**
* Emotion: **Poetic**, **humorous**, or **respectful**
* Platform optimized: **Instagram**, **Reels**, **rishta bios**

---

## 🧪 Sample Prompt

```
Write a funny short script for a Pakistani shaadi drama scene: Mehndi Night Drama in Comedy style.
Make it suitable for TikTok reels, include characters with dialogues and emotions.
```

---

## 👩‍💻 Author

**Fatima Nazeer** – [@fatimanazeer488@gmail.com](https://github.com/FatimaNazeer777)
Agentic AI Engineer & Frontend Developer

---

## 🧁 Future Ideas

* Upload selfie → get auto-caption using vision model
* Custom DP frame generator
* Voice-based rishta personality quiz
* Integration with Shaadi.com / Rishta apps
* Save and export checklist as PDF

---


