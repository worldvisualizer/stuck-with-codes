package amaze.puzzles

import amaze.LlamaAction
import amaze.LlamaController
import amaze.Maze
import amaze.core.GameController
import amaze.toMaze

fun main() {
    GameController(puzzles[3].toMaze(Puzzle4())).startGame()
}

/**
 * Going down every path is not wise, danger awaits!
 *
 * Hint:
 * You'll want to store some state in this class.
 */
class Puzzle4 : LlamaController {
    override fun getNextMove(maze: Maze): LlamaAction {
        return LlamaAction.MOVE_FORWARD
    }
}
