package amaze.puzzles

import amaze.LlamaAction
import amaze.LlamaController
import amaze.Maze
import amaze.core.GameController
import amaze.toMaze

fun main() {
    GameController(puzzles[6].toMaze(Puzzle7())).startGame()
}

/**
 * Who put that alien tech in the Llama forest?
 */
class Puzzle7 : LlamaController {
    override fun getNextMove(maze: Maze): LlamaAction {
        return LlamaAction.MOVE_FORWARD
    }
}
