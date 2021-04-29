package coroutines

import kotlinx.coroutines.*
import kotlin.system.measureTimeMillis

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

suspend fun doSomethingOne() : Int {
    delay(1000L)
    return 13
}

suspend fun doSomethingTwo() : Int {
    delay(1100L)
    return 29
}

// making suspend functions async
fun doSomethingOneAsync() = GlobalScope.async {
    doSomethingOne()
}

fun doSomethingTwoAsync() = GlobalScope.async {
    doSomethingTwo()
}

fun measureTimeSequential() = runBlocking {
    // sequential invocation
    // to the extent that after doSomethingOne exits, doSomethingTwo runs
    val time = measureTimeMillis {
        val one = doSomethingOne()
        val two = doSomethingTwo()
        println("answer: ${one + two}")
    }
    println("seq completed in $time ms")
}

fun measureTimeAsync() = runBlocking {
    val time = measureTimeMillis {
        val one = async { doSomethingOne() }
        val two = async { doSomethingTwo() }
        println("answer: ${one.await() + two.await()}")
    }
    println("async completed in $time ms")
}

fun measureTimeLazyAsync() = runBlocking {
    val time = measureTimeMillis {
        val one = async(start = CoroutineStart.LAZY) { doSomethingOne() }
        val two = async(start = CoroutineStart.LAZY) { doSomethingTwo() }
        // lazily invoked only by await() or start()
        // if started, we expect 1100 ms runtime
        // one.start()
        // two.start()

        // instead, we see 2100 ms runtime
        println("answer: ${one.await() + two.await()}")
    }
    println("lazy async completed in $time ms")
}

fun measureTimeAsyncFunction() {
    val time = measureTimeMillis {
        // this still running when outer block has problem.
        // problem addressed with coroutineScope
        val one = doSomethingOneAsync()
        val two = doSomethingTwoAsync()
        runBlocking {
            println("answer: ${one.await() + two.await()}")
        }
    }
    println("async func completed in $time ms")
}

// concurrent sum
suspend fun concurrentSum(): Int = coroutineScope {
    val one = async { doSomethingOne() }
    val two = async { doSomethingTwo() }
    one.await() + two.await()
}

fun measureTimeAsyncCoroutineScope() = runBlocking {
    val time = measureTimeMillis {
        println("answer: ${concurrentSum()}")
    }
    println("coroutine scope async completed in $time ms")
}

fun main(args: Array<String>) {
    globalScope()
    runBlocking()
    runBlockingIdiomatic()
    runBlockingCoroutineScope()
    nestedLaunch()
    measureTimeSequential()
    measureTimeAsync()
    measureTimeLazyAsync()
    measureTimeAsyncFunction()
    measureTimeAsyncCoroutineScope()
}
