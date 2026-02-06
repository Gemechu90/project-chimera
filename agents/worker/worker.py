from skills.trend_fetcher.skill import fetch_trends
from skills.content_generator.skill import generate_content
from skills.engagement_manager.skill import engage


class Worker:
    def execute(self, task):
        if task == "fetch_trends":
            return fetch_trends()
        if task == "generate_content":
            return generate_content("AI Influencers")
        if task == "engage":
            return engage("🔥 Trending Now: AI Influencers")
