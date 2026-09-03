import curses
import random


def game(screen):
    curses.curs_set(0)

    screen_height, screen_width = screen.getmaxyx()

    window = curses.newwin(screen_height, screen_width, 0, 0)
    window.keypad(1)
    window.timeout(35)

    snake_x = screen_width // 4
    snake_y = screen_height // 2

    snake = [
        [snake_y, snake_x],
        [snake_y, snake_x - 1],
        [snake_y, snake_x - 2]
    ]

    food = [
        screen_height // 2,
        screen_width // 2
    ]

    while food in snake:
        food = [
            random.randint(1, screen_height - 2),
            random.randint(1, screen_width - 2)
        ]

    window.addch(food[0], food[1], curses.ACS_PI)

    key = curses.KEY_RIGHT
    score = 0

    while True:

        next_key = window.getch()

        if next_key != -1:
            if (
                next_key == curses.KEY_UP and key != curses.KEY_DOWN
            ) or (
                next_key == curses.KEY_DOWN and key != curses.KEY_UP
            ) or (
                next_key == curses.KEY_LEFT and key != curses.KEY_RIGHT
            ) or (
                next_key == curses.KEY_RIGHT and key != curses.KEY_LEFT
            ):
                key = next_key

        new_head = [snake[0][0], snake[0][1]]

        if key == curses.KEY_DOWN:
            new_head[0] += 1
        elif key == curses.KEY_UP:
            new_head[0] -= 1
        elif key == curses.KEY_LEFT:
            new_head[1] -= 1
        elif key == curses.KEY_RIGHT:
            new_head[1] += 1

        if (
            new_head[0] in [0, screen_height - 1]
            or new_head[1] in [0, screen_width - 1]
            or new_head in snake
        ):
            window.addstr(
                screen_height // 2,
                max(0, screen_width // 2 - 5),
                "Game Over!"
            )
            window.addstr(
                screen_height // 2 + 1,
                max(0, screen_width // 2 - 7),
                f"Score: {score}"
            )
            window.refresh()
            window.getch()
            break

        snake.insert(0, new_head)

        if snake[0] == food:
            score += 1

            while True:
                new_food = [
                    random.randint(1, screen_height - 2),
                    random.randint(1, screen_width - 2)
                ]

                if new_food not in snake:
                    food = new_food
                    break

            window.addch(food[0], food[1], curses.ACS_PI)

        else:
            tail = snake.pop()
            window.addch(tail[0], tail[1], " ")

        window.addstr(0, 2, f"Score: {score}")

        window.addch(
            snake[0][0],
            snake[0][1],
            curses.ACS_CKBOARD
        )


def main():
    curses.wrapper(game)


if __name__ == "__main__":
    main()
