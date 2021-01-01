package amaze.puzzles

import amaze.LlamaAction
import amaze.LlamaController
import amaze.Maze
import amaze.core.GameController
import amaze.toMaze

fun main() {
    GameController(puzzles[5].toMaze(Puzzle6())).startGame()
}

/**
 * Prepared to be AMazed!
 *
 * Hint:
 * Pits are really no different from forests.
 */
class Puzzle6 : LlamaController {
    override fun getNextMove(maze: Maze): LlamaAction {
        return LlamaAction.MOVE_FORWARD
    }
}
