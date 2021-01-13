package com.example.livedataapp

import androidx.lifecycle.LiveData
import androidx.room.*

@Dao
interface ItemDao {
    @Insert
    fun insertItem(location: Item?): Long?

    @Query("SELECT * FROM Item ORDER BY id DESC")
    fun getAllItems(): LiveData<List<Item?>?>?

    @Query("SELECT * FROM Item WHERE id = :id")
    fun getItem(id: Int): LiveData<Item?>?

    @Update
    fun updateItem(item: Item?)

    @Delete
    fun deleteItem(item: Item?)

    @Query("DELETE FROM Item")
    fun clear()
}