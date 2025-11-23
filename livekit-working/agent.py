import logging
from dotenv import load_dotenv
from livekit import agents
from livekit.agents import Agent, AgentSession, JobContext, WorkerOptions, cli
from livekit.plugins import groq, deepgram
from livekit.plugins.silero import VAD

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def entrypoint(ctx: JobContext):
    """Main entrypoint for the LiveKit agent"""
    
    # Connect to the room
    logger.info(f"Connecting to room: {ctx.room.name}")
    await ctx.connect()
    logger.info("Connected to room successfully")
    
    # Create the Agent with optimized instructions
    agent = Agent(
        instructions="""You are a mock interviewer. Keep it brief and natural.

RULES:
- Ask ONE question at a time, then STOP
- Keep responses to 1-2 sentences maximum
- Never list multiple questions in one turn
- Wait for the candidate to finish before responding

FLOW:
1. First, ask what role they're interviewing for
2. Ask 4-5 interview questions one at a time
3. Give brief feedback only at the very end

STYLE:
- Be conversational like a real interviewer
- Ask follow-ups based on their specific answers
- If answer is vague: "Can you elaborate on that?"
- If off-topic: "Let's refocus on the interview question"
- Don't explain your process - just interview naturally

FEEDBACK (end only):
- Mention 1-2 strengths
- Suggest 1-2 improvements
- Keep total feedback under 30 seconds when spoken""",
        
        # Configure endpointing for faster turn detection
        min_endpointing_delay=0.4,  # Detect end of speech faster (was 0.5)
        max_endpointing_delay=5.0,  # Max wait time reduced (was 6.0)
        
        # Allow interruptions for natural conversation
        allow_interruptions=True,
    )
    
    # Create AgentSession with optimized components
    session = AgentSession(
        # VAD: Optimized for low latency voice detection
        vad=VAD.load(
            min_silence_duration=0.5,  # 500ms silence = turn end (fast response)
            min_speech_duration=0.1,   # 100ms to detect speech start
            activation_threshold=0.5,  # Balanced sensitivity
        ),
        
        # STT: Deepgram Nova-2 (fastest model)
        stt=deepgram.STT(
            model="nova-2",
            language="en",
            smart_format=True,  # Auto punctuation & formatting
        ),
        
        # LLM: Fast 8B model for instant responses
        llm=groq.LLM(
            model="llama-3.1-8b-instant",  # Fastest model (was 70B)
            temperature=0.7,  # Balanced creativity
        ),
        
        # TTS: Deepgram with natural voice
        tts=deepgram.TTS(
            model="aura-asteria-en",
            encoding="linear16",
            sample_rate=24000,
        ),
        
        # Optimize turn detection
        min_endpointing_delay=0.4,  # Faster turn detection
        max_endpointing_delay=5.0,  # Don't wait too long
        
        # Interruption settings for natural flow
        allow_interruptions=True,
        min_interruption_duration=0.5,  # 500ms speech = interruption
        
        # Consecutive speech delay (prevent rapid-fire responses)
        min_consecutive_speech_delay=0.3,  # Small gap between agent utterances
        
        # User away timeout
        user_away_timeout=20.0,  # 20 seconds of silence = user away
    )
    
    # Start the session
    await session.start(agent=agent, room=ctx.room)
    logger.info("✅ Agent started and listening!")
    
    # Generate initial greeting (brief and welcoming)
    await session.generate_reply(
        instructions="Greet the user briefly and ask what role they're interviewing for. Keep it under 2 sentences."
    )


if __name__ == "__main__":
    cli.run_app(
        WorkerOptions(
            entrypoint_fnc=entrypoint,
        )
    )