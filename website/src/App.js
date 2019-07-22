import React from 'react';
import './App.css';

import { Navbar } from 'react-bulma-components/full'
import { Modal } from 'react-bulma-components/full'
import { Form } from 'react-bulma-components/full'

import NavModal from './components/NavModal'

function App() {
  return (
    <>
    <Navbar active={true} fixed={'top'} color={'info'}>
        <Navbar.Brand>
          <Navbar.Item>PennTrade</Navbar.Item>
        </Navbar.Brand>
        <Navbar.Menu>
          <Navbar.Container>
            <NavModal modal={{ closeOnBlur: true}} name="Login">
              <Modal.Card>
                <Modal.Card.Head showClose={false}>
                  <Modal.Card.Title>Login</Modal.Card.Title>
                </Modal.Card.Head>
                <Modal.Card.Body>
                  <Form.Field>
                    <Form.Label>Username</Form.Label>
                    <Form.Control>
                      <Form.Input placeholder="Text input" />
                    </Form.Control>
                  </Form.Field>
                  <Form.Field>
                    <Form.Label>Password</Form.Label>
                    <Form.Control>
                      <Form.Input type="password" placeholder="password"/> 
                    </Form.Control>
                  </Form.Field>
                </Modal.Card.Body>
                <Modal.Card.Foot style={{ alignItems: 'center', justifyContent: 'center' }}>
                  <p>Lorem Ipsum...</p>
                </Modal.Card.Foot>
              </Modal.Card>
            </NavModal>
            <Navbar.Item href="https://www.omfgdogs.com">Signup</Navbar.Item>
          </Navbar.Container>
        </Navbar.Menu>
         
    </Navbar>
    </>
  );
}

export default App;
