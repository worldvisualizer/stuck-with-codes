package amaze.puzzles

import amaze.LlamaAction
import amaze.LlamaController
import amaze.Maze
import amaze.core.GameController
import amaze.toMaze


fun main() {
    GameController(puzzles[10].toMaze(Puzzle11())).startGame()
}

/**
 * Dont blink
 */
class Puzzle11 : LlamaController {
    override fun getNextMove(maze: Maze): LlamaAction {
        return LlamaAction.MOVE_FORWARD
    }
}