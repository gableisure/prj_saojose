import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Container from './components/layouts/Container';
import Navbar from './components/layouts/Navbar';
import Home from './components/pages/Home';


function App() {
  return (
      <Router>
        <Navbar />
        <Switch>
          <Container customClass="min-height">
            <Route exact path="/"><Home/></Route>
          </Container>
        </Switch>
      </Router>
  );
}

export default App;

