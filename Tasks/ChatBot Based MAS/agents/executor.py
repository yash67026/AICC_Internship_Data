class ResearcherAgent:
    def research(self, conversation):
        latest_query = conversation[-1]
        print(f"[Researcher] Processing: {latest_query}")
        
        return f"Research findings on '{latest_query}' with key insights."