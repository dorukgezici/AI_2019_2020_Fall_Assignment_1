import time
import sys
import os


#  import constant definitions
from macros import *


#  import game class
from hamham import Game



#  import agents
from agent import Agent
from bfs_agent import BFSAgent
from dfs_agent import DFSAgent
from astar_agent import AStarAgent



#  Initialize game
hamham = Game()



#  to prevent infinite loop while playing, just in case
MAX_EPISODE_LENGTH = 1000



#First command line argument is player_string
player_string = ""
if (len(sys.argv) >= 2):
    player_string = sys.argv[1]
else:
    #  no argument is provided, assign player_string hardcodedly
    player_string = "HUMAN"
    #player_string = "RANDOM"
    #player_string = "BFS"
    #player_string = "DFS"
    #player_string = "ASTAR"
player_string = player_string.upper()


#Second command line argument is played level
PLAYED_LEVEL = 1
if (len(sys.argv) >= 3):
    PLAYED_LEVEL = int(sys.argv[2])
else:
    PLAYED_LEVEL = 1




#  display player and played level
print("Player {} will be playing level {}".format(player_string, PLAYED_LEVEL))













if (player_string == "HUMAN"):
    (collected_apple_count, elapsed_time_step) = hamham.start_level_human(PLAYED_LEVEL)
    printed_str = "--- Player Statistics ---\n"
    printed_str += "collected apple count:{}\n".format(collected_apple_count)
    printed_str += "elapsed time step:{}\n".format(elapsed_time_step)
    print(printed_str)
elif (player_string == "BFS"):
    agent = BFSAgent()
    (collected_apple_count, elapsed_time_step, elapsed_solve_time, result) = hamham.start_level_computer(PLAYED_LEVEL, agent, 
                                                                                render=True, play_sound=True,
                                                                                max_episode_length=MAX_EPISODE_LENGTH,
                                                                                test=True)
    printed_str = "--- BFS Agent Statistics ---\n"
    printed_str += "collected apple count:{}\n".format(collected_apple_count)
    printed_str += "elapsed time step:{}\n".format(elapsed_time_step)
    printed_str += "number of generated nodes:{}\n".format(agent.generated_node_count)
    printed_str += "number of expanded nodes:{}\n".format(agent.expanded_node_count)
    printed_str += "maximum number of nodes kept in memory:{}\n".format(agent.maximum_node_in_memory_count)
    printed_str += "elapsed solve time:{}\n".format(elapsed_solve_time)
    if (result == RESULT_PLAYER_WON):
        printed_str += "WON\n"
    else:
        printed_str += "FAIL\n"
    print(printed_str)
elif (player_string == "DFS"):
    agent = DFSAgent()
    (collected_apple_count, elapsed_time_step, elapsed_solve_time, result) = hamham.start_level_computer(PLAYED_LEVEL, agent, 
                                                                                render=True, play_sound=True,
                                                                                max_episode_length=MAX_EPISODE_LENGTH,
                                                                                test=True)
    printed_str = "--- DFS Agent Statistics ---\n"
    printed_str += "collected apple count:{}\n".format(collected_apple_count)
    printed_str += "elapsed time step:{}\n".format(elapsed_time_step)
    printed_str += "number of generated nodes:{}\n".format(agent.generated_node_count)
    printed_str += "number of expanded nodes:{}\n".format(agent.expanded_node_count)
    printed_str += "maximum number of nodes kept in memory:{}\n".format(agent.maximum_node_in_memory_count)
    printed_str += "elapsed solve time:{}\n".format(elapsed_solve_time)
    if (result == RESULT_PLAYER_WON):
        printed_str += "WON\n"
    else:
        printed_str += "FAIL\n"
    print(printed_str)
elif (player_string == "ASTAR"):
    agent = AStarAgent()
    (collected_apple_count, elapsed_time_step, elapsed_solve_time, result) = hamham.start_level_computer(PLAYED_LEVEL, agent, 
                                                                                render=True, play_sound=True,
                                                                                max_episode_length=MAX_EPISODE_LENGTH,
                                                                                test=True)
    printed_str = "--- A* Agent Statistics ---\n"
    printed_str += "collected apple count:{}\n".format(collected_apple_count)
    printed_str += "elapsed time step:{}\n".format(elapsed_time_step)
    printed_str += "number of generated nodes:{}\n".format(agent.generated_node_count)
    printed_str += "number of expanded nodes:{}\n".format(agent.expanded_node_count)
    printed_str += "maximum number of nodes kept in memory:{}\n".format(agent.maximum_node_in_memory_count)
    printed_str += "elapsed solve time:{}\n".format(elapsed_solve_time)
    if (result == RESULT_PLAYER_WON):
        printed_str += "WON\n"
    else:
        printed_str += "FAIL\n"
    print(printed_str)