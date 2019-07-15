import React from 'react';
import './App.css';

import { Navbar } from 'react-bulma-components/full'

function App() {
  return (
    <Navbar active={true} fixed={'top'} color={'info'}>
        <Navbar.Brand>
          <Navbar.Item>PennTrade</Navbar.Item>
        </Navbar.Brand>
        <Navbar.Menu>
          <Navbar.Container>
            <Navbar.Item href="https://www.omfgdogs.com">Login</Navbar.Item>
            <Navbar.Item href="https://www.omfgdogs.com">Signup</Navbar.Item>
          </Navbar.Container>
        </Navbar.Menu>
        
    </Navbar>

  );
}

export default App;
