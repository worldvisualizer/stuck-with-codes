package amaze.puzzles

import amaze.LlamaAction
import amaze.LlamaController
import amaze.Maze
import amaze.core.GameController
import amaze.toMaze

fun main() {
    GameController(puzzles[1].toMaze(Puzzle2())).startGame()
}

/**
 * The llama has eyes!  Use [Maze.getEntityInFrontOfLlama] and turn if it's a forest.
 *
 * Kotlin makes it easy to check the instance of something
 * https://kotlinlang.org/docs/reference/typecasts.html#is-and-is-operators
 *
 * In Kotlin "if" can be used as an expression like:
 * return if (a > b) a else b // return max value
 */
class Puzzle2 : LlamaController {
    override fun getNextMove(maze: Maze): LlamaAction {
        return LlamaAction.MOVE_FORWARD
    }
}
