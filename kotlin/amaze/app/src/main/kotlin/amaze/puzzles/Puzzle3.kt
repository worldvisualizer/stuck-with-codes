package amaze.puzzles

import amaze.LlamaAction
import amaze.LlamaController
import amaze.Maze
import amaze.core.GameController
import amaze.toMaze

fun main() {
    GameController(puzzles[2].toMaze(Puzzle3())).startGame()
}

/**
 * Some mazes can start you in a few different locations!
 *
 * The when expression is very useful
 * https://kotlinlang.org/docs/reference/control-flow.html#when-expression
 *
 * Hints:
 * There is a specific condition when you should always turn left.
 * There is a specific condition when you should always turn right.
 */
class Puzzle3 : LlamaController {
    override fun getNextMove(maze: Maze): LlamaAction {
        return LlamaAction.MOVE_FORWARD
    }
}
