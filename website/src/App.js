import React from 'react';
import './App.css';

import { Navbar } from 'react-bulma-components/full'
import { Modal } from 'react-bulma-components/full'
import { Section } from 'react-bulma-components/full'

import NavModal from './components/NavModal'

function App() {
  return (
    <Navbar active={true} fixed={'top'} color={'info'}>
        <Navbar.Brand>
          <Navbar.Item>PennTrade</Navbar.Item>
        </Navbar.Brand>
        <Navbar.Menu>
          <Navbar.Container>
            <NavModal modal={{ closeOnBlur: true }} >
              <Modal.Content>
                <Section>
                  Sap bro
                </Section>
              </Modal.Content>
            </NavModal>
            <Navbar.Item href="https://www.omfgdogs.com">Signup</Navbar.Item>
          </Navbar.Container>
        </Navbar.Menu>
        
    </Navbar>

  );
}

export default App;
