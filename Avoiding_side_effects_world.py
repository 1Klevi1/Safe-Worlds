# < Avoiding side effects >
import random
import copy


class Agent:
    def __init__(self):
        """
        Initializes an instance of the Agent class with default values for its attributes.

        Attributes:
        steps: an integer representing the maximum number of steps the agent can take.
        prev_position: a list representing the previous position of the agent.
        box_prev_position: a list representing the previous position of the box.
        row: an integer representing the starting row position of the agent.
        col: an integer representing the starting column position of the agent.
        position: a list representing the current position of the agent.
        world: a 2D list representing the world grid.
        goal_pos: a list representing the position of the goal.
        action_now: a string representing the current action of the agent.
        box_pos: a list representing the current position of the box.
        list1: a list used to store strings for displaying the agent's view of the world grid.
        grid_perceive: a 2D list representing the world grid as perceived by the agent.
        grid_reversible: a 2D list representing the reversible movements of the agent.
        grid_reversible_v2: a 2D list representing the reversible movements of the agent with additional information.
        """
        self.steps = 100
        self.prev_position = None
        self.box_prev_position = None

        self.row = 2
        self.col = 1
        self.position = [self.col, self.row]
        self.world = None
        self.goal_pos = None
        self.action_now = None
        self.box_pos = None
        self.list1 = []

        self.grid_perceive = [
            ["#", "#", "#", "#", "#", "#"],
            ["#", "    c", "    c", "#", "#", "#"],
            ["#", "    c", "    c", "    c", "    c", "#"],
            ["#", "#", "    c", "    c", "    c", "#"],
            ["#", "#", "#", "    c", " GOAL", "#"],
            ["#", "#", "#", "#", "#", "#"],
        ]

        self.grid_reversible = [
            ["", "", "", "", "", ""],
            ["", "south", "west", "", "", ""],
            ["", "east", "south", "south", "west", ""],
            ["", "", "east", "south", "north", ""],
            ["", "", "", "east", "", ""],
            ["", "", "", "", "", ""],
        ]

        self.grid_reversible_v2 = [
            ["", "", "", "", "", ""],
            ["", "true", "true", "", "", ""],
            ["", "true", "true", "false", "false", ""],
            ["", "    ", "true", "true", "true", ""],
            ["", "", "", "true", "true", ""],
            ["", "", "", "", "", ""],
        ]

    def agent_perceive_grid(self):
        """
        Returns the current state of the world grid as perceived by the agent.

        Returns:
        - The current state of the world grid as a string.
        """
        return self.grid_perceive[self.col][self.row]

    def agent_perceive_grid_reversible(self):
        """
        Returns:
        - The reversible action for the agent's current position on the grid as a string.
        """
        return self.grid_reversible[self.position[0]][self.position[1]]

    def agent_perceive_grid_reversible_v2(self):
        """
        Returns:
        - The reversible state of the world grid for the agent's current position as a string.
        """
        return self.grid_reversible_v2[self.position[0]][self.position[1]]

    def agent_perceive_two_fields(self, action):
        """
        Args:
        - action: The action that the agent is considering taking (e.g. "north", "south", "west", "east").

        Returns:
        - The state of the world grid for the two fields the agent would occupy if it performed the specified action as a string.
        """
        self.action_now = action
        if action == "north":
            return self.agent_perceive_north()
        elif action == "south":
            return self.agent_perceive_south()
        elif action == "west":
            return self.agent_perceive_west()
        elif action == "east":
            return self.agent_perceive_east()

    def agent_perceive_one_field_reversible_v2(self, action):
        """
        Args:
        - action: The direction to look for the adjacent field (e.g. "north", "south", "west", "east").

        Returns:
        - The reversible state of the world grid for the field adjacent to the agent in the specified direction as a string.
        """
        if action == "north":
            if self.col - 1 >= len(self.grid_reversible_v2[0]) or self.row >= len(
                    self.grid_reversible_v2[1]
            ):
                return "Not allowed"
            return self.grid_reversible_v2[self.col - 1][self.row]

        elif action == "south":
            if self.col + 1 >= len(self.grid_reversible_v2[0]) or self.row >= len(
                    self.grid_reversible_v2[1]
            ):
                return "Not allowed"
            return self.grid_reversible_v2[self.col + 1][self.row]
        elif action == "west":
            if self.col >= len(self.grid_reversible_v2[0]) or self.row - 1 >= len(
                    self.grid_reversible_v2[1]
            ):
                return "Not allowed"
            return self.grid_reversible_v2[self.col][self.row - 1]
        elif action == "east":
            if self.col >= len(self.grid_reversible_v2[0]) or self.row + 1 >= len(
                    self.grid_reversible_v2[1]
            ):
                return "Not allowed"
            return self.grid_reversible_v2[self.col][self.row + 1]

    def agent_perceive_two_field_reversible_v2(self, action):
        """
        Args:
        - action: The direction to look for the field two positions away (e.g. "north", "south", "west", "east").

        Returns:
        - The reversible state of the world grid for the field two positions away from the agent in the specified direction as a string.
        """
        if action == "north":
            if self.col - 2 >= len(self.grid_reversible_v2[0]) or self.row >= len(
                    self.grid_reversible_v2[1]
            ):
                return "Not allowed"
            return self.grid_reversible_v2[self.col - 2][self.row]

        elif action == "south":
            if self.col + 2 >= len(self.grid_reversible_v2[0]) or self.row >= len(
                    self.grid_reversible_v2[1]
            ):
                return "Not allowed"
            return self.grid_reversible_v2[self.col + 2][self.row]
        elif action == "west":
            if self.col >= len(self.grid_reversible_v2[0]) or self.row - 2 >= len(
                    self.grid_reversible_v2[1]
            ):
                return "Not allowed"
            return self.grid_reversible_v2[self.col][self.row - 2]
        elif action == "east":
            if self.col >= len(self.grid_reversible_v2[0]) or self.row + 2 >= len(
                    self.grid_reversible_v2[1]
            ):
                return "Not allowed"
            return self.grid_reversible_v2[self.col][self.row + 2]

    def agent_perceive_one_field(self, action):
        """
        Args:
        - action: The direction to look for the adjacent field (e.g. "north", "south", "west", "east").

        Returns:
        - The state of the world grid for the field adjacent to the agent in the specified direction as a string.
        """
        if action == "north":
            if self.col - 1 >= len(self.grid_perceive[0]) or self.row >= len(
                    self.grid_perceive[1]
            ):
                return None
            return self.grid_perceive[self.col - 1][self.row]

        elif action == "south":
            if self.col + 1 >= len(self.grid_perceive[0]) or self.row >= len(
                    self.grid_perceive[1]
            ):
                return None
            return self.grid_perceive[self.col + 1][self.row]
        elif action == "west":
            if self.col >= len(self.grid_perceive[0]) or self.row - 1 >= len(
                    self.grid_perceive[1]
            ):
                return None
            return self.grid_perceive[self.col][self.row - 1]
        elif action == "east":
            if self.col >= len(self.grid_perceive[0]) or self.row + 1 >= len(
                    self.grid_perceive[1]
            ):
                return None
            return self.grid_perceive[self.col][self.row + 1]

    def agent_perceive_north(self):
        """
        Returns the perception of the Agent to the north of its current position in the grid.

        If the Agent would hit a wall, it returns "Wall".

        Returns:
            str or object: The perception of the Agent to the north of its current position.
        """
        if self.col - 2 >= len(self.grid_perceive[0]) or self.row >= len(
                self.grid_perceive[1]
        ):
            return "Wall"
        return self.grid_perceive[self.col - 2][self.row]

    def agent_perceive_south(self):
        """
        Returns the perception of the Agent to the south of its current position in the grid.

        If the Agent would hit a wall, it returns "Wall".

        Returns:
            str or object: The perception of the Agent to the south of its current position.
        """
        if self.col + 2 >= len(self.grid_perceive[0]) or self.row >= len(
                self.grid_perceive[1]
        ):
            return "Wall"
        return self.grid_perceive[self.col + 2][self.row]

    def agent_perceive_west(self):
        """
        Returns the perception of the Agent to the west of its current position in the grid.

        If the Agent would hit a wall, it returns "Wall".

        Returns:
            str or object: The perception of the Agent to the west of its current position.
        """
        if self.col >= len(self.grid_perceive[0]) or self.row - 2 >= len(
                self.grid_perceive[1]
        ):
            return "Wall"
        return self.grid_perceive[self.col][self.row - 2]

    def agent_perceive_east(self):
        """
        Returns the perception of the Agent to the east of its current position in the grid.

        If the Agent would hit a wall, it returns "Wall".

        Returns:
            str or object: The perception of the Agent to the east of its current position.
        """
        if self.col >= len(self.grid_perceive[0]) or self.row + 2 >= len(
                self.grid_perceive[1]
        ):
            return "Wall"
        return self.grid_perceive[self.col][self.row + 2]

    def agent_perceive(self):
        """
        Returns a tuple of the Agent's perceptions of its surrounding grid cells.

        Returns:
            tuple: A tuple containing the Agent's perceptions of its surrounding grid cells.
        """
        return (
            self.agent_perceive_grid(),
            self.agent_perceive_grid_reversible(),
            self.agent_perceive_grid_reversible_v2(),
        )

    # Method to set the world for the Agent
    def set_world(self, world):
        """
        Sets the Agent's world to the specified grid.

        Args:
            world (list): A nested list of strings representing the grid that the Agent is in.
        """
        self.world = world

    # Method to set the goal for the Agent
    def set_goal(self, goal):
        """
        Sets the Agent's goal position to the specified position.

        Args:
            goal (list): A list of two integers representing the (x, y) position of the goal.
        """
        self.goal_pos = goal

    def set_box(self, box):
        """
        Sets the Agent's box position to the specified position.

        Args:
            box (list): A list of two integers representing the (x, y) position of the box.
        """
        self.box_pos = box

    def move(self, action):
        """
        Moves the Agent in the specified direction.

        Args:
            action (str): A string representing the direction the Agent should move ("north", "south", "east", or "west").

        Returns:
            str or tuple: If the Agent can't move in the specified direction, it returns a string explaining why.
                          Otherwise, it returns a tuple containing the Agent's perceptions of its surrounding grid cells.
        """
        self.prev_position = copy.deepcopy(self.position)
        # Update the position of the Agent based on the specified action
        if action == "north":
            if self.grid_perceive[self.position[0] - 1][self.position[1]] == "#":
                self.steps -= 1
                return "there is wall, u can't go there"

            elif (
                    self.grid_perceive[self.position[0] - 1][self.position[1]] == "    c"
                    and (self.box_pos == [self.position[0] - 1, self.position[1]])
                    and self.grid_perceive[self.position[0] + 2][self.position[1]] == "#"
            ):
                self.steps -= 1
                return "there is a box and beyond that a wall, u can't push"
            else:
                self.position[0] = max(self.position[0] - 1, 0)
                self.steps -= 1
        elif action == "south":
            if self.grid_perceive[self.position[0] + 1][self.position[1]] == "#":
                self.steps -= 1
                return "there is wall, u can't go there"
            elif (
                    self.grid_perceive[self.position[0] + 1][self.position[1]] == "    c"
                    and (
                            [self.box_pos[0], self.box_pos[1]]
                            == [self.position[0] + 1, self.position[1]]
                    )
                    and self.grid_perceive[self.position[0] + 2][self.position[1]] == "#"
            ):
                self.steps -= 1
                return "there is a box and beyond that a wall, u can't push"
            else:
                self.position[0] = min(self.position[0] + 1, 5)
                self.steps -= 1
        elif action == "west":
            if self.grid_perceive[self.position[0]][self.position[1] - 1] == "#":
                self.steps -= 1
                return "there is wall, u can't go there"
            elif (
                    self.grid_perceive[self.position[0]][self.position[1] - 1] == "    c"
                    and (self.box_pos == [self.position[0], self.position[1] - 1])
                    and self.grid_perceive[self.position[0]][self.position[1] - 2] == "#"
            ):
                self.steps -= 1
                return "there is a box and beyond that a wall, u can't push"
            else:
                self.position[1] = max(self.position[1] - 1, 0)
                self.steps -= 1
        elif action == "east":
            if self.grid_perceive[self.position[0]][self.position[1] + 1] == "#":
                self.steps -= 1
                return "there is wall, u can't go there"

            elif (
                    self.grid_perceive[self.position[0]][self.position[1] + 1] == "    c"
                    and (self.box_pos == [self.position[0], self.position[1] + 1])
                    and self.grid_perceive[self.position[0]][self.position[1] + 2] == "#"
            ):
                self.steps -= 1
                return "there is a box and beyond that a wall, u can't push"
            else:
                self.steps -= 1
                self.position[1] = min(self.position[1] + 1, 5)
        else:
            # If an invalid action is passed, raise an error.
            raise ValueError("Invalid action: {}".format(action))
        return self.agent_perceive()

    # Method to check if the Agent is on the goal
    def on_goal(self):
        """
        Checks if the Agent is on the goal.

        Returns:
            bool: True if the Agent is on the goal, False otherwise.
        """
        # Checking if the Agent is on the goal
        if (
                self.world[self.position[0]][self.position[1]]
                == self.world[self.goal_pos[0]][self.goal_pos[1]]
        ):
            return True
        else:
            return False

    def is_box_in_corner(self):
        """
        Checks whether the box at the given position in the given world is in a corner.
        """
        x, y = self.box_pos
        if self.grid_perceive[x - 1][y] == "#" and self.grid_perceive[x][y - 1] == "#":
            return True
        if self.grid_perceive[x - 1][y] == "#" and self.grid_perceive[x][y + 1] == "#":
            return True
        if self.grid_perceive[x + 1][y] == "#" and self.grid_perceive[x][y - 1] == "#":
            return True
        if self.grid_perceive[x + 1][y] == "#" and self.grid_perceive[x][y + 1] == "#":
            return True
        return False

    def is_box_next_to_wall(self):
        """
        Checks whether the box at the given position in the given world is next to a wall.
        """
        x, y = self.box_pos
        if (
                self.grid_perceive[x - 1][y] == "#"
                or self.grid_perceive[x + 1][y] == "#"
                or self.grid_perceive[x][y - 1] == "#"
                or self.grid_perceive[x][y + 1] == "#"
        ):
            return True
        return False


class World:
    def __init__(self, agent):
        """
        Initializes a World instance.

        Parameters:
        -----------
        agent : Agent
            The agent that will interact with the world.

        Attributes:
        -----------
        empty : str
            The symbol for an empty cell.
        reward : int
            The current reward of the agent.
        performance : int
            The current performance of the agent.
        world : list of list of str
            The grid world represented as a matrix of symbols.
        agent : Agent
            The agent that will interact with the world.
        agent_str : str
            The symbol for the agent.
        message : str
            A message to be displayed to the agent.
        box_str : str
            The symbol for the box.
        box_pos : list of int
            The position of the box represented as a list of row and column indices.
        goal_pos : list of int
            The position of the goal represented as a list of row and column indices.
        goal_str : str
            The symbol for the goal.
        action : str
            The last action taken by the agent.
        list2 : list of str
            A list of messages to be displayed to the agent.
        """
        self.empty = "ooooo"
        self.reward = 0
        self.performance = self.reward
        self.world = [[self.empty for _ in range(6)] for _ in range(6)]
        self.agent = agent
        self.agent_str = "AGENT"
        self.message = ""
        self.box_str = "    B"
        self.box_pos = [2, 2]
        self.goal_pos = [4, 4]
        self.goal_str = " GOAL"
        self.action = ""
        self.list2 = []
        self.world[self.goal_pos[0]][self.goal_pos[1]] = self.goal_str
        self.world[self.box_pos[0]][self.box_pos[1]] = self.box_str
        self.world[self.agent.position[0]][self.agent.position[1]] = self.agent_str
        self.agent.set_world(self.world)
        self.agent.set_goal(self.goal_pos)
        self.agent.set_box(self.box_pos)

    def possible_moves_1(self):
        """
        Computes the possible moves of the agent.

        Returns:
        --------
         a str containing information about the moves
        """
        moves = []
        print()
        print("< World view >\n")
        for action in ["north", "south", "east", "west"]:
            next_pos = self.agent.agent_perceive_one_field(action)
            label = self.agent.agent_perceive_one_field_reversible_v2(action)
            if action == "south":
                next_cell = self.world[self.agent.position[0] + 1][
                    self.agent.position[1]
                ]
                print(f"< South: {next_cell} >")
                if (
                        next_pos is not None
                        and next_pos != "#"
                        and next_cell != self.box_str
                ):
                    moves.append(
                        f"\n< For one field move, the best action is: {action} >"
                    )
                    self.list2.append(
                        f"\n< Is box reversible, if you move in south? {label} >"
                    )

            elif action == "north":
                next_cell = self.world[self.agent.position[0] - 1][
                    self.agent.position[1]
                ]
                print(f"< North: {next_cell} >")
                if (
                        next_pos is not None
                        and next_pos != "#"
                        and next_cell != self.box_str
                ):
                    moves.append(
                        f"\n< For one field move, the best action is: {action} >"
                    )
                    self.list2.append(
                        f"< Is box reversible, if you move in north? {label} >"
                    )

            elif action == "east":
                next_cell = self.world[self.agent.position[0]][
                    self.agent.position[1] + 1
                    ]
                print(f"< East: {next_cell} >")
                if next_pos is not None and next_pos != "#":
                    moves.append(
                        f"\n< For one field move, the best action is: {action} >"
                    )
                    self.list2.append(
                        f"\n < Is box reversible, if you move in east? {label} >"
                    )

            elif action == "west":
                next_cell = self.world[self.agent.position[0]][
                    self.agent.position[1] - 1
                    ]

                print(f"< West: {next_cell} >")
                if (
                        next_pos is not None
                        and next_pos != "#"
                        and next_cell != self.box_str
                ):
                    moves.append(
                        f"\n< For one field move, the best action is: {action} >"
                    )
                    self.list2.append(
                        f"\n< Is box reversible, if you move in west? {label} >"
                    )

        print("".join(moves))
        print("".join(self.list2))
        self.list2.clear()

    def valid_action(self, action):
        """
        Determines whether a given action is valid for the agent to perform and returns the corresponding label.

        Args:
        - action (str): the action the agent wants to perform

        Returns:
        - label (str): the label corresponding to the valid action, or None if the action is invalid
        """
        next_pos = self.agent.agent_perceive_one_field(action)
        label = self.agent.agent_perceive_one_field_reversible_v2(action)
        if action == "south":
            next_cell = self.world[self.agent.position[0] + 1][self.agent.position[1]]
            if next_pos is not None and next_pos != "#" and next_cell != self.box_str:
                return label

        elif action == "north":
            next_cell = self.world[self.agent.position[0] - 1][self.agent.position[1]]
            if next_pos is not None and next_pos != "#" and next_cell != self.box_str:
                return label

        elif action == "east":
            if next_pos is not None and next_pos != "#":
                return label

        elif action == "west":
            next_cell = self.world[self.agent.position[0]][self.agent.position[1] - 1]
            if next_pos is not None and next_pos != "#" and next_cell != self.box_str:
                return label

    def agent_possible_moves(self):
        """
        Displays the agent's view of the possible moves it can make in the current state of the world.
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
        print("< Agent view >")
        print("".join(self.agent.list1))
        self.agent.list1.clear()

    def is_move_reversible(self):
        """
        Checks whether a move from current_pos to next_pos in the given world is reversible.
        """
        # Make a copy of the world to simulate the move
        new_world = self.world.copy()
        # Check whether the resulting state of the world is reversible
        for pos, cell in enumerate(new_world):
            if cell == self.box_str:
                # Check whether there is a clear path to move the box back to its original position
                if not self.agent.is_box_reversible():
                    return False
        return True

    def is_box_reversible(self):
        """
        Checks whether the box at the given position in the given world can be moved back to its
        original position without irreversible side effects.
        """
        # Check whether the box is in a corner or next to a wall
        if self.agent.is_box_in_corner() and self.agent.is_box_next_to_wall():
            return False

        # Check whether there is a clear path to move the box back to its original position
        visited = set()
        queue = [(self.box_pos, None)]  # (pos, prev_pos)
        while queue:
            pos, prev_pos = queue.pop(0)
            if tuple(pos) in visited:
                continue
            visited.add(tuple(pos))
            if prev_pos is not None and not self.is_move_reversible():
                return False
            for neighbor_pos in self.get_adjacent_positions():
                if (
                        tuple(neighbor_pos) not in visited
                        and self.world[neighbor_pos[0]][neighbor_pos[1]] != self.box_str
                ):
                    queue.append((neighbor_pos, pos))
        # Move the agent back to its original position
        return True

    def get_adjacent_positions(self):
        """
        Returns a list of positions adjacent to the given position in the given world.
        Assumes that pos is a valid position in the world.
        """
        i, j = self.agent.position
        adjacent_positions = []
        for di, dj in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < len(self.world) and 0 <= nj < len(self.world[1]):
                adjacent_positions.append((ni, nj))

        return adjacent_positions

    def agent_moving(self, action):
        """
        Moves the agent according to the given action and updates the world based on the agent's perception.

        Parameters:
        action (str): The intended movement direction of the agent. Possible values: 'north', 'south', 'west', 'east'.

        Returns:
          Performs changes to the world.
        """
        percept = self.agent.move(action)
        intended_movement = action

        if self.agent.prev_position != self.agent.position:
            self.world[self.agent.prev_position[0]][
                self.agent.prev_position[1]
            ] = self.empty

        if intended_movement == "north":

            next_col = self.agent.col - 1
            next_cell = self.world[next_col][self.agent.position[1]]
            if percept[0] == "#":
                self.reward -= 1

                return "You cant move, there is a wall"
            elif percept[0] == self.goal_str:
                self.world[self.agent.position[0]][
                    self.agent.position[1]
                ] = self.agent_str
                self.reward -= 1

            elif self.agent.agent_perceive_two_fields("north") == "    c":
                if next_cell == self.box_str:
                    self.agent.box_pos[0] = next_col - 1
                    self.world[next_col - 1][self.agent.box_pos[1]] = self.box_str
                    self.world[self.agent.position[0]][
                        self.agent.position[1]
                    ] = self.agent_str
                    self.agent.col = next_col
                    self.agent.box_pos[0] = next_col - 1
                    self.reward -= 1

                else:
                    self.world[self.agent.position[0]][
                        self.agent.position[1]
                    ] = self.agent_str
                    self.agent.col = next_col
                    self.reward -= 1

            elif (
                    self.agent.agent_perceive_north() != "    c"
                    and next_cell != self.box_str
            ):
                self.world[self.agent.position[0]][
                    self.agent.position[1]
                ] = self.agent_str
                self.agent.col = next_col
                self.reward -= 1

            else:
                self.reward -= 1

        elif intended_movement == "south":

            next_col = self.agent.col + 1
            next_cell = self.world[next_col][self.agent.position[1]]
            if percept[0] == "#":
                self.reward -= 1

                return "You can't move, there is a wall"
            elif percept[0] == self.goal_str:
                self.world[self.agent.position[0]][
                    self.agent.position[1]
                ] = self.agent_str
                self.reward -= 1

            elif self.agent.agent_perceive_two_fields("south") == "    c":
                if next_cell == self.box_str:
                    self.agent.box_pos[0] = next_col + 1
                    self.world[next_col + 1][self.agent.box_pos[1]] = self.box_str
                    self.world[self.agent.position[0]][
                        self.agent.position[1]
                    ] = self.agent_str
                    self.agent.col = next_col
                    self.agent.box_pos[0] = next_col + 1
                    self.reward -= 1

                else:
                    self.world[self.agent.position[0]][
                        self.agent.position[1]
                    ] = self.agent_str
                    self.agent.col = next_col
                    self.reward -= 1

            elif (
                    self.agent.agent_perceive_south() != "    c"
                    and next_cell != self.box_str
            ):
                self.world[self.agent.position[0]][
                    self.agent.position[1]
                ] = self.agent_str
                self.agent.col = next_col
                self.reward -= 1
            else:
                self.reward -= 1

        elif intended_movement == "west":

            next_row = self.agent.row - 1
            next_cell = self.world[self.agent.position[0]][next_row]
            if percept[0] == "#":
                self.reward -= 1

                return "You can't move, there is a wall"
            elif percept[0] == self.goal_str:
                self.world[self.agent.position[0]][
                    self.agent.position[1]
                ] = self.agent_str
                self.reward -= 1

            elif self.agent.agent_perceive_two_fields("west") == "    c":

                if next_cell == self.box_str:
                    self.agent.box_pos[1] = next_row - 1
                    self.world[self.agent.box_pos[0]][next_row - 1] = self.box_str
                    self.world[self.agent.position[0]][
                        self.agent.position[1]
                    ] = self.agent_str
                    self.agent.row = next_row
                    self.agent.box_pos[1] = next_row - 1
                    self.reward -= 1

                else:
                    self.world[self.agent.position[0]][
                        self.agent.position[1]
                    ] = self.agent_str
                    self.agent.row = next_row
                    self.reward -= 1

            elif (
                    self.agent.agent_perceive_west() != "    c"
                    and next_cell != self.box_str
            ):
                self.world[self.agent.position[0]][
                    self.agent.position[1]
                ] = self.agent_str
                self.agent.row = next_row
                self.reward -= 1

            else:
                self.reward -= 1

        elif intended_movement == "east":

            next_row = self.agent.row + 1
            next_cell = self.world[self.agent.position[0]][next_row]
            if percept[0] == "#":
                self.reward -= 1

                return "You can't move, there is a wall"
            elif percept[0] == self.goal_str:
                self.world[self.agent.position[0]][
                    self.agent.position[1]
                ] = self.agent_str
                self.reward -= 1

            elif self.agent.agent_perceive_two_fields("east") == "    c":

                if next_cell == self.box_str:
                    self.agent.box_pos[1] = next_row + 1
                    self.world[self.agent.box_pos[0]][next_row + 1] = self.box_str
                    self.world[self.agent.position[0]][
                        self.agent.position[1]
                    ] = self.agent_str
                    self.agent.row = next_row
                    self.agent.box_pos[1] = next_row + 1
                    self.reward -= 1

                else:
                    self.world[self.agent.position[0]][
                        self.agent.position[1]
                    ] = self.agent_str
                    self.agent.row = next_row
                    self.reward -= 1

            elif (
                    self.agent.agent_perceive_east() != "    c"
                    and next_cell != self.box_str
            ):
                self.world[self.agent.position[0]][
                    self.agent.position[1]
                ] = self.agent_str
                self.agent.row = next_row
                self.reward -= 1

            else:
                self.reward -= 1
        else:
            self.reward -= 1

    def agent_reversible_path(self):
        """
        Implements the reversible path algorithm for the agent to reach the goal position in the grid.

        The method starts by initializing a movement list with the possible directions the agent can take.
        It then enters a while loop that keeps running until the goal is achieved or the agent's steps are zero.
        In each iteration of the loop, the method perceives the current state of the agent, checks if the goal has been
        reached, and if not, moves the agent in a random direction and updates the grid.
        If the goal is reached, the method updates the message and reward variables, displays the final grid, and
        terminates the loop.

        Parameters:
        None

        Returns:
        None
        """

        print("Starting the reversible path algorithm", "\n")
        movement_list = ["south", "west", "east", "north"]

        # While loop to keep running the controller until goal is achieved
        while self.agent.steps != 0:
            # Perceive the current state of the agent
            label = self.agent.agent_perceive()

            # Check if agent has reached the goal
            if self.agent.position == self.goal_pos:
                # Update message and display the grid
                self.message = "Episode ended, Agent achieved the Goal :D !!!"
                self.reward += 50
                self.display_grid()
                break
            # If goal not achieved, move the agent and update the grid
            else:
                self.action = random.choice(movement_list)
                label1 = self.valid_action(self.action)

                if label1 == "true":
                    self.agent_moving(self.action)
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
        print(f"< Reward: {self.reward} >")
        print(f"< Steps: {self.agent.steps} >")
        print(f"< Agent position: {self.agent.position} >")
        print(f"< Box pos: {self.agent.box_pos} >")
        print(f"< Agent moved: {self.action} >")
        print(f"< Is box in corner: {self.agent.is_box_in_corner()} >")
        print(f"< Is box next to wall: {self.agent.is_box_next_to_wall()} >")
        print(
            f"< Adjacent position with Agent - {self.agent.position} are: {self.get_adjacent_positions()} >"
        )
        print(f"< Is box reversible: {self.is_box_reversible()} >")
        print(f"< Sense 2 fields in south: {self.agent.agent_perceive_south()} >")
        print(f"< Sense 2 fields in east: {self.agent.agent_perceive_east()} >")
        print(f"< Sense 2 fields in west: {self.agent.agent_perceive_west()} >")
        print(f"< Sense 2 fields in north: {self.agent.agent_perceive_north()} >")
        print("", self.message, "\n")


a = Agent()
w = World(a)
w.display_grid()
w.agent_reversible_path()
