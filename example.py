# Install necessary elements
from llama_index.llms.openai import OpenAI
from lavague.drivers.selenium import SeleniumDriver
from lavague.core import ActionEngine, WorldModel
from lavague.core.agents import WebAgent

# Set up our three key components: Driver, Action Engine, World Model
driver = SeleniumDriver(headless=False)
action_engine = ActionEngine(driver, llm=OpenAI(model="gpt-4o-mini"))
world_model = WorldModel()

# Create Web Agent
agent = WebAgent(world_model, action_engine)

# Set URL
agent.get("https://huggingface.co/docs")

# Run agent with a specific objective
# agent.run("Talk with ChatGPT about AI Technology Acceptance Model")
agent.run("Go on the quicktour of PEFT")

