package amaze.puzzles

import amaze.LlamaAction
import amaze.LlamaController
import amaze.Maze
import amaze.core.GameController
import amaze.toMaze

fun main() {
    GameController(puzzles[4].toMaze(Puzzle5())).startGame()
}

/**
 * Mazes are getting more complicated now
 *
 * Hint:
 * You can be lazy and stick to a side.
 */
class Puzzle5 : LlamaController {
    override fun getNextMove(maze: Maze): LlamaAction {
        return LlamaAction.MOVE_FORWARD
    }
}
