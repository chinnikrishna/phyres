"""
Physical Reasoning
"""
import phyre
import argparse
from phyre_env import PhyreEnv

def run(seed, tier, fold):
    env = PhyreEnv(seed)
    task_dict = env.build_task_list(tier, fold)
    train_tasks = task_dict['train_tasks']
    train_sim = env.setup_sim(train_tasks, tier)
    import pdb
    pdb.set_trace()
    print("Turrr")


if __name__ == "__main__":
    cmd_parser = argparse.ArgumentParser()
    cmd_parser.add_argument("--tier", "-t", type=str, default="ball", help="Task tier")
    cmd_parser.add_argument("--fold", "-f", type=int, default=10, help="Validation fold")
    cmd_parser.add_argument("--seed", "-s", type=int, default=42, help="Seed for randomization")
    cmd_args = cmd_parser.parse_args()
    run(cmd_args.seed, cmd_args.tier, cmd_args.fold)
