package com.example.livedataapp

import androidx.room.Entity
import androidx.room.PrimaryKey

@Entity
class Item {
    @PrimaryKey(autoGenerate = true)
    var id = 0
    var description = ""
    var weight = 0.0
    var createdAt: Long = 0
}