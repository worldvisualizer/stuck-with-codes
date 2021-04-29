import React from "react"
import ReactDOM from "react-dom"
import { makeAutoObservable } from "mobx"
import { observer } from "mobx-react"

import logo from './logo.svg'
import './App.css'

class Timer {
    secondsPassed = 0
    constructor() {
        makeAutoObservable(this)
    }

    increase() {
        this.secondsPassed += 1
    }

    reset() {
        this.secondsPassed = 0
    }
}

function App() {
    const myTimer = new Timer()
    const TimerView = observer(({ timer }) => (
        <button onClick={() => timer.reset()}>Seconds passed: {timer.secondsPassed}</button>
    ))

    setInterval(() => {
	myTimer.increase()
    }, 1000)
    return (
        <div className="App">
            <header className="App-header">
            <img src={logo} className="App-logo" alt="logo" />
            <p>
                <TimerView timer={myTimer} />
            </p>
            <a
                className="App-link"
                href="https://reactjs.org"
                target="_blank"
                rel="noopener noreferrer"
            >
            Learn React
            </a>
            </header>
        </div>
  );
}

export default App;
