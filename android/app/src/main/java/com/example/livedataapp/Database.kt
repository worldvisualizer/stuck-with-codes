package com.example.livedataapp

import androidx.room.Database
import androidx.room.RoomDatabase

@Database(entities = [Item::class], version = 3, exportSchema = false)
abstract class Database : RoomDatabase() {
    abstract fun dao(): ItemDao?
}