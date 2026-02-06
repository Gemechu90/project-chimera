from agents.planner.planner import Planner
from agents.worker.worker import Worker
from agents.judge.judge import Judge

def test_full_pipeline():
    planner = Planner()
    worker = Worker()
    judge = Judge()

    for step in planner.plan():
        result = worker.execute(step["task"])
        assert judge.approve(result)
