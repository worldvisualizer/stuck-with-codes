package amaze.puzzles

import amaze.entity.VanishingWalkwayPattern


data class PuzzleDefinition(
    val tileMap: String,
    val vanishingWalkwayPatterns: List<VanishingWalkwayPattern> = emptyList()
)
