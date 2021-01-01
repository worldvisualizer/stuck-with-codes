package amaze.puzzles

import amaze.LlamaAction
import amaze.LlamaController
import amaze.Maze
import amaze.core.GameController
import amaze.toMaze

fun main() {
    GameController(puzzles[0].toMaze(Puzzle1())).startGame()
}

/**
 * The llama is experiencing rightward drunkenness!
 *
 * Fix the [getNextMove] method to make the llama move forward.
 */
class Puzzle1 : LlamaController {
    override fun getNextMove(maze: Maze): LlamaAction {
        return LlamaAction.TURN_RIGHT
    }
}
