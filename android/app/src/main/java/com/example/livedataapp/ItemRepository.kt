package com.example.livedataapp

import android.content.Context
import androidx.lifecycle.LiveData
import androidx.room.Room
import androidx.room.migration.Migration
import androidx.sqlite.db.SupportSQLiteDatabase
import kotlinx.coroutines.coroutineScope

class ItemRepository(context: Context) {
    private val DB_NAME = "itemdb"
    private val db: Database

    init {
        db = Room.databaseBuilder<Database>(context, Database::class.java, DB_NAME)
            .build()
    }

    suspend fun insertItem(item: Item): Long? {
        return coroutineScope {
            db.dao()?.insertItem(item)
        }
    }

    suspend fun updateItem(item: Item?): Unit? {
        return coroutineScope {
            db.dao()?.updateItem(item)
        }
    }

    suspend fun deleteItem(id: Int) {
        getItem(id)?.let { item ->
            coroutineScope {
                db.dao()?.deleteItem(item.value)
            }
        }
    }

    fun getItem(id: Int): LiveData<Item?>? {
        return db.dao()?.getItem(id)
    }

    fun getAllItems(): LiveData<List<Item?>?>? {
        return db.dao()?.getAllItems()
    }
}
