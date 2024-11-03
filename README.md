# Marketing Swarm Template 🚀


[![Join our Discord](https://img.shields.io/badge/Discord-Join%20our%20server-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/agora-999382051935506503) [![Subscribe on YouTube](https://img.shields.io/badge/YouTube-Subscribe-red?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@kyegomez3242) [![Connect on LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/kye-g-38759a207/) [![Follow on X.com](https://img.shields.io/badge/X.com-Follow-1DA1F2?style=for-the-badge&logo=x&logoColor=white)](https://x.com/kyegomezb)


The Marketing Swarm Template is a powerful, easy-to-use framework built on top of [Swarms](https://github.com/kyegomez/swarms) for creating multi-platform marketing content using AI agents. This template implements Alex Hormozi's high-ticket offer frameworks across various platforms including Instagram, LinkedIn, Twitter, Email, TikTok, and more.

[![GitHub stars](https://img.shields.io/github/stars/The-Swarm-Corporation/Marketing-Swarm-Template)](https://github.com/The-Swarm-Corporation/Marketing-Swarm-Template/stargazers)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## 🌟 Features

- 10+ specialized marketing agents for different platforms
- Hormozi-style high-ticket offer frameworks
- Template-based system for easy customization
- Platform-specific content strategies
- Automated content generation across channels
- Value-first marketing approach
- Clear call-to-action frameworks

## 🚀 Quick Start

### 1. Installation

```bash
# Install the Swarms framework
pip install -U swarms

# Clone this repository
git clone https://github.com/The-Swarm-Corporation/Marketing-Swarm-Template
cd Marketing-Swarm-Template
pip install -r requirements.txt
```

### 2. Set Up Environment

Create a `.env` file with your configuration:

```env
# API Keys
GROQ_API_KEY=your_api_key_here # Or OpenAI API Key (OPENAI_API_KEY=your_api_key_here)
# Company Information
COMPANY_NAME=Your Company Name
PRODUCT_NAME=Your Product Name
INDUSTRY=Your Industry
PAIN_POINT=Your Main Pain Point
DESIRED_OUTCOME=Your Desired Outcome
TARGET_AUDIENCE=Your Target Audience
EXPERTISE_AREA=Your Area of Expertise
LEAD_MAGNET=Your Lead Magnet
CONSULTATION_TYPE=Your Consultation Type
TOPIC=Your Main Topic
WORKSHOP_NAME=Your Workshop Name
TIMEFRAME=Your Timeframe
WEBSITE=your-website.com
CALENDAR_LINK=your-calendar-link
```

### 3. Run the Swarm

```python
python3 main.py
```

## 📚 Available Agents

1. **Instagram Content Strategy Agent**
   - Carousel posts
   - Story sequences
   - Reel scripts
   - Bio optimization

2. **LinkedIn Authority Builder Agent**
   - Thought leadership content
   - Case study posts
   - B2B conversion frameworks

3. **TikTok Viral Content Agent**
   - Hook-based content
   - Pattern interrupts
   - Transformation showcases

4. **Email Newsletter Conversion Agent**
   - Welcome sequences
   - Nurture campaigns
   - Sales sequences
   - Re-engagement campaigns

5. **Twitter Thread Mastery Agent**
   - Educational threads
   - Authority building
   - Engagement optimization

And more! Check `agents.yaml` for the complete list.

## 🛠️ Customization

### Modifying Agent Templates

Each agent in `agents.yaml` can be customized:

```yaml
- agent_name: "Platform-Content-Agent"
  system_prompt: |
    You are a specialized agent for [PLATFORM]. Your task is to...
  max_loops: 1
  autosave: true
  verbose: true
  context_length: 200000
  output_type: "str"
```

### Adding New Agents

Create new agents by adding them to `agents.yaml`:

```yaml
- agent_name: "Your-New-Agent"
  system_prompt: |
    Your custom prompt here...
  # Add configuration options
```

## 📊 Example Output

```python
# Example results from Twitter Thread Agent
results = {
    "thread_hook": "Want to 10x your [INDUSTRY] results?",
    "thread_content": [
        "Here's how we helped [COMPANY_NAME] achieve...",
        "Step 1: [STRATEGY]",
        # More content
    ],
    "call_to_action": "DM 'INFO' for our free [LEAD_MAGNET]"
}
```

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 💫 Built With Swarms

This template is powered by the [Swarms](https://github.com/kyegomez/swarms) framework. Check out the Swarms documentation for more information about building powerful AI agent systems.

## 🙏 Acknowledgments

- [Swarms Framework](https://github.com/kyegomez/swarms)
- Alex Hormozi for the high-ticket offer frameworks
- The Swarm Corporation team

---

Made with ❤️ by [The Swarm Corporation](https://github.com/The-Swarm-Corporation)