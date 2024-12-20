from EventManager.Models.RunnerEvents import RunnerEvents
from EventManager.EventSubscriptionController import EventSubscriptionController
from ConfigValidator.Config.Models.RunTableModel import RunTableModel
from ConfigValidator.Config.Models.FactorModel import FactorModel
from ConfigValidator.Config.Models.RunnerContext import RunnerContext
from ConfigValidator.Config.Models.OperationType import OperationType
from ProgressManager.Output.OutputProcedure import OutputProcedure as output

from typing import Dict, List, Any, Optional
from pathlib import Path
from os.path import dirname, realpath

import os
import signal
import pandas as pd
import time
import subprocess
import shlex


class RunnerConfig:
    ROOT_DIR = Path(dirname(realpath(__file__)))

    # ================================ USER SPECIFIC CONFIG ================================
    """The name of the experiment."""
    name:                       str             = "new_runner_experiment"

    """The path in which Experiment Runner will create a folder with the name `self.name`, in order to store the
    results from this experiment. (Path does not need to exist - it will be created if necessary.)
    Output path defaults to the config file's path, inside the folder 'experiments'"""
    results_output_path:        Path             = ROOT_DIR / 'experiments'

    """Experiment operation type. Unless you manually want to initiate each run, use `OperationType.AUTO`."""
    operation_type:             OperationType   = OperationType.AUTO

    """The time Experiment Runner will wait after a run completes.
    This can be essential to accommodate for cooldown periods on some systems."""
    time_between_runs_in_ms:    int             = 1000

    # Dynamic configurations can be one-time satisfied here before the program takes the config as-is
    # e.g. Setting some variable based on some criteria
    def __init__(self):
        """Executes immediately after program start, on config load"""

        EventSubscriptionController.subscribe_to_multiple_events([
            (RunnerEvents.BEFORE_EXPERIMENT, self.before_experiment),
            (RunnerEvents.BEFORE_RUN       , self.before_run       ),
            (RunnerEvents.START_RUN        , self.start_run        ),
            (RunnerEvents.START_MEASUREMENT, self.start_measurement),
            (RunnerEvents.INTERACT         , self.interact         ),
            (RunnerEvents.STOP_MEASUREMENT , self.stop_measurement ),
            (RunnerEvents.STOP_RUN         , self.stop_run         ),
            (RunnerEvents.POPULATE_RUN_DATA, self.populate_run_data),
            (RunnerEvents.AFTER_EXPERIMENT , self.after_experiment )
        ])
        self.run_table_model = None  # Initialized later
        output.console_log("Custom config loaded")

    def create_run_table_model(self) -> RunTableModel:
        """Create and return the run_table model here. A run_table is a List (rows) of tuples (columns),
        representing each run performed"""
        run_factor = FactorModel("run_number", ['r'+str(i) for i in range(0, 20)])
        problem_factor = FactorModel("problem", ['O_n_problem', 'O_nlogn_problem', 'O_n2_problem'])
        prompt_factor = FactorModel("prompts", ['human','base_prompt','few_shot_prompt','instructed_prompt_slen','instructed_prompt_llen','instructed_prompt_de'])
        self.run_table_model = RunTableModel(
            factors = [run_factor, problem_factor, prompt_factor],
            data_columns=['execution_time', 'cpu_usage', 'memory_usage', 'energy_consumption'], 
            # repetitions = 2,
            shuffle=True
            )
        return self.run_table_model

    def before_experiment(self) -> None:
        """Perform any activity required before starting the experiment here
        Invoked only once during the lifetime of the program."""
        output.console_log("Config.before_experiment() called!")

    def before_run(self) -> None:
        """Perform any activity required before starting a run.
        No context is available here as the run is not yet active (BEFORE RUN)"""
        output.console_log("Config.before_run() called!")
      

    def start_run(self, context: RunnerContext) -> None:
        """Perform any activity required for starting the run here.
        For example, starting the target system to measure.
        Activities after starting the run should also be performed here."""
        # start the target
        
        


    def start_measurement(self, context: RunnerContext) -> None:
        """Perform any activity required for starting measurements."""
        output.console_log("Config.start_measurement() called!")
        
        problem = context.run_variation["problem"]
        prompt_type = context.run_variation["prompts"]   
        profiler_cmd = f'energibridge \
                        --interval 200 \
                        --output {context.run_dir / "energibridge.csv"}\
                        --summary python experiments/runner/{problem}/{prompt_type}.py'

        #time.sleep(1) # allow the process to run a little before measuring
        
        self.profiler = subprocess.Popen(shlex.split(profiler_cmd)) # stdout=energibridge_log


    def interact(self, context: RunnerContext) -> None:
        """Perform any interaction with the running target system here, or block here until the target finishes."""

        # No interaction. We just run it for XX seconds.
        # Another example would be to wait for the target to finish, e.g. via `self.target.wait()`


    def stop_measurement(self, context: RunnerContext) -> None:
        """Perform any activity here required for stopping measurements."""
        
        
        self.profiler.wait()
	#output.console_log("Waiting for profiler stop...")

    def stop_run(self, context: RunnerContext) -> None:
        """Perform any activity here required for stopping the run.
        Activities after stopping the run should also be performed here."""
        
        #self.target.kill()
        #self.target.wait()
        #self.timestamp_end = datetime.now()
        output.console_log("Config.stop_run() called!")
    
    def populate_run_data(self, context: RunnerContext) -> Optional[Dict[str, Any]]:
        """Parse and process any measurement data here.
        You can also store the raw measurement data under `context.run_dir`
        Returns a dictionary with keys `self.run_table_model.data_columns` and their values populated"""

        # energibridge.csv - Power consumption of the whole system
        
        df = pd.read_csv(context.run_dir / f"energibridge.csv")
                
 	# calculate the CPU USAGE
        all_data = None
        nb_point = 0
        for metric in df.columns[1:]:  
            if 'CPU_USAGE' in metric:
                nb_point += 1
                if all_data is None:
                    all_data = df[metric].copy()
                else:
                    all_data += df[metric]
 
       
        run_data = {
                'execution_time': round((df['Time'].iloc[-1] - df['Time'].iloc[0])/1000, 3),
                'cpu_usage'    : round((all_data/nb_point).mean(), 3),     
                'memory_usage'    : round(df['USED_MEMORY'].sum()*100/df['TOTAL_MEMORY'].sum(), 3),
                'energy_usage': round(df['SYSTEM_POWER (Watts)'].mean(), 3)
        }
        return run_data

    def after_experiment(self) -> None:
        """Perform any activity required after stopping the experiment here
        Invoked only once during the lifetime of the program."""
        pass

    # ================================ DO NOT ALTER BELOW THIS LINE ================================
    experiment_path:            Path             = None
