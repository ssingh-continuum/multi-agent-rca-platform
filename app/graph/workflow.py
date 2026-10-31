from typing import TypedDict

from langgraph.graph import StateGraph, END

from agents.log_agent import LogAgent
from agents.metrics_agent import MetricsAgent
from agents.rag_agent import RagAgent
from agents.rca_agent import RCAAgent
from agents.recommendation_agent import RecommendationAgent


# ----------------------------------
# Shared State
# ----------------------------------

class IncidentState(TypedDict):
    incident: str
    logs: str
    metrics: str
    history: str
    rca: str
    recommendation: str


# ----------------------------------
# Agent Instances
# ----------------------------------

log_agent = LogAgent()

metrics_agent = MetricsAgent()

rag_agent = RagAgent()

rca_agent = RCAAgent()

recommendation_agent = RecommendationAgent()


# ----------------------------------
# Nodes
# ----------------------------------

def log_node(state: IncidentState):

    print("\n========== LOG AGENT ==========")

    state["logs"] = log_agent.analyze(
        state["incident"]
    )

    print(state["logs"])

    return state


def metrics_node(state: IncidentState):

    print("\n========== METRICS AGENT ==========")

    state["metrics"] = metrics_agent.analyze()

    print(state["metrics"])

    return state


def rag_node(state: IncidentState):

    print("\n========== RAG AGENT ==========")

    state["history"] = rag_agent.retrieve(
        state["incident"]
    )

    print(state["history"])

    return state


def rca_node(state: IncidentState):

    print("\n========== RCA AGENT ==========")

    state["rca"] = rca_agent.analyze(
        incident=state["incident"],
        logs=state["logs"],
        metrics=state["metrics"],
        history=state["history"]
    )

    return state


def recommendation_node(state: IncidentState):

    print("\n========== RECOMMENDATION AGENT ==========")

    state["recommendation"] = (
        recommendation_agent.generate(
            state["rca"]
        )
    )

    return state


# ----------------------------------
# Graph Definition
# ----------------------------------

builder = StateGraph(IncidentState)

builder.add_node(
    "log_analysis",
    log_node
)

builder.add_node(
    "metrics_analysis",
    metrics_node
)

builder.add_node(
    "rag_search",
    rag_node
)

builder.add_node(
    "rca_analysis",
    rca_node
)

builder.add_node(
    "recommendation",
    recommendation_node
)


# ----------------------------------
# Flow
# ----------------------------------

builder.set_entry_point(
    "log_analysis"
)

builder.add_edge(
    "log_analysis",
    "metrics_analysis"
)

builder.add_edge(
    "metrics_analysis",
    "rag_search"
)

builder.add_edge(
    "rag_search",
    "rca_analysis"
)

builder.add_edge(
    "rca_analysis",
    "recommendation"
)

builder.add_edge(
    "recommendation",
    END
)


# ----------------------------------
# Compile
# ----------------------------------

workflow = builder.compile()