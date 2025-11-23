# AI Interview Coach - LiveKit Voice Agent

An AI-powered mock interview assistant built with LiveKit Agents Framework. This application provides real-time voice-based interview practice using state-of-the-art AI models for speech recognition, language processing, and text-to-speech.

## 🎯 Features

- **Real-time Voice Interaction**: Natural conversation flow with low-latency responses
- **Smart Interview Flow**: Asks one question at a time and provides personalized feedback
- **Advanced AI Models**: 
  - **STT**: Deepgram Nova-2 for fast and accurate speech recognition
  - **LLM**: Groq's Llama 3.1 8B Instant for intelligent responses
  - **TTS**: Deepgram Aura for natural-sounding voice
- **Interruption Handling**: Natural conversation with support for interruptions
- **Optimized Turn Detection**: Fast response times with Silero VAD

## 📋 Prerequisites

- Python 3.9 or higher
- A LiveKit Cloud account or self-hosted LiveKit server
- API keys for:
  - LiveKit
  - Groq
  - Deepgram

## 🔑 Getting API Keys

### 1. LiveKit API Credentials

LiveKit provides the infrastructure for real-time audio streaming.

**Steps to get LiveKit credentials:**

1. Go to [LiveKit Cloud](https://cloud.livekit.io/)
2. Sign up for a free account or log in
3. Create a new project:
   - Click on **"New Project"**
   - Give your project a name (e.g., "AI Interview Coach")
   - Select a region closest to you
4. Once the project is created, go to **Settings** → **Keys**
5. Click **"Create Key"** to generate new API credentials
6. Copy the following values:
   - `LIVEKIT_URL` (e.g., `wss://your-project.livekit.cloud`)
   - `LIVEKIT_API_KEY`
   - `LIVEKIT_API_SECRET`

> **Note**: Keep your API secret secure and never commit it to version control!

### 2. Groq API Key

Groq provides ultra-fast LLM inference for the interview agent's intelligence.

**Steps to get Groq API key:**

1. Visit [Groq Console](https://console.groq.com/)
2. Sign up for a free account or log in
3. Navigate to **API Keys** section
4. Click **"Create API Key"**
5. Give it a name (e.g., "interview-agent")
6. Copy the generated API key (starts with `gsk_...`)

> **Free Tier**: Groq offers generous free tier limits perfect for development and testing.

### 3. Deepgram API Key

Deepgram powers both speech-to-text and text-to-speech capabilities.

**Steps to get Deepgram API key:**

1. Go to [Deepgram Console](https://console.deepgram.com/)
2. Create a free account or sign in
3. Navigate to **API Keys** in the dashboard
4. Click **"Create a New API Key"**
5. Give it a name (e.g., "interview-coach")
6. Copy the generated API key

> **Free Credits**: Deepgram provides $200 in free credits for new users.

## 🚀 Installation

### Step 1: Clone the Repository

```bash
git clone <your-repository-url>
cd new-genapp-v8
```

### Step 2: Create Virtual Environment

**On Windows:**
```bash
# Navigate to the project directory
cd livekit-working

# Create virtual environment
python -m venv .

# Activate virtual environment
.\Scripts\activate
```

**On macOS/Linux:**
```bash
# Navigate to the project directory
cd livekit-working

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install livekit livekit-agents livekit-plugins-deepgram livekit-plugins-groq livekit-plugins-silero python-dotenv
```

### Step 4: Configure Environment Variables

Create a `.env` file in the `livekit-working` directory:

```bash
# Copy the example below or create manually
touch .env
```

Add the following content to your `.env` file:

```env
# LiveKit Configuration
LIVEKIT_URL=wss://your-project.livekit.cloud
LIVEKIT_API_KEY=your_livekit_api_key
LIVEKIT_API_SECRET=your_livekit_api_secret

# Groq Configuration
GROQ_API_KEY=your_groq_api_key

# Deepgram Configuration
DEEPGRAM_API_KEY=your_deepgram_api_key
```

Replace the placeholder values with your actual API keys obtained from the steps above.

## 🎮 Running the Agent

### Step 1: Start the LiveKit Agent

Make sure your virtual environment is activated, then run:

```bash
python agent.py dev
```

You should see output indicating the agent is running:
```
✅ Agent started and listening!
```

### Step 2: Access the Playground

1. Open your browser and navigate to: **[LiveKit Playground](https://agents-playground.livekit.io/)**

2. **Connect to your agent:**
   - Enter your `LIVEKIT_URL` (e.g., `wss://your-project.livekit.cloud`)
   - Click **"Connect"**

3. **Configure audio settings:**
   - Allow microphone access when prompted
   - Adjust your microphone and speaker settings as needed

4. **Start interviewing:**
   - Click the **"Start"** button
   - The agent will greet you and ask what role you're interviewing for
   - Have a natural conversation with the AI interviewer!

### Alternative: Use LiveKit Meet (for testing)

You can also test using LiveKit Meet:

1. Go to your LiveKit Cloud dashboard
2. Navigate to your project
3. Click on **"Rooms"** → **"Create Room"**
4. Join the room and the agent should automatically connect

## 🛠️ Project Structure

```
new-genapp-v8/
├── livekit-working/
│   ├── agent.py              # Main agent code
│   ├── .env                  # Environment variables (create this)
│   ├── Scripts/              # Virtual environment scripts (Windows)
│   ├── Lib/                  # Virtual environment libraries
│   └── Include/              # Virtual environment includes
├── .gitignore
└── README.md
```

## ⚙️ Configuration Options

The agent is highly configurable. Key settings in `agent.py`:

- **`min_endpointing_delay`**: How quickly the agent detects end of speech (default: 0.4s)
- **`max_endpointing_delay`**: Maximum wait time for user speech (default: 5.0s)
- **`allow_interruptions`**: Enable natural interruptions (default: True)
- **`min_silence_duration`**: Silence duration to detect turn end (default: 0.5s)
- **LLM Model**: Currently using `llama-3.1-8b-instant` for speed
- **TTS Voice**: Using `aura-asteria-en` for natural female voice

## 🐛 Troubleshooting

### Agent won't connect
- Verify your `.env` file has correct credentials
- Check that your LiveKit project is active
- Ensure virtual environment is activated

### No audio in/out
- Check browser microphone permissions
- Verify audio devices are selected in playground
- Test with LiveKit Meet first to isolate issues

### Slow responses
- Check your internet connection
- Verify you're using the `8b-instant` model (not 70B)
- Consider reducing `min_endpointing_delay` further

### API quota errors
- Check your API usage in respective dashboards (Groq/Deepgram)
- Free tiers have rate limits - upgrade if needed
- Groq free tier: 30 requests/minute

## 📝 Environment Variables Reference

| Variable | Description | Example |
|----------|-------------|---------|
| `LIVEKIT_URL` | Your LiveKit server URL | `wss://project.livekit.cloud` |
| `LIVEKIT_API_KEY` | LiveKit API key | `APIxxxxxxxxxxxxx` |
| `LIVEKIT_API_SECRET` | LiveKit API secret | `secretxxxxxxxxxx` |
| `GROQ_API_KEY` | Groq API key for LLM | `gsk_xxxxxxxxxxxx` |
| `DEEPGRAM_API_KEY` | Deepgram API key for STT/TTS | `xxxxxxxxxxxxxxxx` |

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.

## 🔗 Useful Links

- [LiveKit Documentation](https://docs.livekit.io/)
- [LiveKit Agents Framework](https://docs.livekit.io/agents/)
- [Groq Documentation](https://console.groq.com/docs)
- [Deepgram Documentation](https://developers.deepgram.com/)
- [LiveKit Playground](https://agents-playground.livekit.io/)

## 💡 Tips for Better Interviews

- Speak clearly and at a normal pace
- Wait for the agent to finish before responding
- If you need clarification, just ask!
- The agent is designed to ask one question at a time
- You'll receive feedback at the end of the interview

---

**Built with ❤️ using LiveKit Agents Framework**
