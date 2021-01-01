package amaze.puzzles

import amaze.LlamaAction
import amaze.LlamaController
import amaze.Maze
import amaze.core.GameController
import amaze.toMaze

fun main() {
    GameController(puzzles[7].toMaze(Puzzle8())).startGame()
}

/**
 * Don't get stuck in a loop!
 *
 * Hint:
 * Don't focus on an optimal solution immediately.
 */
class Puzzle8 : LlamaController {
    override fun getNextMove(maze: Maze): LlamaAction {
        return LlamaAction.MOVE_FORWARD
    }
}
