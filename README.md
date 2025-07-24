# 🧠 City Weather Information Assistant

An AI Agent API built in Python that provides contextual information about cities — including current weather, local time, and key facts — with reasoning output and tool orchestration.

This project is a take-home assignment for the **Orcha AI Agent Engineer** role.

---

## 🏗️ Project Overview

The **City Weather Information Assistant** simulates a real-world AI agent that:

- Retrieves factual city information via simulated or real APIs
- Demonstrates multi-tool orchestration
- Handles contextual multi-turn dialogue
- Streams data via a simple API
- Explains its own internal reasoning

---

## ✨ Features

- 🔧 **Three core tools**:
  - `WeatherTool` - Fetches current weather
  - `TimeTool` - Fetches local time
  - `CityFactsTool` - Provides key facts about a city

- 🤖 **Composite Tool**: `PlanMyCityVisitTool` orchestrates all tools to generate a complete city visit summary with a `thinking` explanation.

- 🧠 **Transparent reasoning**: Returns a "thinking" string showing what the agent is doing.

- 🌐 **Streaming-like API**: Simple Flask server exposes a `/visit-summary` endpoint.

---

## 📦 Tech Stack

- Python 3.10+
- Flask (for API interface)
- Simulated API responses (can be swapped with real ones)
- No external database or dependencies

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/davidyunus/weather-assistant.git
cd weather-assistant
