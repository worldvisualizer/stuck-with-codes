package coroutines

import kotlinx.coroutines.* 

class CoroutineApp {
    val greeting: String
        get() {
            return "Hello world."
        }

    // suspend function is really,
    // function that can be suspended and resumed
    suspend fun suspendingFunc() : Int {
        delay(1000L)
        println("does this work?")
        return 42
    }
}

fun globalScope() {
    GlobalScope.launch {
        delay(1000L)
        println("first global scope coroutine")
    }
    // delay function belongs to coroutine
    // current thread to sleep
    println(CoroutineApp().greeting)
    Thread.sleep(2000L)
}

fun runBlocking() {
    // same result as globalScope
    GlobalScope.launch {
        delay(1000L)
        println("run blocking")
    }
    println(CoroutineApp().greeting)
    runBlocking {
        // thread invoking run blocking
        // blocks until this is complete
        delay(2000L)
    }
}

// runBlocking wraps the function
// and this function is run in main thread
fun runBlockingIdiomatic() = runBlocking<Unit> {
    GlobalScope.launch {
        delay(1000L)
        println("run blocking")
    }
    println(CoroutineApp().greeting)
    delay(2000L)
}

// now you don't need delay anymore,
// because runBlocking CoroutineScope
// checks if all child coroutines have completed
// before exiting
fun runBlockingCoroutineScope() = runBlocking {
    launch {
        delay(1000L)
        println("run blocking")
    }
    println(CoroutineApp().greeting)
}

fun nestedLaunch() = runBlocking { // this: CoroutineScope
    launch { 
        delay(200L)
        println("Task from runBlocking")
    }
    
    coroutineScope { // Creates a coroutine scope
        launch {
            delay(500L) 
            println("Task from nested launch")
        }
    
        delay(100L)
        println("Task from coroutine scope") // This line will be printed before the nested launch
    }
    
    println("Coroutine scope is over") // This line is not printed until the nested launch completes
}

fun main(args: Array<String>) {
    globalScope()
    runBlocking()
    runBlockingIdiomatic()
    runBlockingCoroutineScope()
    nestedLaunch()
}
