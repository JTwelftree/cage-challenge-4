import sys
import traceback

try:
    from CybORG import CybORG
    from CybORG.Simulator.Scenarios.EnterpriseScenarioGenerator import EnterpriseScenarioGenerator

    # Create the scenario generator and environment
    sg = EnterpriseScenarioGenerator()
    cyborg = CybORG(sg, 'sim')

    # Optionally inspect a brief summary
    print('CybORG environment created:', type(cyborg), 'with scenario:', type(sg))
except Exception:
    traceback.print_exc()
    sys.exit(1)
