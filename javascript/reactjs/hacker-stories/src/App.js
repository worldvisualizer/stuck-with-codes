import logo from './logo.svg';
import './App.css';

const list = [
  {
    title: "React",
    url: 'https://reactjs.org'
  },
  {
    title: "Redux",
    url: 'https://redux.js.org'

  }
]

function App() {
  return (
    <div>
      <h1>Hello World</h1>
      <ul>
        {
          list.map((item) => {return <li>{item.title}</li>;})
        }
      </ul>
    </div>
  );
}

export default App;
