import './App.css';
import Navbar from './components/Navbar'
import HomePage from './pages/HomePage'
import ServicePage from './pages/ServicePage'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

function App() {
  return (
    <Router>
    <div className="App">
        <Navbar/>
        <Routes>
          <Route path='/' exact Component={HomePage}/>
          <Route path='/service' exact Component={ServicePage}/>
        </Routes>
    </div>
    </Router>
  );
}

export default App;
