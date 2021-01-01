package amaze.entity

import amaze.Llama
import amaze.LlamaState
import amaze.core.assets.Images
import amaze.core.assets.draw
import java.awt.Graphics2D

/**
 * The llama can fall in a [Pit].
 */
object Pit : Entity {
    override fun draw(graphics: Graphics2D, width: Int, height: Int) {
        Images.walkway.draw(graphics, width, height)
        Images.pit.draw(graphics, width, height)
    }

    override fun interact(llama: Llama) {
        llama.transitionToState(LlamaState.ENTERING_PIT)
    }
}
