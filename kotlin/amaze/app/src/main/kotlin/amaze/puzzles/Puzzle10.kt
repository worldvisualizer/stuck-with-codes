package amaze.puzzles

import amaze.LlamaAction
import amaze.LlamaController
import amaze.Maze
import amaze.core.GameController
import amaze.toMaze

fun main() {
    GameController(puzzles[9].toMaze(Puzzle10())).startGame()
}

/**
 * Achieve enlightenment by being one with the llama.  Good Luck!
 */
class Puzzle10 : LlamaController {
    override fun getNextMove(maze: Maze): LlamaAction {
        return LlamaAction.MOVE_FORWARD
    }
}
