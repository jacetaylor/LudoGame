class Player:
    """
    The Player object represents the player who plays the game at a certain position.
    """

    def __init__(self, choice):
        self.choice = choice  # Player Name
        self.stacked = False  # Stacking
        if choice == 'A':  # Setting initial values for player A
            self.start_space = 1
            self.end_space = 50
            self.home_step_count_P = 0
            self.home_step_count_Q = 0
            self.current_pos_P = -1
            self.current_pos_Q = -1
            self.has_won = False
        elif choice == 'B':  # Setting initial values for player B
            self.start_space = 15
            self.end_space = 8
            self.home_step_count_P = 0
            self.home_step_count_Q = 0
            self.current_pos_P = -1
            self.current_pos_Q = -1
            self.has_won = False
        elif choice == 'C':  # Setting initial values for player C
            self.start_space = 29
            self.end_space = 22
            self.home_step_count_P = 0
            self.home_step_count_Q = 0
            self.current_pos_P = -1
            self.current_pos_Q = -1
            self.has_won = False
        else:  # Setting initial values for player D
            self.start_space = 43
            self.end_space = 36
            self.home_step_count_P = 0
            self.home_step_count_Q = 0
            self.current_pos_P = -1
            self.current_pos_Q = -1
            self.has_won = False

    def get_completed(self):
        """
        takes no parameters and returns True or False if the player has finished or not finished the game
        """

        if self.get_space_name(self.get_token_p_step_count()) == 'E' and \
                self.get_space_name(self.get_token_q_step_count()) == 'E':
            self.has_won = True
        return self.has_won

    def get_token_p_step_count(self):
        """
        takes no parameters and returns the total steps the token p has taken on the board
        """

        if self.choice == 'A':
            if self.current_pos_P == -1:
                return -1
            elif self.current_pos_P == 0:
                return 0
            elif self.current_pos_P == self.start_space:
                return 1
            elif self.current_pos_P > self.start_space and self.current_pos_P < self.end_space:
                return self.current_pos_P - self.start_space + 1
            else:
                return self.current_pos_P - self.start_space + self.home_step_count_P + 1

        else:
            if self.current_pos_P == -1:
                return -1
            elif self.current_pos_P == 0:
                return 0
            elif self.current_pos_P == self.start_space:
                return 1
            elif self.current_pos_P > self.start_space:
                return self.current_pos_P - self.start_space + 1
            elif self.current_pos_P < self.start_space and self.current_pos_P != self.end_space:
                return 56 - self.start_space + self.current_pos_P + 1
            else:
                return 56 - self.start_space + self.current_pos_P + self.home_step_count_P + 1

    def get_token_q_step_count(self):
        """
        takes no parameters and returns the total steps the token q has taken on the board
        """

        if self.choice == 'A':
            if self.current_pos_Q == -1:
                return -1
            elif self.current_pos_Q == 0:
                return 0
            elif self.current_pos_Q == self.start_space:
                return 1
            elif self.current_pos_Q > self.start_space and self.current_pos_Q < self.end_space:
                return self.current_pos_Q - self.start_space + 1
                # adding 1 to taking into account that home position is -1

            else:
                return self.current_pos_Q - self.start_space + self.home_step_count_Q + 1

        else:  # Positions B, C, D
            if self.current_pos_Q == -1:
                return -1
            elif self.current_pos_Q == 0:
                return 0
            elif self.current_pos_Q == self.start_space:
                return 1
            elif self.current_pos_Q > self.start_space:
                return self.current_pos_Q - self.start_space + 1
            elif self.current_pos_Q < self.start_space and self.current_pos_Q != self.end_space:
                return 56 - self.start_space + self.current_pos_Q + 1
            else:
                return 56 - self.start_space + self.current_pos_Q + self.home_step_count_Q + 1

    def get_space_name(self, steps):
        """
        takes as a parameter the total steps of the token and returns the name of the space
        the token has landed on as a string
        """

        if self.choice == 'A':
            if steps == -1:
                return 'H'
            elif steps == 0:
                return 'R'
            elif steps >= self.start_space and steps <= self.end_space:
                return self.start_space + steps - 1
            elif steps == 51:
                return self.choice + '1'
            elif steps == 52:
                return self.choice + '2'
            elif steps == 53:
                return self.choice + '3'
            elif steps == 54:
                return self.choice + '4'
            elif steps == 55:
                return self.choice + '5'
            elif steps == 56:
                return self.choice + '6'
            else:
                return 'E'

        else:
            if steps == -1:
                return 'H'
            elif steps == 0:
                return 'R'
            elif 1 <= steps <= (57 - self.start_space):
                return self.start_space + steps - 1
            elif 0 < (steps + self.start_space - 57) <= self.end_space:
                return steps + self.start_space - 57
            elif steps == 51:
                return self.choice + '1'
            elif steps == 52:
                return self.choice + '2'
            elif steps == 53:
                return self.choice + '3'
            elif steps == 54:
                return self.choice + '4'
            elif steps == 55:
                return self.choice + '5'
            elif steps == 56:
                return self.choice + '6'
            else:
                return 'E'


class LudoGame(Player):
    """
    The LudoGame object represents the game as played
    """
    player_list = []

    def __init__(self):
        super().__init__(self)
        self.game_status = [(-1, -1), (-1, -1), (-1, -1), (-1, -1)]  # Game Status to track of each player and its token

    def get_player_by_position(self, player_position):
        """
        takes a parameter representing the player’s position as a string and returns the player object.
        For an invalid string parameter, it will return 'Player not found!'
        """
        # bit_flag: 0 is false and 1 is true
        bit_flag = 0
        for player in self.player_list:
            if player_position == player.choice:
                bit_flag = 1
                return player
        if bit_flag == 0:
            return 'Player not found!'

    def play_game(self, players, turns):
        """
        This method will create the player list first using the players list pass in,
        and then move the tokens according to the turns list following the priority rule
        and update the tokens position and the player’s game state
        """

        if 1 < len(players) <= 4:  # Validating number of players that it should be between 2-4
            for player in players:
                self.player_list.append(Player(player))
        else:
            print('Wrong Number of Players')

        for turn in turns:
            count = 0
            for player in self.player_list:
                if player.get_completed() == True:
                    count += 1
            if count == (len(self.player_list) - 1):
                print('Game has finished')
                break

            # bit_flag: 0 is false and 1 is true

            bit_flag = 0
            for player in self.player_list:
                if turn[0] == player.choice:
                    if player.get_token_p_step_count() == -1 and player.get_token_q_step_count() == -1 \
                            and bit_flag == 0:
                        self.move_token(player, 'P', turn[1])
                        bit_flag = 1
                        # check parameters of Q and P
                    elif player.get_token_p_step_count() > -1 and player.get_token_q_step_count() == -1 \
                            and bit_flag == 0:
                        # if 6 and Q in Home, move token Q first
                        if turn[1] == 6:
                            self.move_token(player, 'Q', turn[1])
                            bit_flag = 1
                            # if 6 and Q is out of Home but P is in Home, move token P
                        else:
                            self.move_token(player, 'P', turn[1])
                            bit_flag = 1
                    else:
                        if 0 <= player.get_token_p_step_count() <= 50 and 0 <= player.get_token_q_step_count() <= 50 \
                                and bit_flag == 0:
                            for p in self.player_list:
                                if p.choice != player.choice:
                                    if p.get_space_name(p.get_token_q_step_count()) == player.get_space_name(
                                            player.get_token_p_step_count() + turn[1]) or p.get_space_name(
                                        p.get_token_p_step_count()) == player.get_space_name(
                                        player.get_token_p_step_count() + turn[
                                            1]) and player.get_token_q_step_count() != player.get_token_p_step_count() \
                                            and bit_flag == 0:
                                        self.move_token(player, 'P', turn[1])
                                        bit_flag = 1

                                    elif p.get_space_name(p.get_token_q_step_count()) == player.get_space_name(
                                            player.get_token_q_step_count() + turn[1]) or p.get_space_name(
                                        p.get_token_p_step_count()) == player.get_space_name(
                                        player.get_token_q_step_count() + turn[
                                            1]) and player.get_token_q_step_count() != player.get_token_p_step_count() \
                                            and bit_flag == 0:
                                        self.move_token(player, 'Q', turn[1])
                                        bit_flag = 1

                                    elif p.get_space_name(p.get_token_q_step_count()) == player.get_space_name(
                                            player.get_token_p_step_count() + turn[1]) or p.get_space_name(
                                        p.get_token_p_step_count()) == player.get_space_name(
                                        player.get_token_p_step_count() + turn[
                                            1]) and player.get_token_q_step_count() == player.get_token_p_step_count() \
                                            and bit_flag == 0:
                                        self.move_token(player, 'P', turn[1])
                                        self.move_token(player, 'Q', turn[1])
                                        bit_flag = 1
                                        player.stacked = True

                            if player.get_token_p_step_count() > player.get_token_q_step_count() and bit_flag == 0:
                                self.move_token(player, 'Q', turn[1])
                                bit_flag = 1

                            elif player.get_token_p_step_count() < player.get_token_q_step_count() and bit_flag == 0:
                                self.move_token(player, 'P', turn[1])
                                bit_flag = 1
                            else:
                                self.move_token(player, 'P', turn[1])
                                self.move_token(player, 'Q', turn[1])
                                bit_flag = 1
                                player.stacked = True

                        elif 0 <= player.get_token_p_step_count() <= 50 and \
                                50 < player.get_token_q_step_count() < 57 and bit_flag == 0:
                            if (player.get_token_q_step_count() + turn[1]) <= 57:
                                self.move_token(player, 'Q', turn[1])
                                bit_flag = 1
                            else:
                                self.move_token(player, 'P', turn[1])
                                bit_flag = 1

                        elif 0 <= player.get_token_q_step_count() <= 50 and \
                                50 < player.get_token_p_step_count() < 57 and bit_flag == 0:
                            if (player.get_token_p_step_count() + turn[1]) <= 57:
                                self.move_token(player, 'P', turn[1])
                                bit_flag = 1
                            else:
                                self.move_token(player, 'Q', turn[1])
                                bit_flag = 1

                        elif 50 < player.get_token_q_step_count() < 57 and \
                                50 < player.get_token_p_step_count() < 57 and bit_flag == 0:
                            if (player.get_token_q_step_count() + turn[1]) <= 57 and (
                                    player.get_token_p_step_count() + turn[1]) \
                                    <= 57 and player.get_token_q_step_count() == player.get_token_p_step_count() \
                                    and bit_flag == 0:
                                self.move_token(player, 'P', turn[1])
                                self.move_token(player, 'Q', turn[1])
                                bit_flag = 1
                                player.stacked = True
                            elif (player.get_token_p_step_count() + turn[1]) == 57 and bit_flag == 0:
                                self.move_token(player, 'P', turn[1])
                                bit_flag = 1
                            elif (player.get_token_q_step_count() + turn[1]) == 57 and bit_flag == 0:
                                self.move_token(player, 'Q', turn[1])
                                bit_flag = 1
                            elif (player.get_token_q_step_count() + turn[1]) <= 57 and (
                                    player.get_token_p_step_count() + turn[
                                1]) <= 57 and player.get_token_q_step_count() < player.get_token_p_step_count() \
                                    and bit_flag == 0:
                                self.move_token(player, 'Q', turn[1])
                                bit_flag = 1
                            elif (player.get_token_q_step_count() + turn[1]) <= 57 and (
                                    player.get_token_p_step_count() + turn[
                                1]) <= 57 and player.get_token_q_step_count() > player.get_token_p_step_count() \
                                    and bit_flag == 0:
                                self.move_token(player, 'P', turn[1])
                                bit_flag = 1

        current_tokens_space = []  # for mapping the current token status for each player
        for player in players:
            if player == 'A':
                current_tokens_space.append(self.game_status[0][0])
                current_tokens_space.append(self.game_status[0][1])
            elif player == 'B':
                current_tokens_space.append(self.game_status[1][0])
                current_tokens_space.append(self.game_status[1][1])
            elif player == 'C':
                current_tokens_space.append(self.game_status[2][0])
                current_tokens_space.append(self.game_status[2][1])
            elif player == 'D':
                current_tokens_space.append(self.game_status[3][0])
                current_tokens_space.append(self.game_status[3][1])

        return current_tokens_space

    def move_token(self, player, token, steps):
        """
        takes three parameters, the player object, the token name (‘p’ or ‘q’)
        and the steps the token will move on the board (int).
        This method will take care of one token moving on the board.
        It will also update the token’s total steps,
        and it will take care of kicking out other opponent tokens as needed.
        The play_game method will use this method
        """

        # defining R position
        if token == 'P' and player.get_token_p_step_count() == -1 and steps == 6:
            player.current_pos_P = 0

        elif token == 'Q' and player.get_token_q_step_count() == -1 and steps == 6:
            player.current_pos_Q = 0

        elif token == 'P' and player.get_token_p_step_count() == 0:
            player.current_pos_P = player.start_space + steps - 1

            # see if stacked
            for p in self.player_list:
                if p.choice != player.choice:
                    if p.get_space_name(p.get_token_p_step_count()) == player.get_space_name(
                            player.get_token_p_step_count()) and \
                            p.get_space_name(p.get_token_q_step_count()) == \
                            player.get_space_name(player.get_token_p_step_count()):
                        p.current_pos_P = -1
                        p.current_pos_Q = -1
                        p.stacked = False

                    elif p.get_space_name(p.get_token_p_step_count()) == player.get_space_name(
                            player.get_token_p_step_count()):
                        p.current_pos_P = -1

                    elif p.get_space_name(p.get_token_q_step_count()) == player.get_space_name(
                            player.get_token_p_step_count()):
                        p.current_pos_Q = -1

        # defining H
        elif token == 'Q' and player.get_token_q_step_count() == 0:
            player.current_pos_Q = player.start_space + steps - 1
            for p in self.player_list:
                if p.choice != player.choice:
                    if p.get_space_name(p.get_token_p_step_count()) == player.get_space_name(
                            player.get_token_q_step_count()) and \
                            p.get_space_name(p.get_token_q_step_count()) == \
                            player.get_space_name(player.get_token_q_step_count()):
                        p.current_pos_P = -1
                        p.current_pos_Q = -1
                        p.stacked = False

                    elif p.get_space_name(p.get_token_p_step_count()) == player.get_space_name(
                            player.get_token_q_step_count()):
                        p.current_pos_P = -1

                    elif p.get_space_name(p.get_token_q_step_count()) == player.get_space_name(
                            player.get_token_q_step_count()):
                        p.current_pos_Q = -1

        # p step count
        elif token == 'P' and player.get_token_p_step_count() > 0 and (player.get_token_p_step_count() + steps) <= 50:
            if (player.current_pos_P + steps) <= 56:
                player.current_pos_P = player.current_pos_P + steps
            else:
                player.current_pos_P = player.current_pos_P + steps - 56

            for p in self.player_list:
                if p.choice != player.choice:
                    if p.get_space_name(p.get_token_p_step_count()) == player.get_space_name(
                            player.get_token_p_step_count()) and \
                            p.get_space_name(p.get_token_q_step_count()) == \
                            player.get_space_name(player.get_token_p_step_count()):
                        p.current_pos_P = -1
                        p.current_pos_Q = -1

                    elif p.get_space_name(p.get_token_p_step_count()) == player.get_space_name(
                            player.get_token_p_step_count()):
                        p.current_pos_P = -1

                    elif p.get_space_name(p.get_token_q_step_count()) == player.get_space_name(
                            player.get_token_p_step_count()):
                        p.current_pos_Q = -1

        # conditions to get P into E
        elif token == 'P' and 50 < (player.get_token_p_step_count() + steps) <= 57:
            if player.home_step_count_P + steps <= 6:
                player.home_step_count_P = player.home_step_count_P + steps - (player.end_space - player.current_pos_P)
            elif player.home_step_count_P + steps == 7:
                player.home_step_count_P = player.home_step_count_P + steps - (player.end_space - player.current_pos_P)
            player.current_pos_P = player.end_space

        # Q step count
        elif token == 'Q' and player.get_token_q_step_count() > 0 and (player.get_token_q_step_count() + steps) <= 50:
            if (player.current_pos_Q + steps) <= 56:
                player.current_pos_Q = player.current_pos_Q + steps
            else:
                player.current_pos_Q = player.current_pos_Q + steps - 56

            for p in self.player_list:
                if p.choice != player.choice:
                    if p.get_space_name(p.get_token_p_step_count()) == player.get_space_name(
                            player.get_token_q_step_count()) and \
                            p.get_space_name(p.get_token_q_step_count()) == \
                            player.get_space_name(player.get_token_q_step_count()):
                        p.current_pos_P = -1
                        p.current_pos_Q = -1
                    elif p.get_space_name(p.get_token_p_step_count()) == player.get_space_name(
                            player.get_token_q_step_count()):
                        p.current_pos_P = -1
                    elif p.get_space_name(p.get_token_q_step_count()) == player.get_space_name(
                            player.get_token_q_step_count()):
                        p.current_pos_Q = -1

        # conditions to get Q into E
        elif token == 'Q' and 50 < (player.get_token_q_step_count() + steps) <= 57:
            if player.home_step_count_Q + steps <= 6:
                player.home_step_count_Q = player.home_step_count_Q + steps - (player.end_space - player.current_pos_Q)
            elif player.home_step_count_Q + steps == 7:
                player.home_step_count_Q = player.home_step_count_Q + steps
            player.current_pos_Q = player.end_space

        # winning status
        for p in self.player_list:
            if p.choice == 'A':
                self.game_status[0] = (
                    p.get_space_name(p.get_token_p_step_count()), p.get_space_name(p.get_token_q_step_count()))
                if self.game_status[0] == ('E', 'E'):
                    p.has_won = True
            elif p.choice == 'B':
                self.game_status[1] = (
                    p.get_space_name(p.get_token_p_step_count()), p.get_space_name(p.get_token_q_step_count()))
                if self.game_status[1] == ('E', 'E'):
                    p.has_won = True
            elif p.choice == 'C':
                self.game_status[2] = (
                    p.get_space_name(p.get_token_p_step_count()), p.get_space_name(p.get_token_q_step_count()))
                if self.game_status[2] == ('E', 'E'):
                    p.has_won = True
            elif p.choice == 'D':
                self.game_status[3] = (
                    p.get_space_name(p.get_token_p_step_count()), p.get_space_name(p.get_token_q_step_count()))
                if self.game_status[3] == ('E', 'E'):
                    p.has_won = True