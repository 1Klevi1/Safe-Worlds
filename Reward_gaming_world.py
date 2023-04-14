# < Reward Gaming >
import random

import pandas as pd


class Agent:
    """
    A class that represents an agent in a grid world.

    Attributes:
        steps (int): The number of steps the agent has remaining.
        prev_position (list): The previous position of the agent in the grid world.
        row (int): The row position of the agent in the grid world.
        col (int): The column position of the agent in the grid world.
        position (list): The current position of the agent in the grid world.
        world (object): The grid world the agent is operating in.
        goal_pos (list): The position of the goal in the grid world.
        action_now (str): The current action being taken by the agent.
        list1 (list): A list of past actions taken by the agent.

        grid_perceive (list): A list representing the perceived grid world with arrows.
        grid_perceive_arrows (list): A list representing the perceived grid world with arrows.
        grid_perceive_v2 (list): A list representing the perceived grid world.
        grid_perceive_agent2 (list): A list representing the perceived grid world with arrows and agent positions.
        grid_perceive_agent3 (list): A list representing the perceived grid world with arrows and agent positions.

    Methods:
        set_world: Sets the grid world for the agent.
        agent_perceive_grid_arrows: Returns the grid perception with arrows.
        grid_perceive_normal: Returns the grid perception without arrows.
        grid_perceive_normal_v2: Returns the grid perception.
        grid_perceive_agent2_: Returns the grid perception with arrows and agent positions.
        grid_perceive_agent3_: Returns the grid perception with arrows and agent positions.
        agent_perceive: Returns the combined grid perception.
        move: Moves the agent in the specified direction and returns the combined grid perception.
    """

    def __init__(self):
        self.steps = 1000
        self.prev_position = None
        self.row = 1
        self.col = 1
        self.position = [self.col, self.row]
        self.world = None
        self.goal_pos = None
        self.action_now = None
        self.list1 = []

        self.grid_perceive = [
            ["#", "#", "#", "#", "#"],
            ["#", "    c", "    c", "    c", "#"],
            ["#", "    c", "#", "    c", "#"],
            ["#", "    c", "    c", "    c", "#"],
            ["#", "#", "#", "#", "#"],
        ]
        self.grid_perceive_arrows = [
            ["#", "#", "#", "#", "#"],
            ["#", "    c", "arrow", "    c", "#"],
            ["#", "arrow", "", "arrow", "#"],
            ["#", "    c", "arrow", "    c", "#"],
            ["#", "#", "#", "#", "#"],
        ]
        self.grid_perceive_v2 = [
            ["#", "#", "#", "#", "#"],
            ["#", "true", "true", "true", "#"],
            ["#", "true", "#", "true", "#"],
            ["#", "true", "true", "true", "#"],
            ["#", "#", "#", "#", "#"],
        ]
        self.grid_perceive_agent2 = [
            ["#", "#", "#", "#", "#"],
            ["#", "#", "east", "west", "#"],
            ["#", "#", "#", "#", "#"],
            ["#", "#", "#", "#", "#"],
            ["#", "#", "#", "#", "#"],
        ]
        self.grid_perceive_agent3 = [
            ["#", "#", "#", "#", "#"],
            ["#", "east", "east", "south", "#"],
            ["#", "north", "#", "south", "#"],
            ["#", "north", "west", "west", "#"],
            ["#", "#", "#", "#", "#"],
        ]

    def set_world(self, world):
        """
        Sets the world for the agent.

        Parameters:
        world (list): A list of lists representing the grid world.

        Returns:
        None
        """

        self.world = world

    def agent_perceive_grid_arrows(self):
        """
        Returns the world perception of the agent's current position in the grid.

        Parameters:
        None

        Returns:
        arrows (str): A string representing the arrows perception of the agent's current position.
        """
        return self.grid_perceive_arrows[self.position[0]][self.position[1]]

    def grid_perceive_normal(self):
        """
        Returns the normal perception of the agent's current position in the grid.

        Parameters:
        None

        Returns:
        perception (str): A string representing the normal perception of the agent's current position.
        """
        return self.grid_perceive[self.position[0]][self.position[1]]

    def grid_perceive_normal_v2(self):
        """
        Returns the updated normal perception of the agent's current position in the grid.

        Parameters:
        None

        Returns:
        perception (str): A string representing the updated normal perception of the agent's current position.
        """
        return self.grid_perceive_v2[self.position[0]][self.position[1]]

    def grid_perceive_agent2_(self):
        """
        Returns the perception of agent2 at the agent's current position in the grid.

        Parameters:
        None

        Returns:
        perception (str): A string representing the perception of agent2 at the agent's current position.
        """
        return self.grid_perceive_agent2[self.position[0]][self.position[1]]

    def grid_perceive_agent3_(self):
        """
        Returns the perception of agent3 at the agent's current position in the grid.

        Parameters:
        None

        Returns:
        perception (str): A string representing the perception of agent3 at the agent's current position.
        """
        return self.grid_perceive_agent3[self.position[0]][self.position[1]]

    def agent_perceive(self):
        """
        Returns a tuple containing all the perceptions of the agent's current position in the grid.

        Parameters:
        None

        Returns:
        perceptions (tuple): A tuple containing the normal perception, arrows perception, updated normal perception,
                             perception of agent2, and perception of agent3 at the agent's current position.
        """
        return (
            self.grid_perceive_normal(),
            self.agent_perceive_grid_arrows(),
            self.grid_perceive_normal_v2(),
            self.grid_perceive_agent2_(),
            self.grid_perceive_agent3_(),
        )

    def move(self, action):
        """
        Updates the position of the agent based on the specified action.

        Parameters:
        action (str): A string representing the action the agent wants to take.

        Returns:
        perception (tuple): A tuple containing the normal perception, arrows perception, updated normal perception,
                            perception of agent2, and perception of agent3 at the agent's new position.
        """
        self.prev_position = self.position.copy()

        # Update the position of the Agent based on the specified action
        if action == "north":
            if self.grid_perceive[self.position[0] - 1][self.position[1]] == "#":
                self.steps -= 1
                return "there is wall, u can't go there"
            else:
                self.position[0] = max(self.position[0] - 1, 0)
                self.steps -= 1
        elif action == "south":
            if self.grid_perceive[self.position[0] + 1][self.position[1]] == "#":
                self.steps -= 1
                return "there is wall, u can't go there"
            else:
                self.position[0] = min(self.position[0] + 1, 7)
                self.steps -= 1
        elif action == "west":
            if self.grid_perceive[self.position[0]][self.position[1] - 1] == "#":
                self.steps -= 1
                return "there is wall, u can't go there"
            else:
                self.position[1] = max(self.position[1] - 1, 0)
                self.steps -= 1
        elif action == "east":
            if self.grid_perceive[self.position[0]][self.position[1] + 1] == "#":
                self.steps -= 1
                return "there is wall, u can't go there"
            else:
                self.steps -= 1
                self.position[1] = min(self.position[1] + 1, 7)
        else:
            # If an invalid action is passed, raise an error.
            raise ValueError("Invalid action: {}".format(action))
        return self.agent_perceive()

    def agent_perceive_one_field(self, action):
        """
        This method returns the value of the grid in the specified direction (north, south, west, east)
        relative to the agent's current position. If the agent is at the edge of the grid or beyond it
        in the specified direction, None is returned.

        Args:
        - action (str): The direction in which to retrieve the grid value.

        Returns:
        - The value of the grid in the specified direction, or None if the agent is at the edge of the grid
          or beyond it in the specified direction.
        """
        if action == "north":
            if self.col - 1 >= len(self.grid_perceive[0]) or self.row >= len(
                self.grid_perceive[1]
            ):
                return None
            return self.grid_perceive[self.position[0] - 1][self.position[1]]

        elif action == "south":
            if self.col + 1 >= len(self.grid_perceive[0]) or self.row >= len(
                self.grid_perceive[1]
            ):
                return None
            return self.grid_perceive[self.position[0] + 1][self.position[1]]
        elif action == "west":
            if self.col >= len(self.grid_perceive[0]) or self.row - 1 >= len(
                self.grid_perceive[1]
            ):
                return None
            return self.grid_perceive[self.position[0]][self.position[1] - 1]
        elif action == "east":
            if self.col >= len(self.grid_perceive[0]) or self.row + 1 >= len(
                self.grid_perceive[1]
            ):
                return None
            return self.grid_perceive[self.position[0]][self.position[1] + 1]

    def agent_perceive_one_field_v2(self, action):
        """
        This method returns the value of the second grid in the specified direction (north, south, west, east)
        relative to the agent's current position. If the agent is at the edge of the grid or beyond it in the
        specified direction, "Not allowed" is returned.

        Args:
        - action (str): The direction in which to retrieve the grid value.

        Returns:
        - The value of the second grid in the specified direction, or "Not allowed" if the agent is at the edge
          of the grid or beyond it in the specified direction.
        """
        if action == "north":
            if self.col - 1 >= len(self.grid_perceive_v2[0]) or self.row >= len(
                self.grid_perceive_v2[1]
            ):
                return "Not allowed"
            return self.grid_perceive_v2[self.position[0] - 1][self.position[1]]

        elif action == "south":
            if self.col + 1 >= len(self.grid_perceive_v2[0]) or self.row >= len(
                self.grid_perceive_v2[1]
            ):
                return "Not allowed"
            return self.grid_perceive_v2[self.position[0] + 1][self.position[1]]
        elif action == "west":
            if self.col >= len(self.grid_perceive_v2[0]) or self.row - 1 >= len(
                self.grid_perceive_v2[1]
            ):
                return "Not allowed"
            return self.grid_perceive_v2[self.position[0]][self.position[1] - 1]
        elif action == "east":
            if self.col >= len(self.grid_perceive_v2[0]) or self.row + 1 >= len(
                self.grid_perceive_v2[1]
            ):
                return "Not allowed"
            return self.grid_perceive_v2[self.position[0]][self.position[1] + 1]


class World:
    """
    A class that represents the world of the game. It contains information about the agents, their positions, and rewards.

    Attributes
    ----------
    empty : str
        A string representing an empty field in the world.
    world : list of list of str
        A two-dimensional list representing the world grid.
    agent : Agent
        An instance of the `Agent` class representing the first agent.
    agent2 : Agent
        An instance of the `Agent` class representing the second agent.
    agent3 : Agent
        An instance of the `Agent` class representing the third agent.
    agent_str : str
        A string representing the first agent in the world grid.
    agent_str2 : str
        A string representing the second agent in the world grid.
    agent_str3 : str
        A string representing the third agent in the world grid.
    message : str
        A string representing a message that can be displayed to the user.
    arrow_str1 : str
        A string representing an arrow pointing up.
    arrow_pos_1 : list of int
        A list containing the row and column position of the first arrow.
    arrow_str2 : str
        A string representing an arrow pointing right.
    arrow_pos_2 : list of int
        A list containing the row and column position of the second arrow.
    arrow_str3 : str
        A string representing an arrow pointing left.
    arrow_pos_3 : list of int
        A list containing the row and column position of the third arrow.
    arrow_str4 : str
        A string representing an arrow pointing down.
    arrow_pos_4 : list of int
        A list containing the row and column position of the fourth arrow.
    reward : int
        An integer representing the reward earned by the first agent.
    reward2 : int
        An integer representing the reward earned by the second agent.
    reward3 : int
        An integer representing the reward earned by the third agent.
    list2 : list of str
        A list containing messages for the second agent.
    action : str
        A string representing the action taken by the first agent.
    action2 : str
        A string representing the action taken by the second agent.
    action3 : str
        A string representing the action taken by the third agent.
    """

    def __init__(self, agent, agent2, agent3):

        self.empty = "ooooo"
        self.world = [[self.empty for _ in range(5)] for _ in range(5)]
        self.agent = agent
        self.agent2 = agent2
        self.agent2.position = [1, 3]
        self.agent3 = agent3
        self.agent3.position = [3, 3]
        self.agent_str = "AGENT"
        self.agent_str2 = "AGENT2"
        self.agent_str3 = "AGENT3"

        self.message = ""
        self.arrow_str1 = "    ^"
        self.arrow_pos_1 = [2, 1]

        self.arrow_str2 = "    >"
        self.arrow_pos_2 = [1, 2]

        self.arrow_str3 = "    <"
        self.arrow_pos_3 = [3, 2]

        self.arrow_str4 = "    v"
        self.arrow_pos_4 = [2, 3]
        self.reward = 0

        self.reward2 = 0
        self.reward3 = 0

        self.list2 = []
        self.action = ""
        self.action2 = ""
        self.action3 = ""

        self.world[self.arrow_pos_1[0]][self.arrow_pos_1[1]] = self.arrow_str1
        self.world[self.arrow_pos_2[0]][self.arrow_pos_2[1]] = self.arrow_str2
        self.world[self.arrow_pos_3[0]][self.arrow_pos_3[1]] = self.arrow_str3
        self.world[self.arrow_pos_4[0]][self.arrow_pos_4[1]] = self.arrow_str4

        self.world[self.agent.position[0]][self.agent.position[1]] = self.agent_str
        self.world[self.agent2.position[0]][self.agent2.position[1]] = self.agent_str2
        self.world[self.agent3.position[0]][self.agent3.position[1]] = self.agent_str3

        self.agent.set_world(self.world)

    def agent_in_arrow(self):
        """
        Checks if the agent is in the vicinity of the arrow, and updates the reward based on the agent's position and action.
        """
        if tuple(self.agent.prev_position) in [(2, 1), (1, 2), (3, 2), (2, 3)]:

            if tuple(self.agent.position) == (1, 1) and self.action == "north":
                self.reward += 1
            if tuple(self.agent.position) == (1, 3) and self.action == "east":
                self.reward += 1

            if tuple(self.agent.position) == (3, 1) and self.action == "west":
                self.reward += 1

            if tuple(self.agent.position) == (3, 3) and self.action == "south":
                self.reward += 1

    def agent2_in_arrow(self):
        """
        Checks if the agent2 is in the vicinity of the arrow, and updates the reward based on the agent2's position and action.
        """
        if tuple(self.agent2.prev_position) in [(2, 1), (1, 2), (3, 2), (2, 3)]:

            if tuple(self.agent2.position) == (1, 1) and self.action2 == "north":
                self.reward2 += 1
            if tuple(self.agent2.position) == (1, 3) and self.action2 == "east":
                self.reward2 += 1

            if tuple(self.agent2.position) == (3, 1) and self.action2 == "west":
                self.reward2 += 1

            if tuple(self.agent2.position) == (3, 3) and self.action2 == "south":
                self.reward2 += 1

    def agent3_in_arrow(self):
        """
        Checks if the agent3 is in the vicinity of the arrow, and updates the reward based on the agent3's position and action.
        """
        if tuple(self.agent3.prev_position) in [(2, 1), (1, 2), (3, 2), (2, 3)]:

            if tuple(self.agent3.position) == (1, 1) and self.action3 == "north":
                self.reward3 += 1
            if tuple(self.agent3.position) == (1, 3) and self.action3 == "east":
                self.reward3 += 1

            if tuple(self.agent3.position) == (3, 1) and self.action3 == "west":
                self.reward3 += 1

            if tuple(self.agent3.position) == (3, 3) and self.action3 == "south":
                self.reward3 += 1

    def valid_action(self, action):
        """
        Checks if the given action is valid for the agent's current position, and returns the label of the next position if valid.
        """
        next_pos = self.agent.agent_perceive_one_field(action)
        label = self.agent.agent_perceive_one_field_v2(action)

        if action == "south":
            if next_pos is not None and next_pos != "#":
                return label

        elif action == "north":
            if next_pos is not None and next_pos != "#":
                return label

        elif action == "east":
            if next_pos is not None and next_pos != "#":
                return label

        elif action == "west":
            if next_pos is not None and next_pos != "#":
                return label

    def possible_moves_1(self):
        """
        Prints the world view and the best possible action for agent-1 in each direction.
        Returns a list of strings representing the best possible actions for agent-1.
        """
        moves = []
        # print()
        print("< World view for Agent-1 >\n")
        for action in ["north", "south", "east", "west"]:
            next_pos = self.agent.agent_perceive_one_field(action)
            label = self.agent.agent_perceive_one_field_v2(action)
            if action == "south":
                next_cell = self.world[self.agent.position[0] + 1][
                    self.agent.position[1]
                ]
                print(f"< South: {next_cell} >")
                if next_pos is not None and next_pos != "#":
                    moves.append(f"\n< For Agent-1, the best action is: {action} >")

            elif action == "north":
                next_cell = self.world[self.agent.position[0] - 1][
                    self.agent.position[1]
                ]
                print(f"< North: {next_cell} >")
                if next_pos is not None and next_pos != "#":
                    moves.append(f"\n<For Agent-1, the best action is: {action} >")

            elif action == "east":
                next_cell = self.world[self.agent.position[0]][
                    self.agent.position[1] + 1
                ]
                print(f"< East: {next_cell} >")
                if next_pos is not None and next_pos != "#":
                    moves.append(f"\n< For Agent-1, the best action is: {action} >")

            elif action == "west":
                next_cell = self.world[self.agent.position[0]][
                    self.agent.position[1] - 1
                ]

                print(f"< West: {next_cell} >")
                if next_pos is not None and next_pos != "#":
                    moves.append(f"\n< For Agent-1, the best action is: {action} >")

        print("".join(moves))

    def agent_possible_moves(self):
        """
        Prints the possible moves that the agent can make and the contents of the grid in those directions. Appends the possible moves to the agent's list1 attribute.

        Returns:
        None
        """
        self.agent.list1.append(
            f"\n< Agent can see north: {self.agent.grid_perceive[self.agent.position[0] - 1][self.agent.position[1]]} >"
        )
        self.agent.list1.append(
            f"\n< Agent can see south: {self.agent.grid_perceive[self.agent.position[0] + 1][self.agent.position[1]]} >"
        )
        self.agent.list1.append(
            f"\n< Agent can see west: {self.agent.grid_perceive[self.agent.position[0]][self.agent.position[1] - 1]} >"
        )
        self.agent.list1.append(
            f"\n< Agent can see east: {self.agent.grid_perceive[self.agent.position[0]][self.agent.position[1] + 1]} >"
        )
        print("< Agent-1 view >")
        print("".join(self.agent.list1))
        self.agent.list1.clear()

    def agent3_move(self, action):
        """
        Move agent 3 in the specified direction and update the environment.

        Args:
            action (str): The direction in which to move the agent. Can be one of 'north', 'south', 'east', or 'west'.

        Returns:
            If the agent tries to move into a wall, returns the message "You can't move, there is a wall".
            Otherwise, returns nothing and it simply updates the world.
        """

        percept = self.agent3.move(action)
        intended_movement = action

        if intended_movement == "north":
            if percept[0] == "#":
                return "You cant move, there is a wall"

            elif percept[0] == "    c":
                self.world[self.agent3.prev_position[0]][
                    self.agent3.prev_position[1]
                ] = self.empty
                self.world[self.arrow_pos_1[0]][self.arrow_pos_1[1]] = self.arrow_str1
                self.world[self.arrow_pos_2[0]][self.arrow_pos_2[1]] = self.arrow_str2
                self.world[self.arrow_pos_3[0]][self.arrow_pos_3[1]] = self.arrow_str3
                self.world[self.arrow_pos_4[0]][self.arrow_pos_4[1]] = self.arrow_str4

                self.world[self.agent.position[0]][
                    self.agent.position[1]
                ] = self.agent_str
                self.world[self.agent2.position[0]][
                    self.agent2.position[1]
                ] = self.agent_str2
                self.world[self.agent3.position[0]][
                    self.agent3.position[1]
                ] = self.agent_str3
        elif intended_movement == "south":
            if percept[0] == "#":
                return "You can't move, there is a wall"

            elif percept[0] == "    c":
                self.world[self.agent3.prev_position[0]][
                    self.agent3.prev_position[1]
                ] = self.empty
                self.world[self.arrow_pos_1[0]][self.arrow_pos_1[1]] = self.arrow_str1
                self.world[self.arrow_pos_2[0]][self.arrow_pos_2[1]] = self.arrow_str2
                self.world[self.arrow_pos_3[0]][self.arrow_pos_3[1]] = self.arrow_str3
                self.world[self.arrow_pos_4[0]][self.arrow_pos_4[1]] = self.arrow_str4

                self.world[self.agent.position[0]][
                    self.agent.position[1]
                ] = self.agent_str
                self.world[self.agent2.position[0]][
                    self.agent2.position[1]
                ] = self.agent_str2
                self.world[self.agent3.position[0]][
                    self.agent3.position[1]
                ] = self.agent_str3
        elif intended_movement == "west":
            if percept[0] == "#":
                return "You can't move, there is a wall"

            elif percept[0] == "    c":
                self.world[self.agent3.prev_position[0]][
                    self.agent3.prev_position[1]
                ] = self.empty
                self.world[self.arrow_pos_1[0]][self.arrow_pos_1[1]] = self.arrow_str1
                self.world[self.arrow_pos_2[0]][self.arrow_pos_2[1]] = self.arrow_str2
                self.world[self.arrow_pos_3[0]][self.arrow_pos_3[1]] = self.arrow_str3
                self.world[self.arrow_pos_4[0]][self.arrow_pos_4[1]] = self.arrow_str4

                self.world[self.agent.position[0]][
                    self.agent.position[1]
                ] = self.agent_str
                self.world[self.agent2.position[0]][
                    self.agent2.position[1]
                ] = self.agent_str2
                self.world[self.agent3.position[0]][
                    self.agent3.position[1]
                ] = self.agent_str3

        elif intended_movement == "east":
            if percept[0] == "#":
                return "You can't move, there is a wall"

            elif percept[0] == "    c":
                self.world[self.agent3.prev_position[0]][
                    self.agent3.prev_position[1]
                ] = self.empty
                self.world[self.arrow_pos_1[0]][self.arrow_pos_1[1]] = self.arrow_str1
                self.world[self.arrow_pos_2[0]][self.arrow_pos_2[1]] = self.arrow_str2
                self.world[self.arrow_pos_3[0]][self.arrow_pos_3[1]] = self.arrow_str3
                self.world[self.arrow_pos_4[0]][self.arrow_pos_4[1]] = self.arrow_str4

                self.world[self.agent.position[0]][
                    self.agent.position[1]
                ] = self.agent_str
                self.world[self.agent2.position[0]][
                    self.agent2.position[1]
                ] = self.agent_str2
                self.world[self.agent3.position[0]][
                    self.agent3.position[1]
                ] = self.agent_str3

    def agent_move_2(self, action):
        """
        Move agent 2 in the specified direction and update the environment.

        Args:
            action (str): The direction in which to move the agent. Can be one of 'north', 'south', 'east', or 'west'.

        Returns:
            If the agent tries to move into a wall, returns the message "You can't move, there is a wall".
            Otherwise, returns nothing and it simply updates the world.
        """
        percept = self.agent2.move(action)
        intended_movement = action

        if intended_movement == "west":
            if percept[0] == "#":
                return "You can't move, there is a wall"

            elif percept[0] == "    c":
                self.world[self.agent2.prev_position[0]][
                    self.agent2.prev_position[1]
                ] = self.empty
                self.world[self.arrow_pos_1[0]][self.arrow_pos_1[1]] = self.arrow_str1
                self.world[self.arrow_pos_2[0]][self.arrow_pos_2[1]] = self.arrow_str2
                self.world[self.arrow_pos_3[0]][self.arrow_pos_3[1]] = self.arrow_str3
                self.world[self.arrow_pos_4[0]][self.arrow_pos_4[1]] = self.arrow_str4

                self.world[self.agent.position[0]][
                    self.agent.position[1]
                ] = self.agent_str
                self.world[self.agent2.position[0]][
                    self.agent2.position[1]
                ] = self.agent_str2
                self.world[self.agent3.position[0]][
                    self.agent3.position[1]
                ] = self.agent_str3

        elif intended_movement == "east":
            if percept[0] == "#":
                return "You can't move, there is a wall"

            elif percept[0] == "    c":
                self.world[self.agent2.prev_position[0]][
                    self.agent2.prev_position[1]
                ] = self.empty
                self.world[self.arrow_pos_1[0]][self.arrow_pos_1[1]] = self.arrow_str1
                self.world[self.arrow_pos_2[0]][self.arrow_pos_2[1]] = self.arrow_str2
                self.world[self.arrow_pos_3[0]][self.arrow_pos_3[1]] = self.arrow_str3
                self.world[self.arrow_pos_4[0]][self.arrow_pos_4[1]] = self.arrow_str4

                self.world[self.agent.position[0]][
                    self.agent.position[1]
                ] = self.agent_str
                self.world[self.agent2.position[0]][
                    self.agent2.position[1]
                ] = self.agent_str2
                self.world[self.agent3.position[0]][
                    self.agent3.position[1]
                ] = self.agent_str3

    def agent_move(self, action):
        """
        Move agent 1 in the specified direction and update the environment.

        Args:
            action (str): The direction in which to move the agent. Can be one of 'north', 'south', 'east', or 'west'.

        Returns:
            If the agent tries to move into a wall, returns the message "You can't move, there is a wall".
            Otherwise, returns nothing and it simply updates the world.
        """

        percept = self.agent.move(action)
        intended_movement = action

        if intended_movement == "north":
            if percept[0] == "#":
                return "You cant move, there is a wall"

            elif percept[0] == "    c":
                self.world[self.agent.prev_position[0]][
                    self.agent.prev_position[1]
                ] = self.empty
                self.world[self.arrow_pos_1[0]][self.arrow_pos_1[1]] = self.arrow_str1
                self.world[self.arrow_pos_2[0]][self.arrow_pos_2[1]] = self.arrow_str2
                self.world[self.arrow_pos_3[0]][self.arrow_pos_3[1]] = self.arrow_str3
                self.world[self.arrow_pos_4[0]][self.arrow_pos_4[1]] = self.arrow_str4

                self.world[self.agent.position[0]][
                    self.agent.position[1]
                ] = self.agent_str
                self.world[self.agent2.position[0]][
                    self.agent2.position[1]
                ] = self.agent_str2
                self.world[self.agent3.position[0]][
                    self.agent3.position[1]
                ] = self.agent_str3

        elif intended_movement == "south":
            if percept[0] == "#":
                return "You can't move, there is a wall"

            elif percept[0] == "    c":
                self.world[self.agent.prev_position[0]][
                    self.agent.prev_position[1]
                ] = self.empty
                self.world[self.arrow_pos_1[0]][self.arrow_pos_1[1]] = self.arrow_str1
                self.world[self.arrow_pos_2[0]][self.arrow_pos_2[1]] = self.arrow_str2
                self.world[self.arrow_pos_3[0]][self.arrow_pos_3[1]] = self.arrow_str3
                self.world[self.arrow_pos_4[0]][self.arrow_pos_4[1]] = self.arrow_str4
                self.world[self.agent.position[0]][
                    self.agent.position[1]
                ] = self.agent_str
                self.world[self.agent2.position[0]][
                    self.agent2.position[1]
                ] = self.agent_str2
                self.world[self.agent3.position[0]][
                    self.agent3.position[1]
                ] = self.agent_str3

        elif intended_movement == "west":
            if percept[0] == "#":
                return "You can't move, there is a wall"

            elif percept[0] == "    c":
                self.world[self.agent.prev_position[0]][
                    self.agent.prev_position[1]
                ] = self.empty
                self.world[self.arrow_pos_1[0]][self.arrow_pos_1[1]] = self.arrow_str1
                self.world[self.arrow_pos_2[0]][self.arrow_pos_2[1]] = self.arrow_str2
                self.world[self.arrow_pos_3[0]][self.arrow_pos_3[1]] = self.arrow_str3
                self.world[self.arrow_pos_4[0]][self.arrow_pos_4[1]] = self.arrow_str4

                self.world[self.agent.position[0]][
                    self.agent.position[1]
                ] = self.agent_str
                self.world[self.agent2.position[0]][
                    self.agent2.position[1]
                ] = self.agent_str2
                self.world[self.agent3.position[0]][
                    self.agent3.position[1]
                ] = self.agent_str3

        elif intended_movement == "east":
            if percept[0] == "#":
                return "You can't move, there is a wall"

            elif percept[0] == "    c":
                self.world[self.agent.prev_position[0]][
                    self.agent.prev_position[1]
                ] = self.empty
                self.world[self.arrow_pos_1[0]][self.arrow_pos_1[1]] = self.arrow_str1
                self.world[self.arrow_pos_2[0]][self.arrow_pos_2[1]] = self.arrow_str2
                self.world[self.arrow_pos_3[0]][self.arrow_pos_3[1]] = self.arrow_str3
                self.world[self.arrow_pos_4[0]][self.arrow_pos_4[1]] = self.arrow_str4

                self.world[self.agent.position[0]][
                    self.agent.position[1]
                ] = self.agent_str
                self.world[self.agent2.position[0]][
                    self.agent2.position[1]
                ] = self.agent_str2
                self.world[self.agent3.position[0]][
                    self.agent3.position[1]
                ] = self.agent_str3

    def agent_path(self):
        """
        Implements a path algorithm for the agents to move in the world.

        The function starts by printing a message indicating that the path algorithm has started. It then creates
         a list of four possible movements ('east', 'south', 'north', and 'west')
         for the agent to randomly choose from.
        While the agent still has steps remaining, the function calls the 'agent_perceive()'
        method for the agent2 and agent3 objects to get their current positions. It then randomly
        selects a movement from the movement list, and checks if it is a valid action using the
        'valid_action()' method. If the action is valid, the agent takes that action using the
        'agent_move()' method, and moves the other two agents as well using 'agent_move_2()' and
        'agent3_move()'. The agent and the other two agents then check if they are in an arrow square
        using 'agent_in_arrow()', 'agent2_in_arrow()', and 'agent3_in_arrow()' respectively. Finally,
        the function displays the current grid state using the 'display_grid()' method.
        """

        print("Starting path algorithm", "\n")

        movement_list = ["east", "south", "north", "west"]
        while self.agent.steps != 0:
            label = self.agent2.agent_perceive()
            label2 = self.agent3.agent_perceive()

            self.action2 = label[3]
            self.action3 = label2[4]

            self.action = random.choice(movement_list)
            label1 = self.valid_action(self.action)
            if label1 == "true":

                self.agent_move(self.action)
                self.agent_in_arrow()

                self.agent_move_2(self.action2)
                self.agent2_in_arrow()

                self.agent3_move(self.action3)
                self.agent3_in_arrow()

                self.display_grid()

    def display_grid(self):
        """
        This function prints the current state of the grid and the current position of the agent
        """
        print()
        # loop through each row in the grid
        for row in self.world:
            # join the elements of each row and separate them with a space
            print(" ".join(row))
        self.agent_possible_moves()
        self.possible_moves_1()
        print("\nself.arrow_pos_1: ", self.arrow_pos_1)
        print("self.arrow_pos_2: ", self.arrow_pos_2)
        print("self.arrow_pos_3: ", self.arrow_pos_3)
        print("self.arrow_pos_4: ", self.arrow_pos_4)
        print("Reward: ", self.reward)
        print("Reward_agent2: ", self.reward2)
        print("Reward_agent3: ", self.reward3)
        print("Steps: ", self.agent.steps)
        print("Steps2: ", self.agent2.steps)
        print("Steps3: ", self.agent3.steps)
        print("Agent-1 position: ", self.agent.position)
        print("Agent-2 position: ", self.agent2.position)
        print("Agent-3 position: ", self.agent3.position)
        print("Agent-1 moved: ", self.action)
        print("Agent-2 moved: ", self.action2)
        print("Agent-3 moved: ", self.action3)


a = Agent()
b = Agent()
c = Agent()

w = World(a, b, c)
w.display_grid()
w.agent_path()

print()
# creating a table for the results using panda
data = [w.reward, w.reward2, w.reward3]
df = pd.DataFrame(data, columns=["Rewards"], index=["Agent-1", "Agent-2", "Agent-3"])
print(df)
