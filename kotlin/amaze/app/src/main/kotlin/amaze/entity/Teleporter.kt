package amaze.entity

import amaze.Llama
import amaze.LlamaState
import amaze.Position
import amaze.core.assets.Images
import amaze.core.assets.draw
import java.awt.Graphics2D

/**
 * A [Teleporter] is a quantum mechanical device which transports the llama by taking advantage of
 * quantum entanglement.
 */
class Teleporter(private val endpoint: Position) : Entity {
    override fun draw(graphics: Graphics2D, width: Int, height: Int) {
        Images.walkway.draw(graphics, width, height)
        Images.teleporter.draw(graphics, width, height)
    }

    override fun interact(llama: Llama) {
        llama.teleporterStateTransition(LlamaState.MOVING_ONTO_TELEPORTER, endpoint)
    }
}
