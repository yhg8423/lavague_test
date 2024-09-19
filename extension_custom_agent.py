from llama_index.multi_modal_llms.anthropic import AnthropicMultiModal
from lavague.core import WorldModel, ActionEngine
from lavague.core.agents import WebAgent
from lavague.server.driver import DriverServer
from lavague.server import AgentServer, AgentSession

def create_agent(session: AgentSession):

    # Use custom multi-modal model
    anthropic_mm_llm = AnthropicMultiModal(model="claude-3-sonnet-20240229", max_tokens=3000) 
    world_model = WorldModel(mm_llm=anthropic_mm_llm)

    driver = DriverServer(session)
    action_engine = ActionEngine(driver)
    return WebAgent(world_model, action_engine)

server = AgentServer(create_agent)
server.serve()