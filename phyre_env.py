"""
Wrapper for PHYRE benchmark
"""
import phyre
import random


class PhyreEnv(object):
    def __init__(self, seed):
        # Set seed
        random.seed(seed)

        # Simulators
        self.train_sim = None
        self.dev_sim = None
        self.test_sim = None


    def build_task_list(self, tier, fold, within=True, shuffle=False):
        """
        Builds a task list depending on tier and returns a dictionary
        """
        if tier == 'ball':
            eval_setup = ['ball_within_template', 'ball_cross_template']
        elif tier == 'two_ball':
            eval_setup = ['two_balls_within_template', 'two_balls_cross_template']
        else:
            raise ValueError("Unknown tier")

        if within:
            train_tasks, dev_tasks, test_tasks = phyre.get_fold(eval_setup[0], fold)
        else:
            train_tasks, dev_tasks, test_tasks = phyre.get_fold(eval_setup[1], fold)

        train_tasks = list(train_tasks)
        dev_tasks = list(dev_tasks)
        test_tasks = list(test_tasks)

        if shuffle:
            train_tasks = random.shuffle(train_tasks)
            dev_tasks = random.shuffle(dev_tasks)
            test_tasks = random.shuffle(test_tasks)

        task_dict = {
            'train_tasks': train_tasks,
            'dev_tasks': dev_tasks,
            'test_tasks': test_tasks
        }
        return task_dict

    def setup_sim(self, task_list, tier, sim_type='train'):
        """
        Sets up a simulator given tasks list and tier
        """
        if sim_type == 'train':
            self.train_sim = phyre.initialize_simulator(task_list, tier)
        elif sim_type == 'dev':
            self.dev_sim = phyre.initialize_simulator(task_list, tier)
        elif sim_type == 'test':
            self.test_sim = phyre.initialize_simulator(task_list, tier)
        else:
            raise ValueError("Unknown simulation setup")


